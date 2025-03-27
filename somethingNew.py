from telegram_bot.bot_tlg  import send_telegram_message

orderedNumber = int(input("Вибери значення більше 0:"))

while True:
    quessingNumber = int(input("Вгадай число тепер:"))

    if quessingNumber == orderedNumber:
        print("Вгадала, сучка")
        break
    if quessingNumber > orderedNumber:
        print("Багато, давай спочатку")
    else:
        print("Не, не в ту сторону вгадуєш")

secPart = input("Напиши що хочеш :")
if len(secPart) > 15:
    print("Багато хочеш")
else:
    print("обво'язково зроблю це")