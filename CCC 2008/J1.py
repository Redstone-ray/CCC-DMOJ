index = float(input()) / (float(input()) ** 2)
if index < 18.5:
    print("Underweight")
elif index <= 25.0:
    print("Normal weight")
else:
    print("Overweight")