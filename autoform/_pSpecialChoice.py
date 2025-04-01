import pyperclip
import random

# รับค่าหมายเลขคำถาม
number = int(input("Number: "))  # เลขข้อ เช่น 8 -> q8
num_options = int(input("Enter the number of options: "))  # จำนวนตัวเลือก
start_xpath = int(input("Enter the starting XPath number: "))  # XPath เริ่มต้น เช่น 23

# สร้างรายการ XPath โดยเพิ่มทีละ 3
options = [f"'//*[@id=\"i{start_xpath + (i * 3)}\"]/div[3]/div'" for i in range(num_options)]

# ชื่อของตัวแปรตามหมายเลขที่ระบุ
q_var = f"q{number}"

# สร้างโค้ดที่ต้องการคัดลอก
generated_code = f"#-------- ข้อ {number} --------\n"
generated_code += f"{q_var}_options = [\n"
generated_code += ",\n".join(f"    {option}" for option in options)
generated_code += "\n]\n\n"
generated_code += f"# Randomly choose an XPath and click on it\n"
generated_code += f"chosen_xpath = random.choice({q_var}_options)\n"
generated_code += f"{q_var}_option = driver.find_element(By.XPATH, chosen_xpath)\n"
generated_code += f"{q_var}_option.click()\n"

# คัดลอกไปยังคลิปบอร์ด
pyperclip.copy(generated_code)

# แสดงผลลัพธ์
print("---------")
print("โค้ดถูกคัดลอกไปยังคลิปบอร์ดแล้ว! 🎉")
print(generated_code)
