from tabulate import tabulate

# Star
star = 12.5 / 40
print("Cost of single star " + str(star))

# Redeemables
deagle = 25 * star
collection = 4 * star
charm = 3 * star
case = 2 * star
sticker = 1 * star

# Table
print(tabulate([['Deagle', deagle], 
                ['Skin Collection', collection], 
                ['Charm', charm],
                ['Case', case],
                ['Sticker', sticker]], 
               headers=['Redeemable', 'Price'], 
               tablefmt='orgtbl'))