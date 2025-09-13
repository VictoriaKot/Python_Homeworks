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
    with open(filepath, "r", encoding="utf-8") as file:
        try:
            content = json.load(file)
            print("Json file is read")
            return content
        except json.decoder.JSONDecodeError:
            print("Read JSON has failed")
            content = None
            
   


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
        return content
        


if __name__ == "__main__":
    my_json1 = Path(__file__).parent / "file_01.json"
    content1 = read_json(my_json1)
    my_json2 = Path(__file__).parent / "file_02.json"
    content2 = read_json(my_json2)
    my_json3 = Path(__file__).parent / "file_03.json"
    content3 = read_json(my_json3)
    
    write_json(Path(__file__).parent / "new.json", content1)