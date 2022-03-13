def mult3(n):
    strNum = str(n)
    print(f"Size of number= {len(strNum)}")
    sum = 0
    for i in range(0, len(strNum)):
        print(f"Digit= {int(strNum[i])}")
        sum += int(strNum[i])
    print(sum)
    if sum % 3 == 0:
        print(f"{n} is a multiple of 3")
    else:
        print(f"{n} is not a multiple of 3")


def mult5(n):
    pass


number = int(input("Enter the number: "))
mult3(number)
mult5(number)
