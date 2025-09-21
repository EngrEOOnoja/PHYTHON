def number_to_words(n):
    ones = {
        0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
        14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen'
    }

    tens = {
        2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
        6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'
    }

    if n == 0:
        return 'Zero'
    elif n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    else:
        return ones[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + number_to_words(n % 100))


def check_amount_to_words(amount):
    if amount >= 1000 or amount < 0:
        return "Amount must be between 0 and 999.99"

    dollars = int(amount)
    cents = round((amount - dollars) * 100)

    dollar_words = number_to_words(dollars).upper()
    return f"{dollar_words} AND {cents:02d}/100"

amount = float(input("Enter a check amount less than 1000: "))
print(check_amount_to_words(amount))
