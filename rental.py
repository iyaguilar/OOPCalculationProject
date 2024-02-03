# rental.py
class Rental:
    def __init__(self, purchase_price, total_investment, annual_rental_income, annual_expenses):
        self.purchase_price = purchase_price
        self.total_investment = total_investment
        self.annual_rental_income = annual_rental_income
        self.annual_expenses = annual_expenses

    def calculate_cash_flow(self):
        return self.annual_rental_income - self.annual_expenses

    def calculate_roi(self):
        cash_flow = self.calculate_cash_flow()
        return (cash_flow / self.total_investment) * 100