# Task 1A
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book_name):
        self.borrowed_books.append(book_name)

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
        else:
            print(f"{book_name} is not in the borrowed list.")

    def show_info(self):
        print(f"Member Name: {self.name}")
        print(f"Borrowed Books: {self.borrowed_books}")

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name


m =  Member("Alice", 101)
m.borrow_book("Titanic")
m.borrow_book("Hello")
m.return_book("World")
m.show_info()
m.getName()
m.setName("Bob")
m.show_info()


# Task 1B
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, subject, grade):
        if grade >= 0 and grade <= 100:
            self.grades[subject] = grade
        else:
            print(f"Grade {grade} is invalid, grade must be between 0 and 100")

    def calculate_average(self):
        for grade in self.grades.values():
            total = sum(self.grades.values()) / len(self.grades)
            return total

    def get_info(self):
        print(f"Student Name: {self.name}")
        print(f"Have {self.calculate_average()} average grade")

s = Student("John", {"Math": 85, "Science": 90})
s.add_grade("English", 95)
s.add_grade("History", 105)
s.get_info()



# Task 2
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eating(self):
        print(f"The {self.species} {self.name} is eating.")

    def drinking(self):
        print(f"The {self.species} {self.name} is drinking water.")

    def sleeping(self):
        print(f"The {self.species} {self.name} is sleeping.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def eating(self):
        return super().eating()

    def barking(self):
        print(f"{self.name} is a {self.breed} and he is barking Woof!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def drinking(self):
        super().drinking()
        print(f"{self.name} is drinking milk too.")

    def meowing(self):
        print(f"{self.name} says Meow!")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, species="Bird")

    def sleeping(self):
        print(f"{self.name} is sleeping on a tree branch.")

    def flying(self):
        print(f"{self.name} is flying.")

if __name__ == "__main__":
    d = Dog("Buddy", "Golden Retriever")
    d.eating()
    d.barking()

    c = Cat("Tom", "Blue")
    c.drinking()
    c.meowing()

    b = Bird("Titi")
    b.sleeping()
    b.flying()

    animals = [d, c, b]

    for animal in animals:
        animal.sleeping()