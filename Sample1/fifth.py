#sval=input('enter a number')
smallest=None
largest=None
while True:
    sval=input('enter a number: ')
    if sval=='done':
        break
    try:
        fval=int(sval)
    except:
        e='Invalid input'
        continue
    #find Maximum
    if largest is None:
        largest=fval
    elif fval>largest:
        largest=fval
    elif smallest is None:
        smallest=fval
    elif fval<smallest:
        smallest=fval
print(e)
print('Maximum is ',largest)
print('Minimum is ',smallest)
