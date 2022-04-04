import random

wage_per_hr = 20
full_day_hr = 8
is_present = 1
attendance = random.randint(0, 1)
if attendance == is_present:
    print("Employee is present")
    empHrs = full_day_hr
else:
    print("Employee is absent")
    empHrs = 0

daily_wage = wage_per_hr * empHrs
print("daily_wage = ", daily_wage)

