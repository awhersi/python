import random
import string


def name_generator(num_instances=1, dept_name=''):
    for i in range(num_instances):
        name_length = random.randint(8, 16)
        char = string.ascii_letters + string.digits + '+-=._:/@'
        ec2_name = dept_name + ''.join(random.choices(char, k=name_length))
        print(ec2_name)


def check_dept(num_instances, dept_name):
    departments = ['marketing', 'accounting', 'finops']
    if any(name in dept_name for name in departments):
        dept_name += '_'
        name_generator(num_instances, dept_name)
    else:
        print("Sorry, this Name Generator can only be used by the Marketing, Accounting, and FinOps Departments")


while True:
    num = int(input("Number of instances to name: "))
    if num > 0:
        break
dept = input("Department (Marketing, Accounting, or FinOps): ").lower()
check_dept(num, dept)
