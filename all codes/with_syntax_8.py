#from a file containing numbers seperated by comma,print the count of even number
with open("muheheh.txt","r") as f :
    data=f.read()
    count=0
    nums=data.split(",")
    print(nums)
    for val in nums:
        if int(val)%2==0:
            count+=1
        
print(count)
