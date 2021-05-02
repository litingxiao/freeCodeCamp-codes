class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        # add title line
        pos = (30 - len(self.name)) // 2
        outstr = '*' * pos + self.name + '*' * (30 - len(self.name) - pos) + '\n'

        # add lines of items in the ledger
        for item in self.ledger:
            if len(item['description']) > 23:
                outstr += item['description'][:23]
            else:
                outstr += item['description'] + ' ' * (23 - len(item['description']))
            outstr +=  '{:7.2f}'.format(item['amount']) + '\n'

        # add category total
        outstr += 'Total: ' + str(self.get_balance())
        return outstr

    def get_balance(self):
        return sum([i["amount"] for i in self.ledger])

    def check_funds(self, amount):
        return False if self.get_balance() < amount else True
        
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, seccat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + seccat.name)
            seccat.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False


def create_spend_chart(categories):
    outstr = "Percentage spent by category\n"

    # calculate the spending percentage
    spent = [sum([-l['amount'] for l in cat.ledger if l['amount'] < 0]) for cat in categories]
    percentage = [(s / sum(spent) * 100) // 10 * 10 for s in spent]

    # create the barchart
    for num in range(100, -10, -10):
        # percentage rowname
        outstr += str(num).rjust(3)
        
        for i, per in enumerate(percentage):
            # place barchart marker
            marker = 'o' if per >= num else ' '
            outstr += '| ' + marker if i == 0 else '  ' + marker
            
            # add extra space at EOL
            outstr += '  \n' if i == len(percentage) - 1 else ''

    # add '-' line
    outstr += ' ' * 4 + '-' * (3 * len(percentage) + 1) + '\n'

    # add barchart category names
    maxlen = max([len(cat.name) for cat in categories])
    for i in range(maxlen):
        for j, cat in enumerate(categories):
            marker = cat.name[i] if len(cat.name) > i else ' '
            outstr += ' ' * 5 + marker if j == 0 else ' ' * 2 + marker

            if j == len(categories) - 1:
                outstr += '  \n' if i != maxlen - 1 else '  '

    return outstr