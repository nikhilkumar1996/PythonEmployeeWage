import random

wage_per_hr = 20
full_day_hr = 8
part_time_hr = 4
emp_present = 1
emp_part_time = 2
tot_working_days = 20
empHrs = 0
for days in range(tot_working_days - 1):
    attendance = random.randint(0, 2)
    if attendance == emp_present:
        print("Employee is Working Full Time")
        empHrs += full_day_hr
    elif attendance == emp_part_time:
        print(" Employee is Working Part Time ")
        empHrs += part_time_hr
    else:
        print("Employee is Absent")
        empHrs += 0

total_emp_wage = wage_per_hr * empHrs
print("Total Employee Wage = ", total_emp_wage)

