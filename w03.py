# BMI Calculator
# Result: BMI = weight / (height ** 2)

try:
    w= input("Enter your weight in kg: ")
    h= input("Enter your height in centimeters: ")

    # ตรวจสอบว่าเป็นตัวเลขหรือไม่
    if not (w.replace('.', '', 1).isdigit() or (w.startswith('-') and w.replace('.', '', 1).isdigit())) or \
       not (h.replace('.', '', 1).isdigit() or (h.startswith('-') and h[1:].replace('.', '', 1).isdigit())):
        raise ValueError # ถ้าไม่ใช่ตัวเลข ให้ส่งไปที่ except block

    w = float(w) # แปลงน้ำหนักเป็น float
    h = float(h) # แปลงส่วนสูงเป็น float

    if w <= 0 or h <= 0: # ตรวจสอบว่าเป็นค่าบวก
        print("ป้อนข้อมูลเป็นจำนวนบวกและมากกว่าศูนย์")
    else:
        print(f"น้ำหนักที่ตั้งค่า: {w} Kg")
        print(f"ส่วนสูงที่ตั้งค่า: {h} cm") # เพิ่มการแสดงส่วนสูงที่ตั้งค่า
        r = w / ((h / 100) ** 2)
        print(f"Your BMI is: {r:.2f}")

except ValueError:
    print("กรุณากรอกข้อมูลใหม่ให้ถูกต้อง")