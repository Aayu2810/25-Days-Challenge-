import matplotlib.pyplot as plt

# Main data
monthly_income: float = 10000
rent: float = 1000
food: float = 2500
tax_rate: float = 0.22
taxes: float = monthly_income * tax_rate
other_expenses: float = 2000

# Yearly
yearly_income: float = monthly_income * 12
yearly_expenses: float = sum([rent, food, taxes, other_expenses]) * 12
yearly_savings: float = yearly_income - yearly_expenses

# Prepare data for plotting
monthly_categories: list[str] = ['Income', 'Rent', 'Food', 'Taxes', 'Other']
monthly_amounts: list[float] = [monthly_income, rent, food, taxes, other_expenses]
monthly_colors: list[str] = ['green', 'red', 'red', 'red', 'red']
yearly_categories: list[str] = ['Income', 'Expenses', 'Savings']
yearly_amounts: list[float] = [yearly_income, yearly_expenses, yearly_savings]
yearly_colors: list[str] = ['green', 'red', 'green']

# Create subplots (1 row, 2 columns) -
# set up the figure with two side-by-side charts
fig, axs = plt.subplots(1, 2, figsize=(10, 6))

# Monthly bar chart
axs[0].bar(monthly_categories, monthly_amounts, color=monthly_colors)
axs[0].set_title('Monthly Financial Overview')
axs[0].set_ylabel('Amount ($)')
axs[0].tick_params(axis='x', rotation=45)

# Yearly bar chart
axs[1].bar(yearly_categories, yearly_amounts, color=yearly_colors)
axs[1].set_title('Yearly Financial Overview')
axs[1].set_ylabel('Amount ($)')

# Adjust layout and display
plt.tight_layout()  # Makes sure that the labels will fit and not overlap
plt.show()
