input_data = open('input.txt', 'r')
data = input_data.read()
a = int(data)
k = 0 
if a > 0:
     for i in range(1,a+1):
          k+=i
elif a < 0:
     for i in range(a,2):
          k+=i
else:
     k=1   
k=str(k)             
output_data = open('output.txt', 'w')
output_data.write(k)
input_data.close()
output_data.close()