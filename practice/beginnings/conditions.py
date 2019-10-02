price = 1000 
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment = ${down_payment}")
#putting f before the quote makes it a formatted string which allows you to insert variables with {}


