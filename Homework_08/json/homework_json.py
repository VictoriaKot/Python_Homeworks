import json
from pathlib import Path


def read_json(filepath: Path) -> dict:
    """
    Читає JSON файл та повертає його вміст як Python об'єкт.
    
    Args:
        filepath (Path): Шлях до JSON файла
        
    Returns:
        dict/list: Вміст JSON файла
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено
        json.JSONDecodeError: Якщо файл містить невалідний JSON
    """
    # with open(filepath, "r", encoding="utf-8") as file:
    #     content = json.load(file)
    #     return content


def write_json(filepath: Path, content:dict):
    """
    Записує Python об'єкт у JSON файл.
    
    Args:
        data (dict/list): Дані для запису
        filepath (Path): Шлях до файла для запису
        
    Returns:
        bool: True якщо успішно записано, False в іншому випадку
    """
    with open(filepath, "w", encoding="utf-8", ) as file:
        json.dump(content, file, indent=4)
        # Ваш код тут


# if __name__ == "__main__":
#     my_json = Path(__file__).parent / "test_result.json"
#     content = read_json(my_json)
#     print(content, type(content))
#     json_string = '{"name": "Ivan", "age": 25, "city": "Kyiv", "pass": 95, "skip": 5,  "failed": 0, "is_failed": true}'
#     json_to = json.loads(json_string)
#     print(json_to)
#     new_json = Path(__file__).parent / "new.json"
#     write_json(new_json, json_to)
    
json1 = Path(__file__).parent / "file_01.json"
json2 = Path(__file__).parent / "file_02.json"
json3 = Path(__file__).parent / "file_03.json"

try:
    with json1.open("r", encoding="utf-8") as f1:
        data1 = json.load(f1)
        print("JSON файл прочитано:")
        #print(data1)
except FileNotFoundError:
    print("Помилкаю Файл file_01.json не знайдено")
except json.JSONDecodeError:
    print("Неможлтво декодуати JSON файл file_01.json")
    data1 = None
    
try:
    with json2.open("r", encoding="utf-8") as f2:
        data2 = json.load(f2)
        print("JSON файл прочитано:")
        #print(data2)
except FileNotFoundError:
    print("Помилкаю Файл file_02.json не знайдено")
except json.JSONDecodeError:
    print("Неможлтво декодуати JSON файл file_02.json")
    data2 = None    

try:
    with json3.open("r", encoding="utf-8") as f3:
        data3 = json.load(f3)
        print("JSON файл прочитано:")
        #print(data3)
except FileNotFoundError:
    print("Помилкаю Файл file_03.json не знайдено")
except json.JSONDecodeError:
    print("Неможлтво декодуати JSON файл file_03.json")
    data3 = None 
"""Записати два валідні JSON файли в один новий"""
merged_data = [data1, data2]
new_json = Path(__file__).parent / "new.json"
with new_json.open("w", encoding="utf-8") as f_out:
    json.dump(merged_data, f_out, indent=4)