
import math
def optimal_change(item_amount, amount_paid) :
    change_needed = ''
    change_needed = float(amount_paid - item_amount)
    print((change_needed))
    change_given = ''
    money_obj = {
        '$100':  100.00,
        '$50':        50.00,
        '$20':       20.00,
        '$10':          10.00,
        '$5':         5.00,
        '$1':          1.00,
        'quarter':      0.25,
        'dime':         0.10,
        'nickle':       0.05,
        'penny':        0.01
    }

    for money in money_obj:
        counter = 0
        # print(change_needed,change_given)
        while change_needed >= money_obj[money] :
            counter += 1
            change_given += str(f'{counter} {money}, ')
            change_needed = round((change_needed  - money_obj[money]),2)
    print(change_given)
        # print(money,money_obj[money])
    return (f"The optimal change for an item that costs ${item_amount} with an amount paid of ${amount_paid} is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("1:", optimal_change(62.13, 100))