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

def get_valid_operation(operation):
    """ფუნქცია ოპერაციის ვალიდაციისთვის"""
    while True:
        user_input = input(operation)
        # შემოწმება არის თუ არა ოპერაცია ვალიდური
        try:
            if user_input in "+-*/":
                return user_input
            else:
                #არასწორი ოპერაციის შეყვანის შემთხვევაში აბრუნებს შეცდომას
                raise ValueError
        except ValueError:
            print("❌ არასწორი ოპერაცია! გთხოვთ აირჩიოთ: +, -, *, ან /")

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