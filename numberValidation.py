import re
valid_codes = {"050", "066", "067", "068", "073", "093", "095", "096", "097", "098", "099"}

while True:
    given_number_in_string = input("Введіть номер телефону:")
    cleared_given_number = re.sub(r'\D', '', given_number_in_string)

    if  len(cleared_given_number) == 10:
       if cleared_given_number[0:3] in valid_codes:
           print("можливо правильний номер, не дописав валідації ще")
       else:
           print("Невалідний номер, введи ще раз:")
           break

    elif len(cleared_given_number) == 12 and cleared_given_number.startswith("380"):
        if cleared_given_number in valid_codes:
            print("можливо правильний номер")
        else:
           print("Невалідний номер, введи ще раз:")
           break
    else:
        print("Невалідний номер, введи ще раз:")

