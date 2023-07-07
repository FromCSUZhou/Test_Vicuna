import json
import os

file_name_pattern = "output_{}.json"
num_files = 8

merged_data = []
identity_counter = 0

for i in range(1, num_files + 1):
    file_name = file_name_pattern.format(i)
    with open(file_name, 'r') as file:
        data = json.load(file)
        for item in data:
            item["id"] = f"identity_{identity_counter}"
            identity_counter += 1
        merged_data.extend(data)

with open('output_merged.json', 'w') as file:
    json.dump(merged_data, file, indent=4)
