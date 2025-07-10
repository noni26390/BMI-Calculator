# Write Python 3 code in t# BMI calculator

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meter:"))

BMI = weight / (height ** 2)

print(BMI)

if BMI < 18.5:
    print("get some gains, you are slim and not fit.")
    
elif 18.5 <= BMI < 24.9:
    print("CONGRATS, You have healthy body")
    
else: 
    print("you fat ass.")
