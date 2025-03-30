import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import time

start_time = datetime.now()

link = ("https://docs.google.com/forms/d/e/1FAIpQLSePlrfKo8IHg8bcgnRo9v77aYuqgY0lKtAv-orqA--lOgIZBw/viewform")

# กำหนด path ของ WebDriver (เช่น ChromeDriver)
driver_path = r'C:\Windows\chromedriver.exe'

# ใช้ Service ในการกำหนด path ของ chromedriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# เปิด Google Form
driver.get(link)

# รอให้ฟอร์มโหลด
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))


#----- Next -----
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(2)

#-------- ข้อ 1 --------
q1_options = [
    '//span[text()="ชาย"]',
    '//span[text()="หญิง"]',
    '//span[text()="LGBTQ"]'
]

q1_choice = random.choice(q1_options)
q1_option = driver.find_element(By.XPATH, q1_choice)
q1_option.click()

#-------- ข้อ 2 --------
q2_options = [
    '//span[text()="น้อยกว่า 20 ปี"]',
    '//span[text()="21-30 ปี"]',
    '//span[text()="31-40 ปี"]',
    '//span[text()="41-50 ปี"]',
    '//span[text()="มากกว่า 50 ปีขึ้นไป"]'
]

q2_choice = random.choice(q2_options)
q2_option = driver.find_element(By.XPATH, q2_choice)
q2_option.click()
#-------- ข้อ 3 --------
q3_options = [
    '//span[text()="โสด"]',
    '//span[text()="สมรส"]',
    '//span[text()="หย่าร้าง"]',
    '//span[text()="หม้าย"]'
]

q3_choice = random.choice(q3_options)
q3_option = driver.find_element(By.XPATH, q3_choice)
q3_option.click()
#-------- ข้อ 4 --------
q4_options = [
    '//span[text()="ต่ำกว่าปริญญาตรี"]',
    '//span[text()="ปริญญาตรี"]',
    '//span[text()="สูงกว่าปริญญาตรี"]'
]

q4_choice = random.choice(q4_options)
q4_option = driver.find_element(By.XPATH, q4_choice)
q4_option.click()
#-------- ข้อ 5 --------
q5_options = [
    '//span[text()="ต่ำกว่า 10,000 บาท"]',
    '//span[text()="10,001-20,000 บาท"]',
    '//span[text()="20,001-30,000 บาท"]',
    '//span[text()="30,001-40,000 บาท"]',
    '//span[text()="40,001 บาทขึ้นไป"]'
]

q5_choice = random.choice(q5_options)
q5_option = driver.find_element(By.XPATH, q5_choice)
q5_option.click()
#-------- ข้อ 6 --------
q6_options = [
    '//span[text()="นักเรียน / นักศึกษา"]',
    '//span[text()="ธุรกิจส่วนตัว"]',
    '//span[text()="ข้าราชการ"]',
    '//span[text()="รัฐวิสาหกิจ"]',
    '//span[text()="พนักงานบริษัท"]'
]

q6_choice = random.choice(q6_options)
q6_option = driver.find_element(By.XPATH, q6_choice)
q6_option.click()

#----- Next -----
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(2)

#-------- ข้อ 7 --------
q7_options = [
    '//span[text()="ครอบครัว"]',
    '//span[text()="เพื่อนหรือคนรู้จัก"]',
    '//span[text()="สื่ออินเทอร์เน็ต"]'
]

q7_choice = random.choice(q7_options)
q7_option = driver.find_element(By.XPATH, q7_choice)
q7_option.click()

#-------- ข้อ 8 --------
q8_options = [
    '//*[@id="i23"]/div[3]/div',
    '//*[@id="i26"]/div[3]/div',
    '//*[@id="i29"]/div[3]/div'
]

# Randomly choose an XPath and click on it
chosen_xpath = random.choice(q8_options)
q8_options = driver.find_element(By.XPATH, chosen_xpath)
q8_options.click()

