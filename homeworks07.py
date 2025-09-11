"""
### Робота з файлами та папками — завдання

1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here
from pathlib import Path
filepath = Path(__file__)
file_dir = filepath.parent / "hello.txt"
with file_dir.open( "w", encoding='utf-8') as file:
   file.write("Hello, Python!\n")
   
"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
with file_dir.open("r", encoding="utf-8") as file:
   content = file.read()
   print(content)
"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
with file_dir.open("a", encoding="utf-8") as file: 
   content = file.write("Learning file operations.\n")
"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with file_dir.open( "r", encoding="utf-8") as file:
   for line in file:
      print(line.strip()) 
"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
with file_dir.open("r",encoding="utf-8") as file:
   content = file.read()
   print(f"У файлі 'hello.txt': {len(content)} символів")
   
      
"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
new_directory = file_dir.parent / "data" 
new_directory.mkdir(parents=True, exist_ok=True)
notes_path = new_directory / "notes.txt"
with notes_path.open("w", encoding="utf-8") as f:
    f.write("My first note.\n")
   
"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
files = [f for f in new_directory.iterdir()]
print(files)
print(f"Is file '{files[0].name}'  exist? {files[0].exists()}")
"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
with notes_path.open("r", encoding="utf-8") as file_read:
   content = file_read.read()
copy_path = new_directory / "copy.txt"
with copy_path.open("w", encoding="utf-8") as file_write:
   file_write.write(content)
   

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
a_path = new_directory.parent / "a.txt"
b_path = new_directory.parent / "b.txt"
with a_path.open("w", encoding="utf-8") as f_a:
   f_a.write("Текст для першого файлу А\n")
with b_path.open("w", encoding="utf-8") as f_b:
   f_b.write("Текст для другого файлу В\n")
with a_path.open("r", encoding="utf-8") as f_a, \
     b_path.open("r", encoding="utf-8") as f_b, \
     (new_directory.parent / "ab.txt").open("w", encoding="utf-8") as f_ab:
   f_ab.write(f_a.read())
   f_ab.write(f_b.read())

"""
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
with notes_path.open("r", encoding="utf-8") as f:
   content = f.read()
search_word = 'note'
if search_word in content:
   print(f"Слово '{search_word}' знайдено")
else:
   print(f"Слово '{search_word}' не знайдено")


