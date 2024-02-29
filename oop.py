#oop.py

class Rental:
    def __init__(self, purchase_price, 
                total_investment, annual_rental_income,
                annual_expenses, mortgage):
        self.purchase_price = purchase_price
        self.total_investment = total_investment
        self.annual_rental_income = annual_rental_income
        self.annual_expenses = annual_expenses
        self.mortgage=mortgage

    def calculate_cash_flow(self):
        return self.annual_rental_income - self.annual_expenses

    def calculate_roi(self):
      return (self.calculate_cash_flow() / self.total_investment) * 100
    
if __name__ == "__main__":
    purchase_price = int(input('Put purchase price here: '))
    total_investment = int(input('Put total investment here: '))
    annual_rent = int(input('Put annual rent here: '))
    expenses = int(input('Put expenses here: '))
    mortgage = int(input('Put mortgage here: '))

rental_property = Rental(purchase_price,total_investment, annual_rent, expenses, mortgage)
    
print(f"Purchase Price: ${rental_property.purchase_price}")
print(f"Total Investment: ${rental_property.total_investment}")
print(f"Annual Rental Income: ${rental_property.annual_rental_income}")
print(f"Annual Expenses: ${rental_property.annual_expenses}")


cash_flow = rental_property.calculate_cash_flow()
roi = rental_property.calculate_roi()

print(f"Annual Cash Flow: ${cash_flow}")
print(f"Return on Investment (ROI): {roi:.2f}%")





 
