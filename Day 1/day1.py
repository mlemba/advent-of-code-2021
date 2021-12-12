###Advent of Code, Day 1 exercise
#Part 1

f = open("input/input.txt", "r")

input_data = f.read()

f.close()

input_list = list(map(int, input_data.split('\n')))       #convert strings to integers


increases = 0

for i in range(1, len(input_list)):
    if input_list[i] > input_list[i-1]:
        increases += 1
    
print(increases)

#Part 2

window_increases = 0

old_window = sum(input_list[0:3])

for i in range(1, (len(input_list)-2)):
    new_window = sum(input_list[i:i+3]) 
    if new_window > old_window:
        window_increases += 1
    old_window = new_window

print(window_increases)




