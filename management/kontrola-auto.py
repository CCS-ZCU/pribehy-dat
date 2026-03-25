import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import google_conf

# Define configurations for each class
class_configurations = [
    {
        "class_name": "UDHB",
        "students_file": "UDHB_students2026.csv",
        "sheet_url": "https://docs.google.com/spreadsheets/d/1saYGp44qhq6a-06w4_r3ifgPriIrYp_mv9vxUrsLtU4/edit?usp=sharing",
        "notebooks_to_keep": ["site", "gis", "http", "nlp", "pdf"]
    },
    {
        "class_name": "KDDHB",
        "students_file": "KDDHB_students2026.csv",
        "sheet_url": "https://docs.google.com/spreadsheets/d/1-sAQHJ5l6By2HiSdcU35UzG35eH0BCPIeGvTF3bLZNw/edit?usp=sharing",
        "notebooks_to_keep": ["http", "api", "tei", "regex", "pdf"]
    }
]

def clean_user(user):
    try:
        return re.search(r"F\d+\w\d+[PK]?", user.replace("O", "0"), re.IGNORECASE).group()
    except:
        print(user)
        return None # Return None for users that don't match the pattern

def process_class_data(config):
    class_name = config["class_name"]
    students_file = config["students_file"]
    sheet_url = config["sheet_url"]
    notebooks_to_keep = config["notebooks_to_keep"]

    print(f"Processing data for class: {class_name}")

    # get addresses of individual checkpoints
    resp = requests.get("https://sciencedata.dk/public/082a018b1f2fd125ef4907f01ab2e2cf/") # latest data
    soup = BeautifulSoup(resp.content, "html.parser")
    address = []
    for item in soup.find_all("a"):
        href = item.get('href')
        if href and '.json' in href:
            address.append(href)

    data = []
    for item in address:
        resp = requests.get('https://sciencedata.dk' + str(item))
        data.append(json.loads(resp.text))

    data_df = pd.DataFrame(data)
    data_df["osCislo"] = data_df["user"].apply(clean_user)
    data_df.dropna(subset=["osCislo"], inplace=True) # Remove rows where osCislo couldn't be extracted

    # groupby the data by notebook names
    table = data_df.groupby(["osCislo", "ntb"]).size().unstack(fill_value=0)
    table = table.clip(upper=2) # maximal value for notebook is 2
    table.reset_index(inplace=True)

    # load students data exported from portal
    students_df = pd.read_csv(f"../data/students_data/{students_file}", sep=";", encoding='cp1250')
    students_df = students_df[students_df["stav"]=="S"]
    students_df = students_df[["osCislo", "prijmeni","jmeno", "userName"]]

    merged_df = pd.merge(students_df, table, on="osCislo", how="left")
    merged_df.fillna(0, inplace=True)

    # Ensure all notebooks_to_keep columns exist in merged_df, add if missing with 0
    for notebook in notebooks_to_keep:
        if notebook not in merged_df.columns:
            merged_df[notebook] = 0

    # keep only the specified notebooks and personal number...
    merged_df = merged_df[["osCislo"] + notebooks_to_keep]

    # sum up the values
    merged_df["sum"] = merged_df[notebooks_to_keep].sum(axis=1)

    # get today's date
    date = pd.Timestamp.today().strftime("%Y-%m-%d")

    cviceni_plneni = google_conf.setup(
        sheet_url=sheet_url,
        service_account_path="../../../ServiceAccountsKey.json")

    # upload the data to google sheets
    n = 0
    sheet_created = False

    while not sheet_created:
        try:
            if n == 0:
                sheet_name = f"{class_name.lower()}_{date}"  # Default name
            else:
                sheet_name = f"{class_name.lower()}_{date}_{n}"  # Incremented name

            # Create the worksheet and upload the DataFrame
            google_conf.set_with_dataframe(cviceni_plneni.add_worksheet(sheet_name, rows=1, cols=1), merged_df.reset_index())
            sheet_created = True  # If successful, mark as created
            print(f"Successfully uploaded data for {class_name} to sheet: {sheet_name}")
        except Exception as e:
            n += 1
            print(f"Worksheet with name '{sheet_name}' already exists for {class_name}. Trying another name...")
            if n > 10: # Prevent infinite loop in case of persistent error
                print(f"Failed to create a unique sheet name for {class_name} after multiple attempts. Error: {e}")
                break

# Iterate through each class configuration and process the data
for config in class_configurations:
    process_class_data(config)
