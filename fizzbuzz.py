x = 0
for x in range(100):
    count = x + 1 
    if count % 15 == 0:
        print('fizzbuzz')
    elif count % 3 == 0:
        print('fizz')
    elif count % 5 ==0:
        print('buzz')
    else:
        print(count)
