import random
import json 
from dict2xml import dict2xml
import xmltodict
import os
from msvcrt import getch


class Person:
    def __init__(self, param):
            self._name = param[0]
            self._surname = param[1]
            self._phone = param[2]
            self._email = param[3]
    
    def __str__(self):
        return f"{self._name, self._surname, self._email, self._phone}"
        

class Student(Person):
    def __init__(self, param):
        super().__init__(param)
        self._studentId = str(random.randint(1,1000))
        self._averMark = param[4]
        self._group = ""

    def __str__(self):
        try:
            return f"{self._name, self._surname, self._email, self._phone, self._studentId, self._averMark}"
        except:
            return f"{self._studentId, self._averMark}"


class Professor(Person):
    def __init__(self, param):
            super().__init__(param)
            self._id = random.randint(1,1000)
            self._department = param[4]
            self._title = param[5]
            self._group = ""

    def __str__(self):
        try:
            return f"{self._name, self._surname, self._email, self._phone,self._id, self._department, self._title, self._group}"
        except:
            return f"{self._id, self._department, self._title, self._group}"

 
class Manager():
    def __init__(self, name = ""):
        self._name = name

    def addProfessor(self, Professor):
        Professor._group = self._name

    def addStudent(self, Student):
        Student._group = self._name


class FileManager():
    def __init__(self) -> None:
        pass

    def write_json(self, path = "data.json", *args):
        for ar in args:
            with open(path, 'w') as outfile:
                json.dump(ar, outfile, ensure_ascii=False)

    def read_json(self, path = ""):

        try:
            with open(path, "r") as json_file:
                data = json.load(json_file)

            return data

        except TypeError:
            print("Path must be string")

    def write_xml(self, path = "data.xml", *args):
        for ar in args:
            with open(path, "w") as outfile:
                outfile.write(dict2xml(ar, wrap = 'data'))

    def read_xml(self, path = ''):
        xml_file = open(path, 'r')
        xml_content = xml_file.read()

        return xmltodict.parse(xml_content)


def main():
    print("Вы хотите прочесть или записать файл? Введите 1 or 2 соответсвенно")
    a=input()
    if a == "1":
        fileM = FileManager()
        try:
            print("Введите путь")
            path = str(input())
            if path.split('.')[-1] == "xml":
                print(fileM.read_xml(path))
            elif path.split('.')[-1] == "json":
                print(fileM.read_json(path))

        except TypeError:
            print("Неверный вид путя")
        except FileNotFoundError:
            print("Такого файла не существует")

    elif a == "2":

        persons = []

        def create(clas):
            try:
                if clas == "Student":

                    try:
                        print("Введите Имя Фамилия Номер телефона Почта Среднюю оценку через пробел")
                        param = input()
                        elem = Student(param.split(' '))
                        persons.append(elem)
                        
                    except Exception:
                        print("Что-то пошло не так")

                elif clas == "Professor":
                    print("Введите Имя Фамилия Номер телефона Почта Кафедру Должность через пробел")
                    param = input()
                    elem = Professor(param.split(' '))
                    persons.append(elem)
            except:
                print("Вы что-то ввели неверно:( Попробуйте еще раз")

        def add():
            try:
                print("Введите название группы")
                manager = Manager(input())
                print(manager._name)
                if isinstance(persons[-1], Student):
                    manager.addStudent(persons[-1])
                elif isinstance(persons[-1], Professor):
                    manager.addProfessor(persons[-1])

            except:
                print("Что-то пошло не так")

        def filem(f):
            data = {}
            p = {}

            try:
                fileM = FileManager()
                print("Input path")
                path = input()

                if f == "1":
                    for i in persons:
                        if isinstance(i, Student):
                            p[i._name] = i.__dict__
                    data["persons"] = p
                    if len(data["persons"]) == 0:
                        print("No students")
                    else:
                        fileM.write_json(path ,data)
                        
                elif f == "2":
                    for i in persons:
                        if isinstance(i, Professor):
                            p[i._name] = i.__dict__
                    data["persons"] = p
                    if len(data["persons"]) == 0:
                        print("No professors")
                    else:
                        fileM.write_xml(path, data)

                else:
                    print("Goodbye")

            except:
                print("Что-то пошло не так")
    
        def addAll():
            print("Student or Professor, input 1 or 2. Input 3, if you want add all persons to one group")
            inp = input()
            print("Введите название группы:")
            group = input()

            if inp == "3":
                for i in persons:
                    i._group = group
            elif inp == "1":
                for i in persons:
                    if isinstance(i, Student):
                        i._group = group
            elif inp == "2":
                for i in persons:
                    if isinstance(i, Professor):
                        i._group = group
            else:
                print("Вы что-то ввели неверно. Попробуйте еще раз")


        while True:
            print("What you want?\n  1) Create Student\n  2) Create Professor\n  3) Add last persons to group\n  4) Create JSON on students")
            print("  5) Create XML on professors\n  6) Add students or professors or all persons to group\n  7) Finish program")
            print("  SPASE check list\n ")
            print("P.S. press key (1-7 or SPACE)")
            
            n = ord(getch())
            os.system('CLS')

            if n == 49:
                create("Student")
            elif n == 50:
                create("Professor")
            elif n == 51:
                add()
            elif n == 52:
                filem("1")
            elif n == 53:
                filem("2")
            elif n == 54:
                addAll()
            elif n == 55:
                break
            elif n == 32:
                print(*persons)


    else:
        print("Запустите программу сначала. Вы что-то ввели неверно(")
        return -1
            

if __name__ == "__main__":
    main()

    
