import random


def emp_wage():
    wage_per_hr = 20
    full_day_hr = 8
    part_time_hr = 4
    emp_present = 1
    emp_part_time = 2
    tot_working_days = 20
    tot_working_hrs = 100
    emphrs = 0
    days = 0
    while days <= tot_working_days or emphrs <= tot_working_hrs:
        attendance = random.randint(0, 2)
        if attendance == emp_present:
            print("Employee is Working Full Time")
            emphrs += full_day_hr
        elif attendance == emp_part_time:
            print(" Employee is Working Part Time ")
            emphrs += part_time_hr
        else:
            print("Employee is Absent")
            emphrs += 0

        if attendance != 0:
            days += 1

        daily_wage = emphrs * wage_per_hr
        print("daily wage = {}".format(daily_wage))

    total_emp_wage = wage_per_hr * emphrs
    return "Total Employee Wage = {}".format(total_emp_wage), "Total Employee Hrs ={}".format(emphrs)


if __name__ == "__main__":
    wage = emp_wage()
    print(wage)


