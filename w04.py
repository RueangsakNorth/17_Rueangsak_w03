#  Error Handling Example
try:
    frequency = float(input("Enter frequency (MHz):"))
    if frequency < 0:
        print("ความถี่ต้องเป็นจำนวนบวก")
    else:
        print(f"ความถี่ที่ตั้งค่า: {frequency} MHz")
except ValueError:
    print("กรุณาใส่ตัวเลขเท่านั้น")