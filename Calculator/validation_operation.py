def get_valid_number(prompt):
    """ფუნქცია რიცხვის ვალიდაციისთვის"""
    while True:
        user_input = input(prompt)
        try:
            # ტექსტი გარდაიქმნება რიცხვად (float)
            value = float(user_input)
            return value
        except ValueError:
            print("❌ არასწორი მონაცემი! გთხოვთ, შეიყვანოთ რიცხვი.")

def shekreba(x, y):
    return x + y

def gamokleba(x, y):
    return x - y

def gamravleba(x, y):
    return x * y

def gayofa(x, y):
    if y == 0:
        return "შეცდომა: ნულზე გაყოფა შეუძლებელია!"
    return round(x / y, 1)