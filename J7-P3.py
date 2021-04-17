import math
def sum(x,y):
    result = {'s' : None , 'm': None}
    result['s'] = x['s'] + y['s']
    result['m'] = x['m'] + y['m']

    return result

def sub(x,y):
    result = {'s' : None , 'm' : None}
    result['s'] = x['s'] - y['s']
    result['m'] = x['m'] - y['m']

    return result
def mul(x,y):
    result = {'s' :None , 'm':None}
    result['s'] = x['s'] * y['s'] - x['m'] * y['m']
    result['m'] = x['s'] * y['m'] + x['m'] * y['s']

    return result
def div(x,y):
    result = {'s' : None , 'm': None}
    result['s'] = (x['s'] * y['s'] + x['m'] * y['m']) / (y['s'] ** 2 + y['m'] ** 2)
    result['m'] = (x['m'] * y['s'] - x['s'] * y['m']) / (y['s'] ** 2 + y['m'] ** 2)

    return result


a= {'s':2 , 'm':3} 
b= {'s':4 , 'm' :-5}



c  = sum(a,b)
print(c['s'] , '+' , c['m'],'i')

c = sub(a,b)
print(c['s'] , '+' , c['m'],'i')

c = mul(a,b)
print(c['s'] , '+' , c['m'],'i')

c = div(a,b)
print(c['s'] , '+' , c['m'],'i')