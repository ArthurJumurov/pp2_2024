import re
file_name = "row.txt"
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        if re.search(r'ab{2,3}', line):
            print(line.strip())