#-------- ข้อ 9 --------
q9_options = [
    '//span[text()="ใช่"]',
    '//span[text()="ไม่ใช่"]'
]

q9_choice = random.choice(q9_options)
q9_option = driver.find_element(By.XPATH, q9_choice)
q9_option.click()
#-------- ข้อ 10 --------
q10_options = [
    '//span[text()="06.01 – 12.00 น."]',
    '//span[text()="12:01 – 18.00 น."]',
    '//span[text()="18.01 – 0.00 น."]',
    '//span[text()="0.01 – 6.00 น."]'
]

q10_choice = random.choice(q10_options)
q10_option = driver.find_element(By.XPATH, q10_choice)
q10_option.click()
#-------- ข้อ 11 --------
q11_options = [
    '//span[text()="1 ครั้ง/สัปดาห์"]',
    '//span[text()="2 ครั้ง/สัปดาห์"]',
    '//span[text()="3 ครั้ง/สัปดาห์"]',
    '//span[text()="มากกว่า 4 ครั้ง/สัปดาห์"]'
]

q11_choice = random.choice(q11_options)
q11_option = driver.find_element(By.XPATH, q11_choice)
q11_option.click()
#-------- ข้อ 12 --------
q12_options = [
    '//span[text()="ตั้งแต่ต้นจนจบรายการ"]',
    '//span[text()="เกือบทั้งหมดของรายการ ( ประมาณ 1 ชั่วโมง )"]',
    '//span[text()="ประมาณครึ่งรายการ ( ประมาณ 45 นาที )"]',
    '//span[text()="น้อยกว่าครึ่งรายการ ( ประมาณ 30 นาที )"]',
    '//span[text()="เพียงส่วนน้อยของรายการ ( ประมาณ 10 นาที )"]'
]

q12_choice = random.choice(q12_options)
q12_option = driver.find_element(By.XPATH, q12_choice)
q12_option.click()
#-------- ข้อ 13 --------
q13_options = [
    '//span[text()="ตั้งใจรับชมตลอดทั้งรายการ"]',
    '//span[text()="เลือกรับชมเฉพาะช่วงที่สนใจ"]',
    '//span[text()="ชมเรื่อยๆ ตั้งใจบ้างเป็นบางครั้ง"]',
    '//span[text()="เปิดทิ้งไว้เป็นเพื่อน"]'
]

q13_choice = random.choice(q13_options)
q13_option = driver.find_element(By.XPATH, q13_choice)
q13_option.click()
#-------- ข้อ 14 --------
q14_options = [
    '//span[text()="เพื่อติดตามข่าวสารของฟุตบอลไทย"]',
    '//span[text()="เพื่อทราบข้อมูลของนักฟุตบอล"]',
    '//span[text()="เพื่อติดตามโปรแกรมการแข่งขัน"]',
    '//span[text()="เพื่อทราบผลการแข่งขัน"]',
    '//span[text()="เพื่อพูดคุยแลกเปลี่ยนความคิดเห็น"]',
    '//span[text()="เพื่อความบันเทิงและผ่อนคลาย"]'
]

num_choices = random.randint(1, len(q14_options))
choices_to_select = random.sample(q14_options, num_choices)

for choice in choices_to_select:
    q14_option = driver.find_element(By.XPATH, choice)
    q14_option.click()
#-------- ข้อ 15 --------
q15_options = [
    '//span[text()="เนื้อหาเกี่ยวกับฟุตบอลไทยน่าสนใจ"]',
    '//span[text()="สไตล์การดำเนินรายการของพิธีกร"]',
    '//span[text()="การอัปเดตข้อมูลที่รวดเร็ว"]',
    '//span[text()="ความสนุกความบันเทิง"]'
]

num_choices = random.randint(1, len(q15_options))
choices_to_select = random.sample(q15_options, num_choices)

