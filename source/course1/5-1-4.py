# 5-1-4 : 반복문과 조건문

sum = 0

while True:
    print("숫자를 입력해 주세요")
    print(" x : 종료하기")
    print(" p : 출력하기")
    inputData = input("> ")
    
    if inputData == "x":
        break
    if inputData == "p":
        print("지금까지 더한 숫자는 : ", sum, "입니다")
        print()
    else:
        sum = sum + int(inputData)   # 숫자 더하기
        print()

