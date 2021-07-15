class Category:
    def __init__(self,category):
        self.category=category
        self.ledger=[]
        self.total=0

        
    def check_funds(self,amount):
        if amount > self.total:
            return False
        elif amount <= self.total:
            return True
    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount

        
    def withdraw (self,amount,description=""):
        if self.check_funds(amount)==False:
            return False
        elif self.check_funds(amount)==True:
            self.ledger.append({"amount": -amount, "description": description})
            self.total = self.total-amount

            return True

    def get_balance(self):
        return self.total
    
    def transfer(self,amount,category):
        if self.check_funds(amount)==False:
            return False
        elif self.check_funds(amount)==True:
            self.withdraw(amount,f"Transfer to {category.category}")
            category.deposit(amount,f"Transfer from {self.category}")
            return True
        
    def __str__(self):
        head = f"{self.category:*^30}\n"
        trans=""
        for transaction in self.ledger:
            trans += f"{transaction['description'][0:23]:23}{transaction['amount']:>7.2f}\n"
        total=f"Total: {self.total}"
        string = head + trans + total   

        return string
def create_spend_chart(categories):
  
    s="Percentage spent by category\n"
    sum=0
    withdraws={}
    for x in categories:
        withdraws[x.category]=0
        for y in x.ledger:
            if y['amount']<0:
                withdraws[x.category]+=y['amount']
        withdraws[x.category]=-withdraws[x.category]
    for x in withdraws:
        sum+=withdraws[x]
    for x in withdraws:
        withdraws[x]=int(withdraws[x]/sum*100)
        
    for i in range(100,-10,-10):
        s+=str(i).rjust(3)+'| '
        for x in categories:
            if withdraws[x.category]>=i:
                s+='o  '
            else:
                s+='   '
        s+='\n'
    s+=' '*4+'-'*(1+len(categories)*3)+'\n'

    max_length=0
    for x in categories:
        if len(x.category)>max_length:
           max_length=len(x.category)
    for i in range(max_length):
        s+=' '*5
        for x in categories:
            if len(x.category)>i:
                s+=x.category[i]+'  '
            else:
                s+=' '*3
        s+='\n'
    return s[0:-1]