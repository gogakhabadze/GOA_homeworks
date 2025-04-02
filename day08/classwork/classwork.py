# num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
# num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

# print("მიმატება:", num1 + num2)
# print("გამოკლება:", num1 - num2)
# print("გამრავლება:", num1 * num2)


# print("გაყოფა:", num1 / num2)
# print("ნაშთიანი გაყოფა:", num1 % num2)

# print("ხარისხში აყვანა:", num1 ** num2)


# კონკატინაცია ნიშნავს ორი ან მეტი სტრიქონის ერთმანეთთან მიერთებას
# მაგალითად, "Hello" + " World" გამოიტანს "Hello World"

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

print("მიმატება:" + str(num1 + num2))  # აქ ხდება სტრიქონის და რიცხვის კონკატინაცია (შერწყმა)
print("გამოკლება:" + str(num1 - num2))
print("გამრავლება:" + str(num1 * num2))

if num2 != 0:
    print("გაყოფა:" + str(num1 / num2))
    print("ნაშთიანი გაყოფა:" + str(num1 % num2))

print("ხარისხში აყვანა:" + str(num1 ** num2))
