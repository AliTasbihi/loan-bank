#LAR,LMP
def monthly_payment(principal,annual_interest_rate,duration):
#def commend in line in the word
                    r=annual_interest_rate/100/12
                    n=duration*12
                    if r==0:
                        payment=principal/12
                    else:    
                        payment=(principal*(r*(1+r)**n))/(((r+1)**n)-1)
                    return payment
##############################                
def ral(principal,annual_interest_rate,duration,number_of_payments):
    #به ترتيب ميزان پولي که گرفتيم،بهره ساليانه بانک،تعداد پرداخت ساليانه،تعداد دفعاتي که پرداخت کرديم
    r=annual_interest_rate/12/100#بهره که بانک ميگيره
    n=duration*12#تعداد کل پرداخت هاي ماهيانه
    p=number_of_payments#تعداد  کل پرداخت هاي انجام شده
    if r==0:
        Remaining_loan=principal-(principal*p)/n
    else:    
        Remaining_loan=(principal*((r+1)**n-(1+r)**p))/((1+r)**n-1)
    return Remaining_loan
###############################
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
print("LOAN AMOUNT:",int(principal),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
print("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(monthly_payment(principal,annual_interest_rate,duration)))
monthlypayment=monthly_payment(principal,annual_interest_rate,duration)
index=duration
for i in range(1,index+1):
    number_of_payments=i*12
    print("YEAR:",i,"BALANCE:",int(ral(principal,annual_interest_rate,duration,number_of_payments)),"TOTAL PAYMENT:",int(monthlypayment*i*12))
      
