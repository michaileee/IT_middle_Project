import json 
import os   

# ფაილის სახელი
DATA_FILE = "student_manegement_system/students.json"

# 1. სტუდენტის კლასი
class Student:
    def __init__(self, name, roll_number, grade):
        self.__name = name
        self.__roll_number = roll_number
        self.__grade = grade

    #Getters (გეტერ მეთოდი ატრიბუტების წასაკითხად)
    @property
    def name(self):
        return self.__name

    @property
    def roll_number(self):
        return self.__roll_number

    @property
    def grade(self):
        return self.__grade

    #Setter (სეტერ მეთოდი შეფასების შესცვლელად)
    @grade.setter
    def grade(self, new_grade):
        if len(new_grade) == 1 and new_grade.isalnum():
            self.__grade = new_grade.upper()
        else:
            print("❌ შეცდომა: შეფასება უნდა იყოს ერთი სიმბოლო.")

    # ობიექტის გადაქცევა ლექსიკონად და (Dict) შესანახად
    def to_dict(self):
        return {
            "name": self.__name,
            "roll_number": self.__roll_number,
            "grade": self.__grade
        }

    def __str__(self):
        return f"----------------------------\nსახელი: {self.__name}\nსიის ნომერი: {self.__roll_number}\nშეფასება: {self.__grade}\n----------------------------"


# 2. კლასი StudentManager
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data() # პროგრამის ჩართვისას მონაცემების წაკითხვა

    # --- ფაილთან მუშაობის ფუნქციები ---
    
    def save_data(self):
        #ინახავს სტუდენტების სიას JSON ფაილში
        # გარდაქმნის სტუდენტების ობიექტებს ლექსიკონების სიად
        data_to_save = [student.to_dict() for student in self.students]
        
        try:
            with open(DATA_FILE, 'w', encoding='utf-8') as file:
                json.dump(data_to_save, file, indent=2, ensure_ascii=False) 
        except Exception as e:
            print(f"❌ ვერ მოხერხდა ფაილის შენახვა: {e}")

    def load_data(self):
        #კითხულობს მონაცემებს JSON ფაილიდან
        if not os.path.exists(DATA_FILE):
            return # თუ ფაილი არ არსებობს, არაფერს ვაბრუნებთ

        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                data_list = json.load(file)
                
                # ლექსიკონებიდან ისევ ობიექტების შექმნა
                for item in data_list:
                    student = Student(item['name'], item['roll_number'], item['grade'])
                    self.students.append(student)
            print(f"📂 ჩაიტვირთა {len(self.students)} სტუდენტი ფაილიდან.\n")
        except Exception as e:
            print(f"❌ ვერ მოხერხდა ფაილის წაკითხვა: {e}")

    # --- ძირითადი ფუნქციონალი ---

    def add_student(self):
        #--- ახალი სტუდენტის დამატება ---
        name = input("შეიყვანეთ სახელი: ").strip()
        
        while True:
            try:
                roll_input = input("შეიყვანეთ სიის ნომერი (რიცხვი): ")
                roll_number = int(roll_input)
                if self.find_student_by_roll(roll_number):
                    print("❌ შეცდომა: სტუდენტი ამ ნომრით უკვე არსებობს.")
                    continue
                break
            except ValueError:
                print("❌ შეცდომა: გთხოვთ შეიყვანოთ მთელი რიცხვი.")

        while True:
            grade = input("შეიყვანეთ შეფასება (მაგ: A, B, C): ").strip().upper()
            if len(grade) == 1:
                break
            print("❌ შეცდომა: შეფასება უნდა იყოს ერთი სიმბოლო.")

        new_student = Student(name, roll_number, grade)
        self.students.append(new_student)
        self.save_data() # შენახვა მონაცემების დამატებისას
        print("✅ სტუდენტი დაემატა და შეინახა!")

    def view_all_students(self):
        #--- ყველა სტუდენტი ---
        if not self.students:
            print("სია ცარიელია.")
        else:
            for student in self.students:
                print(student)

    def find_student_by_roll(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def search_student(self):
        #--- სტუდენტის ძებნა ---
        try:
            roll_number = int(input("შეიყვანეთ საძიებო სიის ნომერი: "))
            student = self.find_student_by_roll(roll_number)
            if student:
                print("ნაპოვნია სტუდენტი:")
                print(student)
            else:
                print("❌ სტუდენტი ვერ მოიძებნა.")
        except ValueError:
             print("❌ შეცდომა: სიის ნომერი უნდა იყოს რიცხვი.")

    def update_student_grade(self):
        #--- შეფასების განახლება ---
        try:
            roll_number = int(input("შეიყვანეთ სტუდენტის სიის ნომერი: "))
            student = self.find_student_by_roll(roll_number)

            if student:
                print(f"მიმდინარე შეფასება: {student.grade}")
                new_grade = input("შეიყვანეთ ახალი შეფასება: ").strip()
                
                old_grade = student.grade
                student.grade = new_grade 
                
                if student.grade != old_grade:
                    self.save_data() # შენახვა მონაცემების განახლებისას
                    print("✅ შეფასება განახლდა და შეინახა.")
            else:
                print("❌ სტუდენტი ვერ მოიძებნა.")
        except ValueError:
            print("❌ შეცდომა: სიის ნომერი უნდა იყოს რიცხვი.")