def solution(price):

    if price>=500000:
        price= price-0.2*price
    elif price>=300000:
        price=price-0.1*price
    elif price>=100000:
        price=price-0.05*price
        
    return int(price)