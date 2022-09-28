#!/usr/bin/python3
"""
This is a mini-program that asks user for their
Sandwich preference
"""
import pyinputplus as pyip

totalCost = 0.0
"""price list"""
prices = {"wheat": 0.5, "white": 0.5, "sourdough": 1.0, "chicken": 4.5,
          "turkey": 4.5, "ham": 5.0, "tofu": 3.5,
          "cheddar": 2.5, "Swiss": 2.5, "mozzarella": 3.0, "mayo": 1.4,
          "mustard": 1.0, "lettuce": 0.3, "tomato": 0.5}


"""sandwich maker function """
while True:
    order = {}
    print("what bread would you want ?")
    order["bread"] = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                                    numbered=True)
    print("what protein filling would you want ?")
    order["protein"] = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                                      numbered=True)
    cheese = pyip.inputYesNo('Do you want cheese?')
    if cheese == 'Yes':
        print("What type of cheese do you want ?")
        order["cheese"] = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],
                                         numbered=True)
    extra = pyip.inputYesNo('Do you want paste ?')
    if extra == 'Yes':
        print("What type of paste do you want ?")
        pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'],
                       numbered=True)
    orderNumber = pyip.inputInt('How many sandwich do you want ?', min=1)

    """Calculate choice of order"""
    for choice in order:
        if order[choice] in prices.key():
            totalCost += prices[order[choice]]
    """Adjust if more than one"""


totalCost *= orderNumber
while False:
    print("Would that be all ?")
    response = pyip.inputYesNo(print)
print("Ok, that will be Ksh" + "{::2f}".format(totalCost) + "please")
