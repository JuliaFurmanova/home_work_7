import zipfile
import os

# Проверяем, существует ли директория tmp, и создаем её, если нет
if not os.path.exists("tmp"):
    os.makedirs("tmp")

with zipfile.ZipFile("tmp/archive.zip", 'w') as zip_file: # создаем архив
    zip_file.write("tmp", arcname='file_example_XLSX_50') # добавляем файл в архив
    zip_file.close() # закрываем архив
