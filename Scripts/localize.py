import ruamel.yaml
import json
from googletrans import Translator

path ='../spells/basic/wind.yml'

yaml = ruamel.yaml.YAML()
translator = Translator()

# Load the YAML data from the 'wind.yml' file
with open(path, 'r', encoding='utf-8') as yaml_file:
    data = yaml.load(yaml_file)

# Add the 'wind' section at the beginning of the YAML data
wind_data = {
    'wind': {
        'category': 'basic',
        'earns_sp': 0,
        'upgrade_required_path': 'student',
        'upgrade_required_casts': 50
    }
}
# Sort the spells by their 'worth' property
sorted_spells = sorted(data.values(), key=lambda x: x.get('worth', 0))

# Create a list to store the JSON data
json_data = []

# Iterate through the sorted spells and create JSON entries
for index, spell_data in enumerate(sorted_spells, start=1):
    en_name = f"magic.spells.basic.wind{index}.name"
    en_description = f"magic.spells.basic.wind{index}.description"
    ru_name = spell_data['name']
    ru_description = spell_data['description']
    
    # Update the YAML data with '[lang]' placeholders
    spell_data['name'] = f"[lang]magic.spells.basic.wind{index}.name[/lang]"
    spell_data['description'] = f"[lang]magic.spells.basic.wind{index}.description[/lang]"
    spell_data['alias'] = f"wind{index}"
    spell_data['inherit'] = f"wind"

    # Remove unnecessary
    spell_data.pop('icon_url')
    spell_data.pop('upgrade_required_path')
    spell_data.pop('upgrade_required_casts')
    spell_data.pop('category')
    spell_data.pop('earns_sp')

    # Move to beginning
    spell_data.move_to_end('inherit', last=False)
    spell_data.move_to_end('alias', last=False)
    spell_data.move_to_end('description', last=False)
    spell_data.move_to_end('name', last=False)

    # Create JSON entries
    #json_entry_name = {
    #    "type": "text",
    #    "key": en_name,
    #    "languages": {
    #        "en_GB": translator.translate(ru_name, dest='en').text,
    #        "ru_RU": ru_name
    #    }
    #}

    #json_entry_description = {
    #    "type": "text",
    #    "key": en_description,
    #    "languages": {
    #        "en_GB": translator.translate(ru_description, dest='en').text,
    #        "ru_RU": ru_description
    #    }
    #}

    #json_data.extend([json_entry_name, json_entry_description])

data.update(wind_data)
data.move_to_end('wind', last=False)
# Write the JSON data to 'wind.json'
#with open('wind.json', 'w', encoding='utf-8') as json_file:
#    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

# Write the updated YAML data back to 'wind.yml'
with open('basic/wind.yml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(data, yaml_file)
