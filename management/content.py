import os
import json

# Path to the scripts directory
scripts_dir = "/home/jupyter-vojta/notebooks/pribehy-dat/scripts"

# Output file
output_file = "/home/jupyter-vojta/notebooks/pribehy-dat/management/notebook_content.txt"

def extract_notebook_content(notebook_path):
    """Extract markdown and code cell content from a Jupyter notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    content = []
    for cell in nb.get('cells', []):
        cell_type = cell.get('cell_type')
        source = cell.get('source', [])
        
        # Join the source lines
        text = ''.join(source) if isinstance(source, list) else source
        
        if text.strip():  # Only add non-empty cells
            if cell_type == 'markdown':
                content.append(f"[MARKDOWN]\n{text}")
            elif cell_type == 'code':
                content.append(f"[CODE]\n{text}")
    
    return '\n\n'.join(content)

def main():
    output_lines = []
    
    # Get all .ipynb files in the scripts directory (excluding subdirectories)
    ipynb_files = [f for f in os.listdir(scripts_dir) if f.endswith('.ipynb')]
    ipynb_files.sort()
    
    for filename in ipynb_files:
        filepath = os.path.join(scripts_dir, filename)
        output_lines.append(f"\n{'='*60}")
        output_lines.append(f"FILE: {filename}")
        output_lines.append(f"{'='*60}\n")
        
        try:
            content = extract_notebook_content(filepath)
            output_lines.append(content)
        except Exception as e:
            output_lines.append(f"Error reading notebook: {e}")
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"Content saved to {output_file}")
    print(f"Processed {len(ipynb_files)} notebooks")

if __name__ == "__main__":
    main()
