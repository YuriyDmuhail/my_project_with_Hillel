import re
while True:
    given_number_in_string = input("Введіть номер телефону: +38")
    cleared_given_number = re.sub(r'\D', '', given_number_in_string)
    if  len(cleared_given_number) == 10 or len(cleared_given_number) == 12:
        print("можливо правильний номер, не дописав валідації ще")
        break
    else:
        print("неправильний номер, спробуй ще раз ввести : ")
