with open("muheheh.txt","r") as f:
    data=f.read()
    print(data)

new_data=data.replace("java","python")
print(new_data)

with open("muheheh.txt", "w") as f:
    f.write(new_data)