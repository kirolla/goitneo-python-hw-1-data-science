from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # створення словника для зберігання імен користувачів по днях тижня
    birthdays_per_week = defaultdict(list)
    
    # отримання поточної дати
    today = datetime.today().date()

    # перебір користувачів
    for user in users:
        # конвертація дати народження до типу date
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        # оцінка дати на цей рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                    
        # порівняння з поточною датою
        delta_days = (birthday_this_year - today).days

        # визначення дня тижня
        if delta_days < 7:
            # вихідні дні переносяться на понеділок
            if birthday_this_year.weekday() >= 5:
                weekday = 0
            else:
                weekday = birthday_this_year.weekday()
                
            # зберігання імені користувача в відповідний день тижня
            birthdays_per_week[weekday].append(name)
    
    # виведення результату
    for weekday, names in birthdays_per_week.items():
        weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][weekday] + ':'
        print(weekday_name, ', '.join(names))

# Приклад використання функції
users = [
    {'name': 'Iryna Podporina', 'birthday': datetime(1988, 3, 26)},
    {'name': 'Aleksandr Popov', 'birthday': datetime(1993, 7, 21)},
    {'name': 'Kataryna Gutieva', 'birthday': datetime(1989, 5, 14)},
    {'name': 'Mihailo Kravetz', 'birthday': datetime(1992, 12, 10)},
    {'name': 'Borys Samchyk', 'birthday': datetime(1982, 5, 28)},
    {'name': 'Maryna Nikitenko', 'birthday': datetime(1984, 5, 14)},
    {'name': 'Semen Kolusko', 'birthday': datetime(1992, 12, 8)},
]

get_birthdays_per_week(users)
