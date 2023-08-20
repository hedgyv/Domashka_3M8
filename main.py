from datetime import datetime, timedelta
current_datetime = datetime.now()
print(current_datetime.date())
users = [
    {'name':'Sergey','bday': datetime(year=1980, month=8, day=15)},
    {'name':'Oleg','bday':datetime(year=1983, month=9, day=1)},
    {'name':'Yaroslav','bday':datetime(year=1985, month=8, day=13)},
    {'name':'Volodymyr','bday':datetime(year=1958, month=8, day=22)}
]

day_bday = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
    }

#print(users)


def get_birthdays_per_week(users):
    for user in users:
        if current_datetime.month == user['bday'].month:
            if user['bday'].day <= current_datetime.day + 7 and user['bday'].day >= current_datetime.day:
                #user's this year bday option
                current_bday = datetime(year = current_datetime.year, month = user['bday'].month, day = user['bday'].day)
                print(current_bday)
                #define weekday of bday
                wday = current_bday.strftime('%A') if current_bday.strftime('%A') not in ('Sunday' ,'Saturday') else 'Monday'
                #print(wday)
                day_bday[wday].append(user['name'])
        if user['bday'].month - current_datetime.month == 1:
            bday_next_month =  datetime(year = current_datetime.year, month = user['bday'].month, day = user['bday'].day)
            curr_date_prev_month =  datetime(year = current_datetime.year, month = current_datetime.month, day = current_datetime.day)
            print(bday_next_month)
            print(curr_date_prev_month)
            diff = bday_next_month - curr_date_prev_month
            print(type(diff))
            
            if user['bday'].day <= (current_datetime + timedelta(days=7)).day and diff.days <= 7:
                
                wday = bday_next_month.strftime('%A') if bday_next_month.strftime('%A') not in ('Sunday' ,'Saturday') else 'Monday'
                #print(wday)
                day_bday[wday].append(user['name'])
        #user['bday'].month == 1        
        if user['bday'].year - current_datetime.year == 1:
            bday_month_jan =  datetime(year = current_datetime.year + 1, month = user['bday'].month, day = user['bday'].day)
            curr_date_prev_year =  datetime(year = current_datetime.year, month = current_datetime.month, day = current_datetime.day)
            diff = bday_month_jan - curr_date_prev_year

            if user['bday'].day <= (current_datetime + timedelta(days=7)).day and diff.days <= 7:
                wday = bday_next_month.strftime('%A') if bday_next_month.strftime('%A') not in ('Sunday' ,'Saturday') else 'Monday'
                #print(wday)
                day_bday[wday].append(user['name'])

    #print the day and name(names)
    for day, names in day_bday.items():
        if names:
            print(f"{day}: {', '.join(names)}")
    
            
get_birthdays_per_week(users)