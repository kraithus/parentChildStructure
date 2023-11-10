import json

# Open the input file for reading
with open('projects_list.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Initialize an empty dictionary to store the restructured data
result = {}

# Iterate over each entry in the original data
for entry in data:
    # Extract relevant information from the entry
    category = entry['Category']
    region = entry['Region']
    council = entry['Council']
    project = entry['Project']

    # Check if the category is already in the result dictionary
    if category not in result:
        result[category] = {}

    # Check if the region is already in the category dictionary
    if region not in result[category]:
        result[category][region] = {}

    # Check if the council is already in the region dictionary
    if council not in result[category][region]:
        result[category][region][council] = []

    # Append the project to the list under the council
    result[category][region][council].append(project)

# Open the output file for writing
with open('projects_list_formatted.json', 'w') as file:
    # Write the restructured data to the output file with indentation for better readability
    json.dump(result, file, indent=2)
