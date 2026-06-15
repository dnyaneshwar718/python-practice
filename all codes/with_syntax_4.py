#finding word in a text file
word="learning"
with open("muheheh.txt","r") as f :
    data=f.read()

    if word in data:
        print("word found")
    
    else:
        ("not founnd")
#muheheh.txt
#i love to study in python
#i want to master in python
#i am learning python