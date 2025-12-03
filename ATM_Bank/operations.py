import os

FILE_NAME = "ATM_Bank/data.txt"

def load_users():
    #კითხულობს მომხმარებლის მონაცემებს ტექსტური ფაილიდან
    users = {}
    if not os.path.exists(FILE_NAME):
        # თუ ფაილი არ არსებობს, ვქმნით 3 მომხმარებლით
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            f.write("ლადო,1234,1000.0\n")
            f.write("გიორგი,0000,500.50\n")
            f.write("ნინო,1212,2200.0\n")
    # მონაცემების წაკითხვა უკვე არსებული ფაილიდან და ლექსიკონის ფორმატში დაბრუნება ფუნქციიდან
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                username, pin, balance = parts
                users[username] = {
                    "pin": pin,
                    "balance": float(balance)
                }
    return users

def save_users(users):
    #ინახავს განახლებულ მონაცემებს ფაილში
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for username, data in users.items():
            line = f"{username},{data['pin']},{data['balance']}\n"
            f.write(line)

def check_balance(users, username):
    #ბალანსის შემოწმება
    balance = users[username]['balance']
    print(f"\n--- თქვენი ბალანსია: {balance:.2f} GEL ---")

def deposit(users, username):
    #თანხის შეტანა
    try:
        amount = float(input("შეიყვანეთ შესატანი თანხა: "))
        if amount > 0:
            users[username]['balance'] += amount
            save_users(users)
            print(f"✅ ოპერაცია წარმატებულია. ახალი ბალანსი: {users[username]['balance']:.2f} GEL")
        else:
            print("❌ თანხა უნდა იყოს დადებითი რიცხვი.")
    except ValueError:
        print("❌ გთხოვთ, შეიყვანოთ რიცხვი.")

def withdraw(users, username):
    #თანხის გატანა
    try:
        amount = float(input("შეიყვანეთ გასატანი თანხა: "))
        if amount > 0:
            if amount <= users[username]['balance']:
                users[username]['balance'] -= amount
                save_users(users)
                print(f"✅ ოპერაცია წარმატებულია. დარჩენილი ბალანსი: {users[username]['balance']:.2f} GEL")
            else:
                print("❌ შეცდომა: ანგარიშზე არ არის საკმარისი თანხა.")
        else:
            print("❌ თანხა უნდა იყოს დადებითი რიცხვი.")
    except ValueError:
        print("❌ გთხოვთ, შეიყვანოთ რიცხვი.")

