number = 10
if number > 0:
    print("The number is positive.")
else:
    print("The number is non-positive")

number = 0
if number > 0:
    print("The number is positive.")

elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"your grade is: {grade}")


x = 10
y = 5

if x > 0:
    if y > 0:
        print("Both x and y are positive.")

    else:
        print("x is positive, but y is negative") 

else:
    print("x is not positive.")




age = 20
status = "adult" if age  >= 18 else "minor"
print(status)

def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
    }
    return switcher.get(argument, "Invalid month")

print(switch_demo(2))
print(switch_demo(5))