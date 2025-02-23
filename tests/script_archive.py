import zipfile
import os
import pandas as pd

# Проверяем, существует ли директория tmp, и создаем её, если нет
if not os.path.exists("tmp"):
    os.makedirs("tmp")

with zipfile.ZipFile("tmp/archive.zip", 'w') as zip_file: # создаем архив
    zip_file.write("tmp", arcname='file_example_XLSX_50') # добавляем файл в архив
    zip_file.close() # закрываем архив

# Открываем архив
with zipfile.ZipFile("tmp/archive.zip", 'r') as zip_ref:
    # Получаем список файлов в архиве
    file_list = zip_ref.namelist()

    # Ищем файл с расширением .xlsx
    xlsx_file = next((f for f in file_list if f.endswith('.xlsx')), None)

    if xlsx_file:
        # Читаем содержимое файла из архива
        with zip_ref.open(xlsx_file) as file:
            # Используем pandas для чтения Excel-файла
            df = pd.read_excel(file)

            # Проверка содержимого (например, вывод первых строк)
            print(f"Содержимое файла {xlsx_file}:")
            print(df.head())
    else:
        print("В архиве нет файлов с расширением .xlsx.")