for choice in choices_to_select:
    q15_option = driver.find_element(By.XPATH, choice)
    q15_option.click()
#-------- ข้อ 16 --------
q16_options = [
    '//span[text()="กดติดตามช่องตูดูบอลไทย"]',
    '//span[text()="กดไลค์วิดีโอของรายการ"]',
    '//span[text()="ส่งคำถามหรือข้อความในช่วงไลฟ์สด"]',
    '//span[text()="แสดงความคิดเห็นใต้คลิปของรายการ"]',
    '//span[text()="แชร์วิดีโอของรายการไปยังโซเซียลมีเดีย"]'
]

num_choices = random.randint(1, len(q16_options))
choices_to_select = random.sample(q16_options, num_choices)

for choice in choices_to_select:
    q16_option = driver.find_element(By.XPATH, choice)
    q16_option.click()

#----- Next -----
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(2)


#-------------------------------------------------------#
# ค้นหาตัวเลือกทั้งหมดของข้อที่ 1
a = 2

for _ in range(19):
    # Randomly choose a value for c between 0 and 3
    c = random.randint(1, 4) 
    
    # Construct the XPath with the variables a and c
    options_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[{a}]/span/div[{c}]/div/div/div'
    
    # Find the options using the XPath
    options = driver.find_elements(By.XPATH, options_xpath)

    # ตรวจสอบว่ามีตัวเลือกหรือไม่
    if options:
        # เลือกตัวเลือกแบบสุ่มหลายตัว (ตัวอย่างเลือก 3 ตัว)
        random_choices = random.sample(options, 3)  # เลือก 3 ตัวจากตัวเลือกทั้งหมด
        for choice in random_choices:
            ActionChains(driver).move_to_element(choice).click().perform()  # คลิกแต่ละตัวเลือก
        a += 2  # เพิ่มค่า a ทีละ 2
    else:
        pass

#-------------------------------------------------------#
# ค้นหาตัวเลือกทั้งหมดของข้อที่ 2
a = 2

for _ in range(19):
    # Randomly choose a value for c between 0 and 3
    c = random.randint(1, 4)  
    
    # Construct the XPath with the variables a and c
    options_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[{a}]/span/div[{c}]/div/div/div'
    
    # Find the options using the XPath
    options = driver.find_elements(By.XPATH, options_xpath)

    # ตรวจสอบว่ามีตัวเลือกหรือไม่
    if options:
        # เลือกตัวเลือกแบบสุ่มหลายตัว (ตัวอย่างเลือก 3 ตัว)
        random_choices = random.sample(options, 3)  # เลือก 3 ตัวจากตัวเลือกทั้งหมด
        for choice in random_choices:
            ActionChains(driver).move_to_element(choice).click().perform()  # คลิกแต่ละตัวเลือก
        a += 2  # เพิ่มค่า a ทีละ 2
    else:
        pass

#-------------------------------------------------------#
# ค้นหาตัวเลือกทั้งหมดของข้อที่ 3
a = 2
b = 1

for _ in range(19):
    # Randomly choose a value for c between 0 and 3
    c = random.randint(1, 4)  
    

    b = b+1
    # Construct the XPath with the variables a and c
    options_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[{a}]/span/div[{c}]/div/div/div'
    
    # Find the options using the XPath
    options = driver.find_elements(By.XPATH, options_xpath)

    # ตรวจสอบว่ามีตัวเลือกหรือไม่
    if options:
        # เลือกตัวเลือกแบบสุ่มหลายตัว (ตัวอย่างเลือก 3 ตัว)
        random_choices = random.sample(options, 3)  # เลือก 3 ตัวจากตัวเลือกทั้งหมด
        for choice in random_choices:
            ActionChains(driver).move_to_element(choice).click().perform()  # คลิกแต่ละตัวเลือก
        a += 2  # เพิ่มค่า a ทีละ 2
    else:
        pass


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


