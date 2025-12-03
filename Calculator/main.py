from validation_operation import get_valid_number, shekreba, gamokleba, gamravleba, gayofa, get_valid_operation

def kalkulatori():
    print('''   --- კალკულატორი ---
შეყვანილ ორ რიცხვზე ჩაატარებს ოპერაციებს!!''')
    
    while True:
        # 1. პირველი რიცხვის მიღება და ვალიდაცია
        num1 = get_valid_number("\nშეიყვანეთ პირველი რიცხვი: ")
        
        # 2. ოპერაციის არჩევა
        operacia = get_valid_operation("\nაირჩიეთ მოქმედება: +, -, *, / : ")

        # 3. მეორე რიცხვის მიღება და ვალიდაცია
        num2 = get_valid_number("\nშეიყვანეთ მეორე რიცხვი: ")

        # 4. გამოთვლა
        shedegi = None
        
        if operacia == '+':
            shedegi = shekreba(num1, num2)
        elif operacia == '-':
            shedegi = gamokleba(num1, num2)
        elif operacia == '*':
            shedegi = gamravleba(num1, num2)
        elif operacia == '/':
            shedegi = gayofa(num1, num2)
        else:
            continue # თავიდან იწყებს ციკლს

        # შედეგის გამოტანა
        print(f"✅ შედეგი: {num1} {operacia} {num2} = {shedegi}")

        # კითხვის დასმა, სურს თუ არა გაგრძელება
        next_calculation = input("\nგსურთ ახალი გამოთვლა? (y/n): ")
        if next_calculation.lower() != "y":
            print("კალკულატორი გამორთულია. ნახვამდის!")
            break
kalkulatori()