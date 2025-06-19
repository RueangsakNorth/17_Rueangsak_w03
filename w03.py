# BMI Calculator
# Result: BMI = weight / (height ** 2)
try:
     w = float(input("Enter your weight in kg: "))
     if w < 0:
        print("น้ำหนักต้องเป็นจำนวนบวก")
     else:
        print(f"น้ำหนักที่ตั้งค่า: {w} Kg")
except ValueError:
    print("กรุณาใส่ตัวเลขเท่านั้น")
    
try:
    h = float(input("Enter your height in centimeters: "))
    if h < 0:
        print("น้ำหนักต้องเป็นจำนวนบวก")
    else:
        print(f"น้ำหนักที่ตั้งค่า: {h} cm")
except ValueError:
    print("กรุณาใส่ตัวเลขเท่านั้น")
    
   
# Convert height from centimeters to meters 
r = w / ((h/100) ** 2)
# Print the result
# print(f"Your BMI is: {r:.2f}")