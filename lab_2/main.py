def lab_02_03():
    print("Hello, World!")

def lab_02_04():
    name = 'Denis'
    age = 21
    height = 180.0
    is_student = True
    print(f"Name: {name}\nAge: {age}\nHeight: {height} \nstudent: {is_student}")
    print(f"Name: {type(name)}\nAge: {type(age)}\nHeight: {type(height)} \nstudent: {type(is_student)}")

def lab_02_05():
    name = input("Enter name - ")
    second_name = input("Enter second name - ")
    age = input("Enter age - ")
    print(f"Name type: {type(name)}; Second name type: {type(second_name)}; Age type: {type(age)}")
    age = int(age)
    height = float(input("Enter height(with '.') - "))
    print(f"Name and type: {name}, {type(name)}; Second name and type: {second_name}, {type(second_name)}; Age and type: {age}, {type(age)}; Height and type: {height}, {type(height)}")

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
    for i in range(1, 11, 1):
        print(i)
    print("from 10 to 1")
    for j in range(10, 0, -1):
        print(j)
    print("Even number form 0 to 20")
    for e in range(0, 21, 2):
        print(e)

def lab_02_09():
    n = int(input("Enter n(n>0 and integer) - "))
    summ = 0
    for i in range(1,n+1):
        summ += i
    print(summ)

def lab_02_10():
    count  = 10
    while count >= 1:
        print(count)
        count -= 1
    print("The cycle is complete")

def lab_02_11():
    import math
    import random
    radius = random.randint(1, 10)
    L = 2 * math.pi * radius
    S = math.pi * radius ** 2 
    print(f"Radius = {radius}\nL = {L}, S = {S}")
    i = random.randint(0,50)
    print(f"√{i} = {math.sqrt(i)}")

def lab_02_12():
    x = int(input("Enter integer - "))
    if x > 0:
        print("Number is positive")
    elif x < 0:
        print("Number is negative")
    else:
        print("Number equals 0")
    if x % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def lab_02_13():
    import random
    for i in range(5):
        age = random.randint(17,22)
        has_access = bool(random.getrandbits(1))
        if age >= 18 and has_access == True:
            print(f"Age: {age}\nAccess: {has_access}\nAccess granted")
        else:
            print(f"Age: {age}\nAccess: {has_access}\nAccess denied")

def lab_02_14():
    n = int(input("Enter n - "))
    sum = 0
    numbers = []
    for i in range(n):
        x = float(input("Enter number - "))
        numbers.append(x)
        sum += x
    print(f"Sum - {sum}\navg - {sum / n}")
    print(f"Numbers - {numbers}")

