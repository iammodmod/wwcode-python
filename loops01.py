""" Aling Nena's Cashier Challenge
Author:
Description: During closing, Aling Nena counts from her vault the day's total income and
also the total amount of all her paper bills.

Help Aling Nena count her total income and total amount of her paper bills
from a list of cash money and using a loop!
"""


def is_coins(money):
    """ Determine if the money is a coin
    :param money: (Integer)
    :return: (Boolean)

    Examples:
        >>>  print(is_coins(20))
        False
        >>>  print(is_coins(1))
        True
    """
    if money < 20:
        return True
    return False

def compute(list_of_money):

    coins = 0
    bills = 0.00
    income = 0.00

    for money in list_of_money:

        if not is_coins(money):
            bills = bills + money

        income = income + money

    return {'income':income,'bills':bills}

# Main
cash_on_vault = [1, 5, 100, 10, 50, 50, 20, 5, 1, 1000, 1000, 500, 5, 200]
return_value = compute(cash_on_vault)

print(f"Aling Nena's Total income: { return_value['income'] }")
print(f"Aling Nena's Total Amount of Bills: { return_value['bills'] }")