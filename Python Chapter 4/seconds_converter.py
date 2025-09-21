
def seconds_since_midnight(Hours , Minutes, Seconds ):
	hour_in_seconds = Hours * 60 *60
	minute_in_seconds = Minutes * 60
	seconds = Seconds 
	converted_seconds = hour_in_seconds + minute_in_seconds + seconds
	return converted_seconds


Hours = 13
Minutes = 30
Seconds = 45
result = seconds_since_midnight(Hours, Minutes, Seconds)
print(result)





def average(first, *go):
    total = first + sum(go)
    return total / (1 + len(go))
    
print(average(10, 20, 30))  # Output: 20.0
print(average(5))  # Output: 5.0

try:
    print(average())
except TypeError as e:
    print(e)

def my_function(*go):
	return go 
    
digit = 1, 2, 3, 4, 5
result = my_function(digit)
print(result)



