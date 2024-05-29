# Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic

gallon_milk = 2.51
dozen_eggs = 1.88
case_waters = 5.98

total = gallon_milk + dozen_eggs + case_waters

print ("The total cost for a gallon of milk, dozen of eggs & a case of waters:",round(total, 2))

#============================================#

# Task 2: Bank Interest (Extra Credit) If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

initial_balance = 7000
yearly_rate = .06

eoy_balance = (initial_balance * yearly_rate) + initial_balance

print("The end of year balance for an account with an initial balance of $7000 and an interest rate of 6% would be:",eoy_balance)
