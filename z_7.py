input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
if a > b and a > c:
    output_data = open('output.txt', 'w')
    output_data.write(str(a))
elif b > c and b > a:
    output_data = open('output.txt', 'w')
    output_data.write(str(b))
else:
    output_data = open('output.txt', 'w')
    output_data.write(str(c))
input_data.close()
output_data.close()