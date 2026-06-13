#reading the file and overwriting it 
with open("muheheh.txt","r") as f:
    data=f.read()
    print(data)

with open("muheheh.txt","w")as f:
    data2=f.write("loki is god")

with open("muheheh.txt","r")as f:
    data3=f.read()
    print(data3)