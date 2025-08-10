def get_divide_or_square(result):
	if result == float:
		raise ValueError
	if int(result) % 5 != 0 :
		raise ValueError
	if type(result) == str:
		raise ValueError
	if type(result) == chr:
		raise ValueError
	return result
	

def get_only_float(a, b):	
	if type(a or b) == str:
		raise ValueError	
	elif type(a and b) == chr:
		raise ValueError
	elif type(a and b) != float:
		return 0
	elif type(a or b) != float:
		return 1
	else :
		return 2
	

def get_investment_rate_years(investment_amount, monthly_investment_rate, no_of_months):
	if int(investment_amount) <= 0 or float(monthly_investment_rate) <= 0  or int(no_of_months <=0):
		raise ValueError
	investment_amount = 5_000_000
	monthly_investment_rate = .12
	n0_of_months = 60
	future_investment_value = investment_amount * (1 + monthly_investment_rate) ** no_of_months
	return future_investment_value
	
		
	
	

