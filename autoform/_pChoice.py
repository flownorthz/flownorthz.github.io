import pyperclip

# รับจำนวนตัวเลือกจากผู้ใช้
number = int(input("Number: "))  # เลขข้อ เช่น 3 -> q3
num_options = int(input("Enter the number of options: "))

# รับข้อความของแต่ละตัวเลือก
options = []
for i in range(1, num_options + 1):
    choice_text = input(f"Enter text for choice {i}: ").strip()
    if choice_text:  # ตรวจสอบว่าไม่ใช่ค่าว่าง
        options.append(f"//span[text()=\"{choice_text}\"]")

# สร้างตัวแปรตามหมายเลขที่ผู้ใช้ระบุ
q_var = f"q{number}"

# สร้างโค้ดที่ต้องการคัดลอก
generated_code = f"#-------- ข้อ {number} --------\n"
generated_code += f"{q_var}_options = [\n"
for i, option in enumerate(options):
    comma = "," if i < len(options) - 1 else ""  # เพิ่ม ',' เว้นแต่เป็นตัวสุดท้าย
    generated_code += f"    '{option}'{comma}\n"
generated_code += "]\n\n"
generated_code += f"{q_var}_choice = random.choice({q_var}_options)\n"
generated_code += f"{q_var}_option = driver.find_element(By.XPATH, {q_var}_choice)\n"
generated_code += f"{q_var}_option.click()\n"


# คัดลอกไปยังคลิปบอร์ด
pyperclip.copy(generated_code)

# แสดงผลลัพธ์
print("---------")
print("โค้ดถูกคัดลอกไปยังคลิปบอร์ดแล้ว! 🎉")
print(generated_code)




