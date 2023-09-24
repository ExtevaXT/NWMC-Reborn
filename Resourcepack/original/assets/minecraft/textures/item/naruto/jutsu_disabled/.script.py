from PIL import Image, ImageFilter, ImageEnhance
import os

# Путь к папке с PNG-файлами
input_folder = os.path.dirname(__file__)

# Получаем список файлов в папке
files = os.listdir(input_folder)

# Фильтр, который вы хотите применить (например, GaussianBlur)
filter_type = ImageFilter.GaussianBlur(radius=5)

# Проходим по каждому файлу в папке
for file_name in files:
    if file_name.endswith(".png"):
        # Открываем изображение
        image = Image.open(os.path.join(input_folder, file_name))
        
        # Применяем фильтр
        image_filtered = image.filter(filter_type)
        
        # Darken the image
        enhancer = ImageEnhance.Brightness(image_filtered)
        image_filtered = enhancer.enhance(0.5)
        
        # Сохраняем измененное изображение
        output_file_name = f"{file_name}"
        image_filtered.save(os.path.join(input_folder, output_file_name))

        # Закрываем изображение
        image.close()
