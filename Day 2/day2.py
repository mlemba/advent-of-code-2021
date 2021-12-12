
###Part 1

f = open("input/input.txt", "r")

input_data = f.read()

f.close()

input_list = input_data.split('\n')    

location = {'horizontal': 0, 'depth': 0}

for i in input_list:
    direction = i.split()[0]
    magnitude = int(i.split()[1])
    if direction == 'up':
        location['depth'] -= magnitude
    if direction == 'down':
        location['depth'] += magnitude
    if direction == 'forward':
        location['horizontal'] += magnitude

print(location, location['horizontal']*location['depth'])

####Part 2

location = {'horizontal': 0, 'aim': 0, 'depth': 0}

for i in input_list:
    direction = i.split()[0]
    magnitude = int(i.split()[1])
    if direction == 'up':
        location['aim'] -= magnitude
    if direction == 'down':
        location['aim'] += magnitude
    if direction == 'forward':
        location['horizontal'] += magnitude
        location['depth'] += magnitude*location['aim']

print(location, location['horizontal']*location['depth'])

