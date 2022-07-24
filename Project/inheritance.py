'''B. Define a class person (attributes: name, department, date Of Birth). Derive two classes
employee (attributes: employee id, salary) and student (attributes: PRN, year, CGPA) from
person class. Derive two classes lab_assistant (attributes: labs) and faculty (attributes:
subject, number of research papers, qualification).
i) Create objects for lab assistant, faculties, and students.
ii) Display the data.
iii) Delete a data
iv) Find the total salary of all employees.
v) Find average CGPA of students department wise.
'''


def see():
    print('''Menu:i) Create objects for lab assistant, faculties, and students.
                ii) Display the data.
                iii) Delete a data
                iv) Find the total salary of all employees.
                v) Find average CGPA of students department wise.:
          ''')


class person:
    def __init__(self, name, department, date_of_birth):
        self.name = name
        self.department = department
        self.date_of_birth = date_of_birth

    def display(self):
        print('Name:', self.name)
        print('department:', self.department)
        print('date_of_birth:', self.date_of_birth)


class employee(person):
    def __init__(self, employee_id, salary, name, department, date_of_birth):
        self.employee_id = employee_id
        self.salary = salary
        person.__init__(self, name, department, date_of_birth)
    def display(self):
        person.display(self)
        print('Employee id:', self.employee_id)
        print('Salary:', self.salary)


class student(person):
    comp = 0
    electrical = 0
    def __init__(self, prn, year, cgpa, name, department, date_of_birth):
        self.prn = prn
        self.year = year
        self.cgpa = cgpa
        person.__init__(self, name, department, date_of_birth)

        if department == "Computer":
            student.comp += cgpa
        elif department == "Electrical":
            student.electrical += cgpa

    def display(self):
        person.display(self)
        print('PRN:', self.prn)
        print('Year:', self.year)
        print('CGPA:', self.cgpa)


class lab_assistant(employee):
    lab_salary = 0
    def __init__(self, labs, employee_id, salary, name, department, date_of_birth):
        self.labs = labs
        employee.__init__(self, employee_id, salary, name, department, date_of_birth)
        lab_assistant.lab_salary += salary
    def display(self):
        employee.display(self)
        print('Lab:', self.labs)


class faculty(employee):
    faculty_salary = 0

    def __init__(self, subject, research, qualification, employee_id, salary, name, department, date_of_birth):
        self.subject = subject
        self.research = research
        self.qualification = qualification
        employee.__init__(self, employee_id, salary, name, department, date_of_birth)
        faculty.faculty_salary += salary

    def display(self):
        employee.display(self)
        print('Subject:', self.subject)
        print('No. of Research Paper:', self.research)
        print('Qualification:', self.qualification)


# i)Create objects for lab assistant, faculties, and students.

lab1 = lab_assistant('Chemistry Lab', 150, 20000, 'Rajesh', 'Chemical', '13/05/1990')
lab2 = lab_assistant('Python Lab', 160, 25000, 'Suresh', 'Computer', '10/04/1992')
lab3 = lab_assistant('Electrical Lab', 170, 22000, 'Himesh', 'Electrical', '04/10/1995')

fac1 = faculty('Chemistry', 10, 'Ph.D', 130, 40000, 'Supriya', 'Chemical', '13/07/1990')
fac2 = faculty('Python', 8, 'M.Tech', 140, 35000, 'Pranali', 'Computer', '23/12/1995')
fac3 = faculty('ELectronics', 12, 'M.E', 120, 20000, 'Neeta', 'Electrical', '18/02/1992')

s1 = student(2030331245162, '2nd', 9.04, 'Priya Patil', 'Computer', '15/07/2000')
s2 = student(2030331245122, '2nd', 9.84, 'Ruhi More', 'Computer', '12/08/1998')
s3 = student(2030331245052, '2nd', 9.00, 'Rahul Deshmukh', 'Electrical', '28/03/2000')
s4 = student(2030331245032, '2nd', 9.76, 'Prachi Pawar', 'Electrical', '18/12/1999')

