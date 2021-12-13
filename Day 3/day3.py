
###Part 1

f = open("input/input.txt", "r")

input_data = f.read()

f.close()

input_list = input_data.split('\n')

common_bits = []
lesser_bits = []

for i in range(0, len(input_list[0])):
    bit_list = [int(x[i]) for x in input_list]
    if sum(bit_list) > 0.5*len(bit_list):
        common_bits.append(1)
        lesser_bits.append(0)
    else:
        common_bits.append(0)
        lesser_bits.append(1)

def bin_to_dec(binary):
    return int(str(binary),2)

def rate(bit_list):
    return ''.join([str(x) for x in bit_list])

gamma_rate = rate(common_bits)

epsilon_rate = rate(lesser_bits)

print(int(gamma_rate,2) * int(epsilon_rate, 2))


    



