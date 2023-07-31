from package.database.staff import get_employees
from package.salary import calculate_salary
from datetime import datetime


if __name__ == '__main__':
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #округляем до секунд
    print(t)
    get_employees()
    calculate_salary()