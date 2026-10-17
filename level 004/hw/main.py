# დავალება 1
width =int(input("width:"))
length =int(input("length:"))
print("ფართობი:",width * length)

# დავალება 2
number =int(input("number:"))
print(number % 2)
if number == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")

# დავალება3

age = 23
if age >= 18:
    print("მოგესალმებით, თქვენ სრულწლოვანი ხართ!")
else:
    print("შესვლა შეზღუდულია!")

# დავალება 4
temperature =int(input("temperature:"))
if temperature < 0:
    print("გარეთ ყინავს, ჩაიცვი თბილად!")
elif temperature >= 0 and temperature <= 20:
    print("გარეთ ნორმალური ამინდია")
else:
    print("ძალიან ცხელა!")

# დავალება 5

balance = 500
withdraw_amaount =int(input("withdraw_amaount:"))
if balance <= 500:
     print("balance=",balance - withdraw_amaount)

# დავალება 6
total_price = int(input("total_price:"))
if total_price >= 100:
    print("20%-იანი ფასდაკლება")
    print(total_price % 20)
elif total_price >= 50:
    print("10%-იანი ფასდაკლება")
    print(total_price % 10)
else:
    print(total_price)
# დავალება 7

correct_password = "python123"
user_password =int(input("user password:"))
if user_password == correct_password:
    print("წვდომა დაშვებულია!")
else:
    print("არასწორი პაროლი!")
# დავალება 8
score =int(input("score:"))
if score >= 91 and score <= 100:
    print("A")
elif score >= 81 and score <= 90:
    print("B")
elif score >= 71 and score <= 80:
    print("C")
elif score >= 60 and score <= 70:
    print("D")
elif score >= 51 and score <= 60:
    print("E")
else:
    print("F")
# დავალება 9
total_seconds =int(input("total seconds:"))
print(total_seconds // 60)
print(total_seconds % 60)
if total_seconds >60:
    print("ეს უკვე ერთ საათზე მეტია!")
# დავალება 10
item_name =int(input("item name:"))
price =int(input("price:"))
quanity =int(input("quanity:"))
total_price =(price * quanity)
if total_price >= 50:
    print("has_discount = True")
print("------ქვითარი------")
print("item_name:", item_name)
print("price:", price)
print("quanity:", quanity)
print("total_price:", total_price)
print("-------------------")
# BOSS LEVEL FOR 1 WEEK
# 1
print("  ", "*" * 1)
print(" ", "*" * 3)
print("", "*" * 5)
print(" ", "*" * 3)
print("  ", "*" * 1)
# 2
secret_number = 67
number =int(input("გამოიცანი რიცხვი:"))
if number > secret_number:
    print("შენი რიცხვი მეტია")
elif number < secret_number:
    print("შენი რიცხვი ნაკლებია!")
else:
    print("სწორია! გამოიცანი!")