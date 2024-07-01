import os
import json

def convert_json_to_txt(src_folder, dst_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    
    # Iterate through all files in the source folder
    for filename in os.listdir(src_folder):
        if filename.endswith('.json'):
            # Construct full file path
            file_path = os.path.join(src_folder, filename)
            
            # Open and read the JSON file
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            
            # Convert JSON object to string
            data_str = json.dumps(data, indent=4)
            
            # Create the destination file path with .txt extension
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_file_path = os.path.join(dst_folder, txt_filename)
            
            # Write the string data to the text file
            with open(txt_file_path, 'w') as txt_file:
                txt_file.write(data_str)
            
            print(f"Converted {filename} to {txt_filename}")

# Define the source and destination folders
src_folder = 'screenshot-data-dump/4895/1193118-George Dita/2024-06-06'
dst_folder = src_folder+'-txt'

# Run the conversion function
convert_json_to_txt(src_folder, dst_folder)
