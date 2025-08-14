frst = input("Enter first number: ")
second = input("Enter second number: ")

total_sum = float(first) + float(second)
print("The sum of the two numbers is: ", total_sum, "'\n'First:", first, "'\n'Second:", second)

#mosh boys, mana
temperature = float(input("Enter temperature in Celsisus:"))
# This helps evaluate the current temperature and gives an advisory answer.
if temperature > 45:
    print("Current temperature is hot, please make sure to stay hydrated at all times.")
elif temperature < 30 and temperature > 10:
    print("Current temperature is moderate, you can wear loose clothes if suitable.")
else: 
    print("Current temperature is super cold, please wear enough clothes to mitigate against the cold weather.")
print("Thank you for using the fahreneit calc to check temp")

weight = float(input("Please enter your weight:"))
conversion_term =input("Please specify if weight is in '(L)bs' or in '(K)gs':")

if conversion_term == 'L' or conversion_term == 'l':
    print("Your body weight is:", weight, "Kg")
elif conversion_term =='K' or conversion_term == 'k':
    print("Your body weight is:", weight, "Lbs" )
else:
    print("Please enter a valid weight parameter, either 'L' or 'K'.")
