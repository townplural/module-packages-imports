from salary_package.salary import calculate_salary
from people_package.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now())
