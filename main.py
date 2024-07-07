from flask import Flask, render_template
from datetime import datetime, date


app = Flask(__name__)

def get_days(year, month):
    year = int(year) 
    month = int(month)
    
    month_map = {
    1: 31, 
    2: 28,
    3: 31, 
    4: 30, 
    5: 31, 
    6: 30, 
    7: 31, 
    8: 31, 
    9: 30, 
    10: 31, 
    11: 30, 
    21: 31
    }
    
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            return 29

    return month_map[month]


@app.route("/")
def main_page():
    return "<p>This is probably where the login page will go</p>"


@app.route("/user/<year>/<month>/<day>")
def calander(year, month, day):
    try:
        dt = datetime(int(year), int(month), int(day))
    except:
        return app.redirect(f"/user/2024/7/27") #Redirect to current date instead
    
    start_day = datetime(int(year), int(month), 1)
    day_of_week = start_day.weekday() + 1 #using this we know where to start iterating through the array
    num_days = get_days(year, month)

    calander_display = [[0 for column in range(0, 7)] for row in range(6)]

    count = 1
    for row in range(len(calander_display)):
        for column in range(len(calander_display[row])):
            if row == 0 and column >= day_of_week or row > 0 and count <= num_days:
                calander_display[row][column] = count
                count += 1
    
    print(calander_display, day_of_week, num_days)
    return render_template("calendar.html", year=year, month=month, day=day, calander_display=calander_display)


app.run(debug=True)


    
    