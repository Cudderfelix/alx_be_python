# Prompt user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% simple interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings: ${monthly_savings:.2f}")
print(f"Your projected annual savings with 5% interest: ${projected_annual_savings:.2f}")
