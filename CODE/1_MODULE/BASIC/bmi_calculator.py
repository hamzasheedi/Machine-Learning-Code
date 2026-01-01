def weight_calculator(user_weight, user_height, user_name):
    BMI = user_weight / (user_height ** 2)
    print(f"Your BMI is {BMI:.3f}")

    if BMI < 18.5:
        print(f"{user_name} is underweight")
    elif 18.5 <= BMI < 25:
        print(f"{user_name} has normal weight")
    elif 25 <= BMI < 30:
        print(f"{user_name} is overweight")
    else:  # BMI >= 30
        print(f"{user_name} is obese")


user_name = input("Enter your name: ")
user_height = float(input("Enter your height in meters: "))
user_weight = float(input("Enter your weight in kg: "))

weight_calculator(user_weight, user_height, user_name)
