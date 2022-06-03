
import math
def optimal_change(item_amount,amount_paid) :
    change_needed = ''
    change_needed = float(amount_paid - item_amount)
    change_given = ''

    money_obj = {
        '$100 bill': 100.00,
        '$50 bill':  50.00,
        '$20 bill':  20.00,
        '$10 bill':  10.00,
        '$5 bill':   5.00,
        '$1 bill':   1.00,
        'quarter':   0.25,
        'dime':      0.10,
        'nickle':    0.05,
        'penny':     0.01
    }

    if change_needed < 0:
        return ("Sorry! You don't have enough money!")

    for money in money_obj:
        output = ''
        counter = 0
        while change_needed >= money_obj[money] :
            counter += 1
            if money in output :      
                if money == 'penny' :
                    output = str(f'{counter} pennies.')
                    change_needed = round((change_needed  - money_obj[money]),2)
                else:
                    output = str(f'{counter} {money}s,')
                    change_needed = round((change_needed  - money_obj[money]),2)
            else :
                output = str(f'{counter} {money},')
                change_needed = round((change_needed  - money_obj[money]),2)
                
        change_given += f"{output} " 
        total_change =''
        total_change = total_change.join(change_given) 
        total_change = (total_change[:-2] +'.')
    return f"The optimal change for an item that costs ${item_amount} with an amount paid of ${amount_paid} is{total_change}"
