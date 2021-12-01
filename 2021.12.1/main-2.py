with open("input-1.txt", 'r') as my_file:
    file_array = [int(word.strip()) for word in my_file]
my_file.close()

increased = 0

for i in range(len(file_array)-4):
    first = file_array[i] + file_array[i+1] + file_array[i+2]
    second = file_array[i+1] + file_array[i+2] + file_array[i+3]
    if second > first:
        increased += 1

print(increased)
