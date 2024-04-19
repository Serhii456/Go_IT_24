from datetime import datetime

def get_days_from_today(date_str):
    # Перетвірка введеної дати на об'єкт datetime
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        #today = datetime.strptime("2021-05-05", "%Y-%m-%d").date()
        days_diff = (today - given_date).days
        return days_diff
    except ValueError:
        print(f"Невірний формат дати: {date_str}")

print (get_days_from_today("2021-10-09"))
       
    
    


