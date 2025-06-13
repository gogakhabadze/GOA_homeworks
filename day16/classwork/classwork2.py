
original_pincodi = "1234"

user_pin = input("შეიყვანე პინ კოდი: ")


while user_pin != original_pincodi:
    print("არასწორია! სცადე თავიდან.")
    user_pin = input("შეიყვანე პინ კოდი: ")

print("წარმატებით შედით სისტემაში!")
