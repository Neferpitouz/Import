from application.people import get_employees
from application.salary import calculate_salary
from datetime import date


def main():
    print(date.today())
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
