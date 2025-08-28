import csv
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def write_csv(filepath: Path, content:list):
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file)
        writer.writerows(content)


#my_csv1 = Path(__file__).parent / "users_1.csv"
#content = read_file(my_csv1)
merged_dict = []
my_csv1 = Path(__file__).parent / "users_1.csv"
my_csv2 = Path(__file__).parent / "users_2.csv"

with open(my_csv1, "r", encoding="utf-8") as my_cvs1:
    reader = csv.DictReader(my_cvs1)
    for row in reader:
        merged_dict.append(row)

with open(my_csv2, "r", encoding="utf-8") as my_cvs2:
    reader = csv.DictReader(my_cvs2)
    for row in reader:
        merged_dict.append(row)

unique_rows_list = []
unique_rows_set = set()
    
for row in merged_dict:
    row_tuple = tuple(sorted(row.values()))
    if row_tuple not in unique_rows_set:
        unique_rows_set.add(row_tuple)
        unique_rows_list.append(row)
    
    if unique_rows_list:
        output_csv = Path(__file__).parent / "clean_users_3.csv"
        with open(output_csv, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=unique_rows_list[0].keys())
            writer.writeheader()
            writer.writerows(unique_rows_list)
            
  
    