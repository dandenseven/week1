#file_object = open('text.txt', 'r')
#never use this again#

with open('test.txt', "r") as file_object:
    for line in file_object:
        print(line.split())
print('\n\n\nn\n\n\n')

with open('test.txt', 'r') as file_object:
    line = file_object.readline()
    print(line)
    line2 = file_object.readline()
    print(line2)
with open('test.txt' as file_obejct:)
    whole_text = file_object.read()
    print(whole_text) 

with open('file_open_with.py') as file_object:
    for line in file_object:
        print(line, end='')
