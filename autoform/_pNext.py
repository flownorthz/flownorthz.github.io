import pyperclip

code = """
#----- Next -----
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(2)
"""

pyperclip.copy(code)  # คัดลอกข้อความไปยังคลิปบอร์ด
print("---------")
print("โค้ดถูกคัดลอกไปยังคลิปบอร์ดแล้ว! 🎉")
