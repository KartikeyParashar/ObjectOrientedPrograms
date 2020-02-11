class Stocks:
    """This class contains info about the stocks owned by an individual
    """

    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number


class Portfolio:
    """This class contains methods for creating a portfolio for stock account
    """

    def __init__(self):
        self.value = 0
        self.portfolio = []

    def enter_stock(self, name, price, number):
        """This method adds new account in the portfolio
        Parameters:
            name: name of the individual
            price: price of the stocks
            number: no. of shares purchased
        """
        new_stock = Stocks(name, price, number)
        self.portfolio.append(new_stock)

    def portfolio_details(self):
        """This method calculates the total value of the stocks
        """
        for obj in self.portfolio:
            print(f"{obj.name}:\n\tPrice per share: {obj.price}\n\t"
                  f"Number of Shares: {obj.number}\n\tValue: {obj.price*obj.number}\n.")

    def portfolio_total(self):
        """This method iterates through the portfolio and calculates the stock value"""
        for obj in self.portfolio:
            self.value += obj.number * obj.price


port = Portfolio()
port.enter_stock("Infosys", 50000, 550)
port.enter_stock("TCS", 65000, 350)
port.portfolio_details()
port.portfolio_total()
print("Total portfolio value = ", port.value)
