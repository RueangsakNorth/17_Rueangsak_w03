# แยกข้อความม
radio_data = "hs1acb,14.234,100,USB,Nolmal"
#  แยกข้อความมาเป็น list
parts = radio_data.split(',')
# # 0 1 2 3 4
call_sign =(f"นามเรียนขาน : { str ,parts[0]}")
# Call sign
frequency = float(parts[1])  
# Frequency in MHz
Power = (int ,parts[2])  
# Power in watts
mode = {str ,parts[3]}  
# Mode of operation
status = {str ,parts[4]} 
# status of the radio
print(call_sign)