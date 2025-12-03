from main_oparations import StudentManager

manager = StudentManager()

while True:
        
        choice = input('''===== სტუდენტების მართვის სისტემა =====")
                       
        1. ახალი სტუდენტის დამატება
        2. ყველა სტუდენტის ნახვა
        3. სტუდენტის ძებნა ნომრის მიხედვით
        4. სტუდენტის შეფასების განახლება
        5. გასვლა
                                    
        აირჩიეთ მოქმედება (1-5): ''')

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_all_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.update_student_grade()
        elif choice == '5':
            print("პროგრამა დასრულებულია!")
            break
        else:
            print("❌ არასწორი არჩევანი. გთხოვთ სცადოთ თავიდან.")