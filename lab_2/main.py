def lab_02_03():
    print("Hello, World!")

def lab_02_04():
    name= 'Denis'
    age = 21
    height = 180.0
    is_student = True
    print(f"Name: {name}\nAge: {age}\nHeight: {height} \nstudent: {is_student}")
    print(f"Name: {type(name)}\nAge: {type(age)}\nHeight: {type(height)} \nstudent: {type(is_student)}")

def lab_02_05():
    name = input("Enter name - ")
    secondName = input("Enter second name - ")
    age = input("Enter age - ")
    print(f"Name type: {type(name)}; Second name type: {type(secondName)}; Age type: {type(age)}")
    age = int(age)
    height = float(input("Enter height(with '.') - "))
    print(f"Name and type: {name}, {type(name)}; Second name and type: {secondName}, {type(secondName)}; Age and type: {age}, {type(age)}; Height and type: {height}, {type(height)}")

def lab_02_06():
    a = int(15)
    b = int(4)
    print(f"a + b = {a + b};\na - b = {a - b};\na * b: {a * b};\na / b =  {a / b};\na // b = {a // b};\na % b = {a % b};\na ** b = {a ** b}.")
    print(f"2 + 3 * 4 = {2 + 3 * 4}, (2 + 3) * 4 = {(2 + 3) * 4}")

def lab_02_07():
    x = float(input("Enter x (float with '.') - "))
    y = float(input("Enter y (float with '.') - "))
    print(f" x + y = {x + y}\n x - y = {x - y}\n x * y = {x * y}\n x / y = {x / y}")

def lab_02_08():
    print("from 1 to 10")
    for i in range(1,11,1):
        print(i)
    print("from 10 to 1")
    for j in range(10,0,-1):
        print(j)
    print("Even number form 0 to 20")
    for e in range(0,21,2):
        print(e)

