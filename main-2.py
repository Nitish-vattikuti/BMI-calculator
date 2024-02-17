# BMI CALCULATOR

# ask user to enter weight in kg
weight = float(input("Enter your weight in kg : "))
#ask user to enter height in m
height = float(input("Enter your height in m : "))
# calculate BMI
BMI = weight / (height ** 2)
#print BMI
print("Your BMI is : ", BMI)
# if BMI is less than 18.5 print
if(BMI < 18.5):
  print("You are underweight")
if(BMI >= 18.5 and BMI <= 24.9):
  print("You are normal")
if(BMI >= 25 and BMI <= 29.9):
  print("your are overweight")
if(BMI > 30):
  print("You are obese")