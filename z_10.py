input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
for i in range(-100,101):
    if a*(i^3) + b*(i^2) + c*i + d == 0:
      break
    output_data = open('output.txt', 'w')
    output_data.write(str(i))
input_data.close()
output_data.close()