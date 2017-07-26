straw = int(input('How many strawberries?'))

is_weekend = input('is it the weekend?')

if is_weekend == 'yes':
    if straw > 39:
        print('fun')
    else:
        print('not fun')
else:
    if straw > 39 and straw < 61:
        print('fun')
    else:
        print('not fun')
        
