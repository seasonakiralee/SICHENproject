class Student():
    pass

wujia = Student()

class PythonStudent():
    name = None
    age = 18
    course = "python"

    def doHomework(self):
        print("I'm doing my home work")
        return None

jiajia = PythonStudent()
print (jiajia.age)
print (jiajia.course)
print(jiajia.name)
jiajia.doHomework()