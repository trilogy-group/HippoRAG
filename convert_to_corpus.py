import os
import json

def convert_json_files():
    prefix = "screenshot-data-dump/4172"
    candidate_id = "20104"
    date_str = "2024-06-04"
    source_dir = os.path.join(prefix, candidate_id, date_str)
    target_dir = "data/"
    os.makedirs(target_dir, exist_ok=True)

    transformed_data = []
    for filename in os.listdir(source_dir):
        if filename.endswith(".json"):
            with open(os.path.join(source_dir, filename), 'r') as source_file:
                data = json.load(source_file)
                transformed_data.append({
                    "title": filename,
                    "text": json.dumps(data)
                })
    
    with open(os.path.join(target_dir, f'worksmart_{candidate_id}_{date_str}_corpus.json'), 'w') as target_file:
        json.dump(transformed_data, target_file, indent=4)

convert_json_files()
