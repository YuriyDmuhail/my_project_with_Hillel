from telegram_bot.bot_tlg  import send_telegram_message

import re
valid_codes = {"050", "066", "067", "068", "073", "093", "095", "096", "097", "098", "099"}

while True:
    given_number_in_string = input("Введіть номер телефону:")
    cleared_given_number = re.sub(r'\D', '', given_number_in_string)

    if  len(cleared_given_number) == 10:
       if cleared_given_number[0:3] in valid_codes:
           print("можливо правильний номер, не дописав валідації ще")
           break
       else:
           print("Невалідний номер.")

    elif len(cleared_given_number) == 12 and cleared_given_number.startswith("380"):
        if cleared_given_number[2:5] in valid_codes:
            print("можливо правильний номер, не дописав валідації ще")
            break
        else:
           print("Невалідний номер, введи ще раз:")
    else:
        send_telegram_message("Неправильно спробуй ще раз")

