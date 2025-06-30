
def monthly_wage(annual_wage):
	return annual_wage / 12

def weekly_wage(monthly_wage):
	return monthly_wage / 4

def hourly_wage(weekly_wage, working_hours):
	return weekly_wage / working_hours

your_annual_wage = float(input("Your annual wage: \n"))
worked_hours = float(input("Your working hours this week: \n"))

month_wage = monthly_wage(your_annual_wage)
week_wage = weekly_wage(month_wage)
your_hourly_wage = hourly_wage(week_wage, worked_hours)

print(f"Your hourly wage is {your_hourly_wage}$")