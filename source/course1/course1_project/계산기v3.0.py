# -------------------------------------------
# 계산기 프로그램 ver3.0          제작자 :
#
# 두 수와 사칙연산자 중 하나를 입력받아
# 입력받은 사칙연산(+, -, *, /)을 수행하고
# 그 결과를 출력하는 프로그램 입니다.
# -------------------------------------------

while True:
    # [입력]
    # 종료여부, 개산하려는 두 수, 연산자를 입력받는다.
    close = input("종료 = x, 시작 = 아무 키나 누르세요 : ")
    if close == "x":
        break
    firstNumber = input("첫 번째 수 : ")
    operator = input("+, -, *, / 중 한 가지를 선택하세요 : ")
    secondNumber = input("두 번째 수 : ")

    # 두 수를 숫자 자료형으로 변환한다.
    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)

    # [처리]
    # 두 수의 합을 계산한다.
    if (operator == "+"):
        result = "두 수의 합 : {}".format(firstNumber + secondNumber)
    # 두 수의 차를 계산한다.
    if (operator == "-"):
        result = "두 수의 차 : {}".format(firstNumber - secondNumber)
    # 두 수의 곱을 계산한다.
    if (operator == "*"):
        result = "두 수의 곱 : {}".format(firstNumber * secondNumber)
    # 두 수의 나눗셈을 계산한다.
    if (operator == "/"):
        result = "두 수의 나눗셈 : {}".format(firstNumber / secondNumber)

    # [출력]
    print()
    print("-----------------------------------------")
    print(result)
    print("------------------------------------------")

