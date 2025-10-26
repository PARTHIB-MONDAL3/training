f = open("C:\\Users\\parth\\OneDrive\\Desktop\\customers-100.csv", 'r')
header=f.readline()
count = 0

line = f.readline()
while line != '':
    count += 1
    line=f.readline()
f.close()

print("Number of customers:", count)
