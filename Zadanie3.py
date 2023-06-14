class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_albumu):
        super().__init__(imie, nazwisko)
        self.numer_albumu = numer_albumu

    def __str__(self):
        return f'Student: {self.imie} {self.nazwisko}, Numer albumu: {self.numer_albumu}'

    def przywitanie(self):
        return print(f'Cześć nazywam się {self.imie} {self.nazwisko} i mój numer albumu to {self.numer_albumu}')


student1 = Student("Adam", "Haraf", "998872")
student2 = Student("Julia", "Hadała", "796963")
student3 = Student("Marta", "Kowalska", "564784")

print(student1)
print(student2)
print(student3)

student2.przywitanie()