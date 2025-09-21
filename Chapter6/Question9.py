tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
print('Canada' in tlds)
print('France' in tlds)
for country, tld in tlds.items():
    print(f'{country:<15} {tld}')
tlds['Sweden'] = 'sw'
print(tlds)
tlds['Sweden'] = 'se'
print(tlds)
reversed_tlds = {tld: country for country, tld in tlds.items()}
print(reversed_tlds)
uppercase_tlds = {tld: country.upper() for tld, country in reversed_tlds.items()}
print(uppercase_tlds)
