# 4-2-3 : if, else문 2

a = input("1~5사이 숫자 입력 : ")
a = int(a)

if(a == 5):
    b = "최우수"
if(a == 4):
    b = "우수"
if(a == 3):
    b = "보통"
if(a == 2):
    b = "부족"
if(a == 1):
    b = "미흡"
    
print(b)