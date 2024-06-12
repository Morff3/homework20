from pprint import pprint

file_name = "text.txt"
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
file.close()
print(file_content)


file_name = "text.txt"
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
print(file_content)
