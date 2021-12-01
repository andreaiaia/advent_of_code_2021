with open("input-1.txt", 'r') as my_file:
    file_array = [word.strip() for word in my_file]
my_file.close()
print(file_array)
increased = 0

for i, j in enumerate(file_array[:-1]):
    if file_array[i+1] > j:
        increased += 1
    
print(increased)