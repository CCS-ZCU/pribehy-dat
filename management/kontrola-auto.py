import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import google_conf

# get addresses of individual checkpoints
resp = requests.get("https://sciencedata.dk/public/082a018b1f2fd125ef4907f01ab2e2cf/") # 2025
#resp = requests.get("https://sciencedata.dk/public/ede416946cfd3b35dcf1e61ac68da5de") # 2024
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

def clean_user(user):
    try:
        return re.search(r"F\d+\w\d+[PK]?", user.replace("O", "0"), re.IGNORECASE).group()
    except:
        print(user)
data_df["osCislo"] = data_df["user"].apply(clean_user)

# groupby the data by notebook names
table = data_df.groupby(["osCislo", "ntb"]).size().unstack(fill_value=0)
table = table.clip(upper=2) # maximal value for notebook is 2
table.reset_index(inplace=True)


# load  students data exported from portal
students_df = pd.read_csv("../data/UDHB_students2025.csv", sep=";", encoding='cp1250')
students_df = students_df[students_df["stav"]=="S"]
students_df = students_df[["osCislo", "prijmeni","jmeno", "userName"]]

merged_df = pd.merge(students_df, table, on="osCislo", how="left")
merged_df.fillna(0, inplace=True)

# keep only the 5 notebooks and personal number...
merged_df = merged_df[["osCislo", "site", "gis", "http", "nlp", "pdf"]]

# sum up the values
merged_df["sum"] = merged_df[["gis", "site", "http", "nlp", "pdf"]].sum(axis=1)

# get today's date
date = pd.Timestamp.today().strftime("%Y-%m-%d")
import google_conf

cviceni_plneni = google_conf.setup(
    sheet_url="https://docs.google.com/spreadsheets/d/1DjmDNSVgiqxNjFzHWKZ1iBkK6NPlbL6gxohoH-kqUYg/edit?usp=sharing",
    service_account_path="../../../ServiceAccountsKey.json")
#%%

# upload the data to google sheets
n = 0
sheet_created = False

while not sheet_created:
    try:
        # Attempt to create the worksheet with the appropriate name
        if n == 0:
            sheet_name = f"udhb_{date}"  # Default name
        else:
            sheet_name = f"udhb_{date}_{n}"  # Incremented name

        # Create the worksheet and upload the DataFrame
        google_conf.set_with_dataframe(cviceni_plneni.add_worksheet(sheet_name, rows=1, cols=1), merged_df.reset_index())
        sheet_created = True  # If successful, mark as created
    except Exception as e:
        # If it fails (likely because the name exists), increment the suffix and try again
        n += 1
        print(f"Worksheet with name '{sheet_name}' already exists. Trying another name...")