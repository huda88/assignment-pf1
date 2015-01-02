def eliminate(s, letters):
    for i in s:
        if i not in letters:
            print (i, end='')
    print('')

eliminate('programing', 'pro')
eliminate('txrwy iwmpxqowrt qanxtigwxraqvity win qxpywtwhoxn', 'qwx')
