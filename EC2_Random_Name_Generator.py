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
        print("Sorry, this Name Generator can only be used by the Marketing, Accounting, and FinOps Departments.")


while True:
    num = input("How many instances would you like to name: ")
    if num.isdigit() and int(num) > 0:
        break
    else:
        print(f"\n'{num}' is not a valid entry, please enter a whole number greater than 0.")
dept = input("\nEnter your Department (Marketing, Accounting, or FinOps): ").lower()
print('')
check_dept(int(num), dept)
