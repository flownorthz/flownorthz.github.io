import pyperclip

code = """
# รอจนกว่าปุ่มส่งจะปรากฏ
submit_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="ส่ง"]'))
)

# คลิกปุ่มส่ง
submit_button.click()

# ตรวจสอบว่าปุ่มส่งยังอยู่หรือไม่หลังจากคลิก
try:
    WebDriverWait(driver, 5).until_not(
        EC.presence_of_element_located((By.XPATH, '//span[text()="ส่ง"]'))
    )
    print("ส่งข้อมูลสำเร็จ")
except:
    print("ปุ่มส่งยังคงอยู่ อาจไม่ได้กดสำเร็จหรือมีปัญหา")

# ปิดเบราว์เซอร์
driver.quit()

end_time = datetime.now()
ftime = int((end_time - start_time).total_seconds())

print("--------------")
print(f"ใช้เวลาทำฟอร์มไป {ftime} วินาที")

"""

pyperclip.copy(code)  # คัดลอกข้อความไปยังคลิปบอร์ด
print("---------")
print("โค้ดถูกคัดลอกไปยังคลิปบอร์ดแล้ว! 🎉")
