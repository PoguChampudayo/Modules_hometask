from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
if __name__ == '__main__':
    actual_date = datetime.date.today()
    print(actual_date)
    print(calculate_salary())
    print(get_employees())