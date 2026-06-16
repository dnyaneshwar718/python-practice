#checking the word in file using text
def check_for_word(word):
    with open("muheheh.txt","r") as f :
     data=f.read()

    if data.find(word) != -1:
        print("word found")
    
    else:
        ("not founnd")

check_for_word("learning")