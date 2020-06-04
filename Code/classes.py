class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_ = "student"

    def scores(self, score1, score2, score3):
        return int((score1 + score2 + score3) / 3)


Callum = Student("Callum", 27)
John = Student("John", 26)

print(Callum.scores(5, 5, 5))
print(getattr(Callum, "age"))
