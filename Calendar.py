import datetime

# Get the input date from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Create a datetime object for the input date
date_obj = datetime.datetime(year, month, day)

# Get the day of the week (Monday is 0 and Sunday is 6)
day_of_week = date_obj.weekday()

# Define a list of weekday names
weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Display the day of the week for the input date
print(f"The day of the week for {date_obj.strftime('%Y-%m-%d')} is {weekday_names[day_of_week]}.")
