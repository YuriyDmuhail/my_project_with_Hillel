orderedNumber = int(input("Вибери значення більше 0:"))

while True:
    quessingNumber = int(input("Вгадай число тепер, урод:"))

    if quessingNumber == orderedNumber:
        print("Вгадала, сучка")
        break
    if quessingNumber > orderedNumber:
        print("Дохуя, давай спочатку")
    else:
        print("Не, не в ту сторону вгадуєш")

secPart = input("Напиши що хочеш :")
if len(secPart) > 15:
    print("Дохуя хочеш")
else:
    print("обво'язково зроблю це, муділа")