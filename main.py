from datetime import datetime, timedelta
current_datetime = datetime.now()
print(current_datetime.date())
users = [
    {'Sergey':datetime(year=1980, month=8, day=15)},
    {'Oleg':datetime(year=1983, month=8, day=15)},
    {'Yaroslav':datetime(year=1985, month=8, day=13)},
    {'Volodymyr':datetime(year=1958, month=8, day=22)}
]

days_with_b_users = list()
days_with_b_users_after_week = list()
days_with_b_users_on_holiday = list()

#print(users)


def get_birthdays_per_week(users):
    one_week_interval = timedelta(weeks=1)
    one_week_date_further = current_datetime.date() + one_week_interval
    print(one_week_date_further)

    for i in users:
        for key, value in i.items():
            if value.month == one_week_date_further.month and value.day == one_week_date_further.day:
                #при условии, что неделя вперед не выпадает на следующий год year=current_datetime.year
                value = datetime(year=current_datetime.year, month=value.month, day=value.day)
                #print(f'{key} has a B-DAY at {value.strftime("%d %B")}')
                days_with_b_users_after_week.append(key)
                print('B-Day mentioned before one week')
                print(f'{value.strftime("%A")}: {days_with_b_users_after_week}')
            if current_datetime.month == value.month and current_datetime.day == value.day:
                value = datetime(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day)
                if value.weekday() != 5 or value.weekday() != 6: 
                    days_with_b_users.append(key)
                    print('Happy B-Day!')
                    print(f'{value.strftime("%A")}: {days_with_b_users}')
                    
                    #print(days_with_b_users)
            #проблема с логикой, когда поздравить надо в понедельник тех, у кого др в субботу или воскресенье        
            else:
                if (current_datetime.day - value.day) == 1 or (current_datetime.day - value.day) == 2 and current_datetime.weekday() != 1:
                    #при условии, что неделя вперед не выпадает на следующий год year=current_datetime.year
                    value = datetime(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day)
                    #print(value.weekday())
                    days_with_b_users_on_holiday.append(key)
                    print('B-Day was on holidays')
                    print(f'{value.strftime("%A")}: {days_with_b_users_on_holiday}')
            
get_birthdays_per_week(users)