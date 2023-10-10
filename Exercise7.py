from datetime import date

date_components = input("Enter date formatted as YYYY-MM-DD: ").split("-")
year, month, day = [int(item) for item in date_components]
d = date(year, month, day)
today = date.today()
diffDate = today - d
if today >= d:
    print(f"{diffDate.days} days have passed")
else:
    diffDate = d - today
    print(f"{diffDate.days} days left")
