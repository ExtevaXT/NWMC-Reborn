import os
import json

# Get the directory where the script is located
script_directory = os.path.dirname(__file__)

# Combine the script directory with the folder name
input_folder = os.path.join(script_directory, "item/naruto")
output_folder = os.path.join(script_directory, "json")

# Функция для создания .json файла на основе пути к иконке
def create_json(icon_path):
    icon_path = icon_path.replace('\\', '/')
    json_data = {
        "parent": "item/custom/icon",
        "textures": {
            "particle": icon_path,
            "texture": icon_path
        }
    }
    return json_data

# Базовая папка, в которой находятся файлы с иконками
base_folder = input_folder

# Папка, в которой будет создана структура
output_folder = output_folder

# Рекурсивная функция для создания структуры .json файлов
def create_json_structure(folder_path, output_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.png'):
                icon_path = os.path.join(root, file)
                relative_path = os.path.relpath(icon_path, folder_path)

                # Создаем .json файл в отдельной папке
                json_folder = os.path.join(output_path, os.path.dirname(relative_path))
                os.makedirs(json_folder, exist_ok=True)
                json_data = create_json("item/naruto/icons/" + os.path.splitext(relative_path)[0])

                # Создаем .json файл в соответствующей папке
                json_file_path = os.path.join(json_folder, file.replace('.png', '.json'))
                with open(json_file_path, 'w') as json_file:
                    json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    # Создаем выходную папку, если она не существует
    os.makedirs(output_folder, exist_ok=True)

    # Создаем структуру в выходной папке
    create_json_structure(base_folder, output_folder)