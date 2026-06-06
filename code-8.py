#function for identifying even number or odd number
num=int(input("Enter your num :"))
def identifier(num):
    if num%2==0:
        print("even number")
    else:
        print("Odd number")

identifier(num)
