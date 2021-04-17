def subin(x,y):
    if x >= y:
        result = x - y
    elif x < y:
        result = x - y + 60
    return result

def sub(x,y):
    result = {'h' : None , 'm':None , 's':None}
    
    result['s'] = subin(x['s'],y['s'])

    result['m'] = subin(x['m'],y['m'])
    if x['s'] < y['s']:
        result['m'] -= 1   
    result['h'] = x['h'] - y['h']
    if x['m'] < y['m']:
        result['h'] -= 1 
    return result

def sum(x,y):
    result = {'h' : None , 'm':None , 's':None}

    result['s'] = x['s'] + y['s']

    result['m'] = x['m'] + y['m']

    if result['s'] > 59:
        result['s'] = result['s'] - 60
        result['m'] = result['m'] +1
    
    result['h'] = x['h'] + y['h']
    if result['m'] > 59:
        result['m'] = result['m'] - 60
        result['h'] = result['h'] + 1
    return result

def sec(x):
    result = x['h'] * 3600 + x['m'] * 60 + x['s']
    return result

print('Choice your fuction :')
print('1 - sum two time \n2 - sub to time\n3 - sec to time\n4- time to sec')
choice = int(input())
if choice == 1 or choice ==2:
    e = int(input('saniye 1 ru vared konid : '))
    w = int(input('daqiqe 1 ru vared konid : '))
    q = int(input('saat 1 ru vared konid : '))
    r = int(input('saniye 2 ru vared konid : '))
    t = int(input('daqiqe 2 ru vared konid : '))
    y = int(input('saat 2 ru vared konid : '))
    a = {'h' :q , 'm' :w , 's': e}
    b = {'h' :y , 'm' :t , 's' :r}
    if choice == 1:
        c = sum(a,b)
        print(c['h'],':',c['m'],':',c['s'])
    if choice == 2:
        c = sub(a,b)
        print(c['h'],':',c['m'],':',c['s'])
if choice == 3:
    sec = int(input('Saniye ru vared konid : '))
    hour = sec // 3600
    sec2 = sec % 3600
    min = sec2 // 60
    sec3 = sec2 %60
    print(hour,':',min,':',sec3)
if choice == 4:
    e = int(input('saniye 1 ru vared konid : '))
    w = int(input('daqiqe 1 ru vared konid : '))
    q = int(input('saat 1 ru vared konid : '))
    a = {'h' :q , 'm' :w , 's': e}
    c = sec(a)
    print(c)

