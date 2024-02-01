
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    price_change = current_price - last_month_price
    mort_est = float((current_price * 0.051) / 12)
    print('This house is $'+ str(current_price)+'. The change is $'+str(price_change)+' since last month.')
    print('The estimated monthly mortgage is $'+f'{mort_est:.2f}'+'.')
if __name__ == "__main__":
    real_estate()