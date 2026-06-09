#calculating sum using recursion function
def cal_sum(n):
    if n==0:
        return 0
    else:
        return n+cal_sum(n-1)

print(cal_sum(5))