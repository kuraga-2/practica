input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
if c == a *b:
    output_data = open('output.txt', 'w')
    output_data.write(str("YES"))
else:
    output_data = open('output.txt', 'w')
    output_data.write(str("NO"))
input_data.close()
output_data.close()