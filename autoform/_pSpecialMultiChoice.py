import pyperclip
import random

# รับค่าหมายเลขคำถาม
number = int(input("Number: "))  # เลขข้อ เช่น 13 -> q13
num_options = int(input("Enter the number of options: "))  # จำนวนตัวเลือก
start_xpath = int(input("Enter the starting XPath number: "))  # XPath เริ่มต้น เช่น 161

# สร้างรายการ XPath โดยเพิ่มทีละ 3
options = [f"'//*[@id=\"i{start_xpath + (i * 3)}\"]/div[2]'" for i in range(num_options)]

# ชื่อของตัวแปรตามหมายเลขที่ระบุ
q_var = f"q{number}"

# สร้างโค้ดที่ต้องการคัดลอก
generated_code = f"#-------- ข้อ {number} --------\n"
generated_code += f"{q_var}_xpaths = [\n"
generated_code += ",\n".join(f"    {option}" for option in options)
generated_code += "\n]\n\n"
generated_code += f"# สุ่มเลือกจำนวนตัวเลือกที่ต้องการคลิก\n"
generated_code += f"num_choices = random.randint(1, len({q_var}_xpaths))\n"
generated_code += f"choices_to_select = random.sample({q_var}_xpaths, num_choices)\n\n"
generated_code += f"# คลิกตัวเลือกที่สุ่มได้\n"
generated_code += f"for xpath in choices_to_select:\n"
generated_code += f"    element = driver.find_element(By.XPATH, xpath)\n"
generated_code += f"    element.click()\n"

# คัดลอกไปยังคลิปบอร์ด
pyperclip.copy(generated_code)

# แสดงผลลัพธ์
print("---------")
print("โค้ดถูกคัดลอกไปยังคลิปบอร์ดแล้ว! 🎉")
print(generated_code)
