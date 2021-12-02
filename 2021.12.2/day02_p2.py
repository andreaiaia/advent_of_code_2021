with open("input.txt", "r") as my_file:
    my_input = [word.strip() for word in my_file]

f_pos = 0
d_pos = 0
aim = 0

for item in my_input:
    if item[:-2] == "forward":
        f_pos = f_pos + int(item[-1])
        d_pos = d_pos + aim * int(item[-1])
    elif item[:-2] == "down":
        aim = aim + int(item[-1])
    else:
        aim = aim - int(item[-1])

print("----- Second part -----")
print("Forward: ", f_pos)
print("Depth: ", d_pos)
print("Anwser: ", f_pos * d_pos)


