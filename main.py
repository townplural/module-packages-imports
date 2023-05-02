from salary import calculate_salary
from people import get_employees
from datetime import datetime

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now())
