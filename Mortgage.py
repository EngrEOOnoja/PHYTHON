PERCENTAGE = 100
MONTH_IN_YEARS = 12
principal = int(input('Enter principal :'))
duration_in_years = int(input("Enter duration in years : "))
rate_in_years = int(input("Enter_annual_intrest_rate_in_years : ")) 
duration_in_month = duration_in_years * MONTH_IN_YEARS
rate_in_month = (rate_in_years / 100) / MONTH_IN_YEARS
monthly_payment_value =  principal * (rate_in_month * ((1 + rate_in_month) ** duration_in_month)) / (((1 + rate_in_month) ** duration_in_month) - 1)
print(round(monthly_payment_value,2))


 









