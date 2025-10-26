f = open('bar.txt', 'r')
f = open('bar.txt', 'w')
f.write("Hello, this is some text inside bar.txt!\n")
j=input("get data")
f.write(j)

line=f.read()
f.close()