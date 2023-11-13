with open("file1.txt") as file1:
    file1_list = file1.read()

with open("file2.txt") as file2:
    file2_list = file2.read()


file1_list = file1_list.split("\n")
file1_list = [int(number) for number in file1_list]

file2_list = file2_list.split("\n")
file2_list = [int(number) for number in file2_list]

print(file1_list)
print(file2_list)
print()

common_numbers = [number for number in file1_list if number in file2_list]

print(common_numbers)