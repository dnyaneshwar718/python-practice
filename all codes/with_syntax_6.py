#funtion for finding word in a line
def check_for_line(word):
    data=True
    line_no=1
    with open("muheheh.txt","r") as f:
         while data:
              data=f.readline()
              if word in data :
                   print(line_no)
                   return
              line_no +=1
        
    return -2
print(check_for_line("learn"))