see()
while (True):
    key = int(input("Enter a choice key for operation :"))
    if key == 1:
        # ii) Display the data.
        print("Lab Assistent Data:")
        lab1.display()
        print()
        lab2.display()
        print()
        lab3.display()
        print()
        print("-------------------------------------------")

        print('Faculty Data:')
        fac1.display()
        print()
        fac2.display()
        print()
        fac3.display()
        print()
        print("-------------------------------------------")
        print('Student Data:')
        s1.display()
        print()
        s2.display()
        print()
        s3.display()
        print()
    elif key == 2:
        print('''Enter key to delete data
                1) Lab assistant ofr faculty
                2) student''')
        del_val = int(input('Enter key:'))
        if (del_val == 1):
            k = int(input('Enter Employee Id:'))
            if lab1.employee_id == k:
                print('Data of Lab Assistant {0} is deleted :'.format(lab1.name))
                del lab1
                print('Remaining Lab Assistant data:')
                lab2.display()
                print()
                lab3.display()
                print()
                print("-------------------------------------------")
            elif lab2.employee_id == k:
                print('Data of Lab Assistant {0} is deleted :'.format(lab2.name))
                del lab2
                print('Remaining Lab Assistant data:')
                lab1.display()
                print()
                lab3.display()
                print()
                print("-------------------------------------------")
            elif lab3.employee_id == k:
                print('Data of Lab Assistant {0} is deleted :'.format(lab3.name))
                del lab3
                print('Remaining Lab Assistant data:')
                lab1.display()
                print()
                lab2.display()
                print()
                print("-------------------------------------------")
            elif fac1.employee_id == k:
                print('Data of Faculty {0} is deleted :'.format(fac1.name))
                del fac1
                print('Remaining Faculty data:')
                fac2.display()
                print()
                fac3.display()
                print()
                print("-------------------------------------------")
            elif fac2.employee_id == k:
                print('Data of Faculty {0} is deleted :'.format(fac2.name))
                del fac2
                print('Remaining Faculty data:')
                fac1.display()
                print()
                fac3.display()
                print()
                print("-------------------------------------------")
            elif fac3.employee_id == k:
                print('Data of Faculty {0} is deleted :'.format(fac3.name))
                del fac3
                print('Remaining Faculty data:')
                fac1.display()
                print()
                fac2.display()
                print()
                print("-------------------------------------------")
            else:
                print('Employee Id is not found.')
        elif (del_val == 2):
            a = int(input('Enter PRN:'))
            if s1.prn == a:
                print('Data of Student {0} is deleted :'.format(s1.name))
                del s1
                print('Remaining Student data:')
                s2.display()
                print()
                s3.display()
                print()
                print("-------------------------------------------")
            elif s2.prn == a:
                print('Data of Student {0} is deleted :'.format(s2.name))
                del s2
                print('Remaining Student data:')
                s1.display()
                print()
                s3.display()
                print()
                print("-------------------------------------------")
            elif s3.prn == a:
                print('Data of Student {0} is deleted :'.format(s3.name))
                del s3
                print('Remaining Student data:')
                s1.display()
                print()
                s2.display()
                print()
                print("-------------------------------------------")
            else:
                print('PRN Number is not found.')

    elif key == 3:
        print("total Salary of Lab Assistants : ", lab_assistant.lab_salary)
        print("Total Salary of Faculty :", faculty.faculty_salary)
        Total = lab_assistant.lab_salary + faculty.faculty_salary
        print("Total salary of all employees :", Total)
        print()

    elif key == 4:
        comp_cgpa = student.comp / 2
        electrical_cgpa = student.electrical / 2
        print("Average CGPA of Computer Department is :", comp_cgpa)
        print("Average CGPA of Electrical Department is :", electrical_cgpa)
        print()

    elif key == 5:
        exit()

    else:
        print("Enter Correct Key Input.")
