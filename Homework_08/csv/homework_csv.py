import csv
from pathlib import Path



def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
        return rows

def write_csv(filepath: Path, content: list):
    if not content:
        return 
    
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        
        # If content is a list of dicts, handle as before; if list of lists, write directly
        if isinstance(content[0], dict):
            headers = list(content[0])
            writer.writerow(headers)
            for row_dict in content:
                row = [row_dict.get(header, "") for header in headers]
                writer.writerow(row)
        else:
            for row in content:
                writer.writerow(row)


if __name__ == "__main__":
    my_csv = Path(__file__).parent / "users_1.csv"
    content1 = read_file(my_csv)
    #print(content1)
    my_csv_2 = Path(__file__).parent / "users_2.csv"
    content2 = read_file(my_csv_2)
#Обєднати 2 списки і прибрати дуплікати  
merged_list = []  
merged_list.extend(content1)
merged_list.extend(content2)

no_duplic_list = []
for sublist in merged_list:
    if sublist not in no_duplic_list:
        no_duplic_list.append(sublist)
print(no_duplic_list)
clean_users = write_csv(Path(__file__).parent / "users_3.csv", no_duplic_list )
