# Task 1: Validating Calculations Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.

expression_1 =   7 * 6/2 * 2 + 1

expression_2 =  7 * 6/(2 * 2) + 1

print("expression1 =", expression_1)
print("expression2 =",expression_2)

print("=" *50)
#============================================#

# Task 2: Mix and Match Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct.


predict = int(input("Enter a lucky number: "))

lucky_num = predict > 56+2 or predict<11


if lucky_num == True:
    print("Lucky Charms!")
else:
    print("Not so lucky!")

