# -------------------------------------------
# 계산기 프로그램 ver2.0             제작자 : 
#
# 두 수를 입력받아 사칙연산(+, -, *, /)을
# 차례대로 출력하는 프로그램 입니다.
# -------------------------------------------

# 두 수를 입력 받는다.
firstNumber = input("첫 번째 수 : ")
operator = input("+, -, *, / 중 한 가지를 선택하세요 : ")
secondNumber = input("두 번째 수 : ")

# 두 수를 숫자 자료형으로 변환한다.
firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

#결과문 출력 
print()
print("-----------------------------------------")

# 두 수의 합을 출력한다.
if (operator == "+"):
    print("두 수의 합 : ", firstNumber + secondNumber)

# 두 수의 차을 출력한다.
if (operator == "-"):
    print("두 수의 차 : ", firstNumber - secondNumber)

# 두 수의 곱을 출력한다.
if (operator == "*"):
    print("두 수의 곱 : ", firstNumber * secondNumber)

# 두 수의 나눗셈을 출력한다.
if (operator == "/"):
    print("두 수의 나눗셈 : ", firstNumber / secondNumber)

print("------------------------------------------")
