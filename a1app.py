"""User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Brandon Nathasingh bn243 Taerim Eom te89
Date:   09/24/19"""
import a1
source= str(input('Enter source currency: '))
target= str(input('Enter target currency: '))
amount= float(input('Enter original amount: '))
result= a1.exchange(source, target, amount)
print('You can exchange '+str(amount)+' '+str(source)+' for '+str(result)+' '+
str(target)+'.')
