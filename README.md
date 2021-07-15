# budget-app
This is a project done to complete the freecodecamp.org Scientific Computing with Python certificate.....

There is a  `Category` class in `budget_app.py`. It instantiates objects based on different budget categories like *food*, *clothing*, and *entertainment*. When objects are created, they are passed in the name of the category. The class have an instance variable called `ledger` that is a list. The class contain the following methods:

* A `deposit` method that accepts an amount and description. If no description is given, it default to an empty string. The method append an object to the ledger list in the form of `{"amount": amount, "description": description}`.
* A `withdraw` method that is similar to the `deposit` method, but the amount passed in is stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method  return `True` if the withdrawal took place, and `False` otherwise.
* A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
* A `transfer` method that accepts an amount and another budget category as arguments. The method add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledgers. This method return `True` if the transfer took place, and `False` otherwise.
* A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method is used by both the `withdraw` method and `transfer` method.

When the budget object is printed it displays:

* A title line of 30 characters where the name of the category is centered in a line of * characters.
* A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
* A line displaying the category total.

Here is the output when run the main.py code:

'''
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
***********Clothing***********
Transfer from Food       50.00
                        -25.55
Total: 24.45
'''
Besides the `Category` class, there is a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. It  returns a string that is a bar chart.

Here is the output graph of the code:

'''
Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
 '''
