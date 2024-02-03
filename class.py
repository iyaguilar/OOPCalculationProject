# class.py
from rental import Rental 

if __name__ == "__main__":
    # Input values for a rental property
    purchase_price = float(input("Enter the purchase price of the property: $"))
    total_investment = float(input("Enter the total investment amount: $"))
    annual_rental_income = float(input("Enter the annual rental income: $"))
    annual_expenses = float(input("Enter the annual expenses: $"))



    # Create an instance of Rental
    rental_property = Rental(purchase_price, total_investment, annual_rental_income, annual_expenses)

    # Accessing instance attributes
    print(f"Purchase Price: ${rental_property.purchase_price}")
    print(f"Total Investment: ${rental_property.total_investment}")
    print(f"Annual Rental Income: ${rental_property.annual_rental_income}")
    print(f"Annual Expenses: ${rental_property.annual_expenses}")

    # Calculate and print the cash flow and ROI
    cash_flow = rental_property.calculate_cash_flow()
    roi = rental_property.calculate_roi()

    print(f"Annual Cash Flow: ${cash_flow}")
    print(f"Return on Investment (ROI): {roi:.2f}%")