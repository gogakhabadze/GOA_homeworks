# მომხმარებლისგან მოითხოვს ოჯახის წევრების ასაკს
mama = int(input("შეიყვანე მამის ასაკი: "))
deda = int(input("შეიყვანე დედის ასაკი: "))
dzma = int(input("შეიყვანე ძმის ასაკი: "))
me = int(input("შეიყვანე შენი ასაკი: "))
da = int(input("შეიყვანე დის ასაკი: ")) 

# 25 წლის შემდეგ ასაკის გამოთვლა
mama_future = mama + 25
deda_future = deda + 25
dzma_future = dzma + 25
me_future = me + 25
da_future = da + 25
# შედეგის დაბეჭდვა
print("25 წლის შემდეგ:")
print("მამა იქნება", mama_future, "წლის")
print("დედა იქნება", deda_future, "წლის")
print("ძმა იქნება", dzma_future, "წლის")
print("შენ იქნები", me_future, "წლის")
print("და იქნება", da_future, "წლის")
