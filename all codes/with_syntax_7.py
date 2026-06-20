#from a file containing numbers seperated by comma,print the numbers 
with open ("muheheh.txt","r") as f :
    data=f.read()

    num=""
    for i in range (len(data)):
        if (data[i]==","):
            print(num)
            num=""
        else:
            num+=data[i]