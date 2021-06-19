############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

class Category:
    ''' Category class that represents a spending category in the budget.''' 

    def __init__(self, category):
        ''' Constructor for class Category. Takes a category name (str)
            as an input.
        
        @param self: Category class instance self-reference
        @param category: category name as a string
        @return: None
        '''
        self.category = category
        self.ledger = list()
    
    def __str__(self):
        ''' Creates string representation of any instance of Category.

        @param self: Category class instance self-reference
        @return: string representation of this instance of Category
        '''
        s = self.category.center(30, '*') + '\n'

        for item in self.ledger:
            temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            s += temp + "\n"
        
        s += "Total: " + str(self.get_balance())
        return s

    def deposit(self, amount, description=""):
        ''' Accepts an amount and description (optional) and appends an object
            to the ledger list containing said amount and description in 
            dictionary format.

        @param self: Category class instance self-reference
        @param amount: the amount to deposit into the ledger
        @return: None 
        '''
        temp = dict()
        temp['amount'] = amount
        temp['description'] =  description
        self.ledger.append(temp)

    def withdraw(self, amount, description=""):
        ''' Accepts an amount and description and appends an object to the
            ledger list similarly to Category.deposit() but as a negative 
            number rather than a positive number.

        @param self: Category class instance self-reference
        @param amount: the amount to withdraw from the ledger
        @return: true if function successful and false otherwise 
        '''
        if self.check_funds(amount):
            temp = dict()
            temp['amount'] = 0 - amount
            temp['description'] = description
            self.ledger.append(temp)
            return True
        return False

    def get_balance(self):
        ''' Checks the current balance in the ledger.

        @param self: Category class instance self-reference
        @return: a float that represents the current balance of the ledger 
        '''
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance
    
    def transfer(self, amount, budget_cat):
        ''' Accepts an amount and budget category to transfer money into.
            Adds a withdrawal with a description stating it as a transfer
            to the destination category and then adds a deposit to the other
            budget category with a description stating it as a transfer. If 
            not enough funds are available, returns False and nothing changes.

        @param self: Category class instance self-reference 
        @param amount: amount to be transferred
        @param budget_cat: category to transfer money to
        '''
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + budget_cat.category)
            budget_cat.deposit(amount, 'Transfer from ' + self.category)
            return True
        return False
        
    def check_funds(self, amount):
        ''' Takes input amount and returns False if the amount is less than 
            that in the budget category, and returns True otherwise.

        @param self: Category class instance self-reference
        @param amount: amount to check if it exists in category
        @return: true if amount exists and false otherwise 
        '''
        if amount > self.get_balance():
            return False
        return True

def create_spend_chart(categories):
    ''' Creates the spending chart to print out and display for the user with
        the given input categories list.

    @param categories: a list of categories
    @return: the spending chart as a string
    '''
    spend_chart = list()
    for category in categories:
        temp = 0

        for item in category.ledger:
            if item['amount'] < 0:
                temp += abs(item['amount'])
        spend_chart.append(temp)

    total = sum(spend_chart)
    percent = [val/total * 100 for val in spend_chart]

    s = 'Percentage spent by category'
    for i in range(100, -1, -10):
        s += '\n' + str(i).rjust(3) + '|'

        for j in percent:
            if j > i:
                s += ' o '
            else:
                s += '   '
                
        s += ' '
    s += '\n    ----------'

    cat_len = list()
    for category in categories:
        cat_len.append(len(category.category))
    max_len = max(cat_len)

    for i in range(max_len):
        s += '\n    '
        for j in range(len(categories)):
            if i < cat_len[j]:
                s += ' ' + categories[j].category[i] + ' '
            else:
                s += '   '
        s += ' '
    
    return s