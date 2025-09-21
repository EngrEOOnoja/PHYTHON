temperatures = {
    'Monday': [66, 70, 74],
    'Tuesday': [50, 56, 64],
    'Wednesday': [75, 80, 83],
    'Thursday': [67, 74, 81]
}

for key, value in temperatures.items():
    print(f'The temperature of {key} is: {sum(value) / len(value):.2f}')
