# Tax Calculator Program
def calculate_tax(income):
    if income <= 2000:
        tax_rate = 0.0
    elif income <= 4000:
        tax_rate = 0.15
    elif income <= 7000:
        tax_rate = 0.20
    elif income <= 10000:
        tax_rate = 0.25
    elif income <= 14000:
        tax_rate = 0.30
    else:
        tax_rate = 0.35
    total_tax = income * tax_rate
    net_income = income - total_tax

    return total_tax, net_income

income = float(input("Enter your income amount: "))

tax, net = calculate_tax(income)

print(f"\nYour total tax: ${tax:.2f}")
print(f"Your net income after tax: ${net:.2f}")
