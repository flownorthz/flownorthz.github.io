import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# กำหนด path ของ WebDriver (เช่น ChromeDriver)
driver_path = r'C:\Windows\chromedriver.exe'

# ใช้ Service ในการกำหนด path ของ chromedriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# เปิด Google Form
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdoFZwSF3tvOrRyjzU5rlQa_c-6THlnIcP0R04TUfeDITKcUA/viewform')

# รอให้ฟอร์มโหลด
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

'''
# ย้ายไปที่จอที่ 3 (กำหนดพิกัดเอง)
screen_x = -1300  # ปรับตามตำแหน่งจอที่ 3 ของคุณ
screen_y = 150
driver.set_window_position(screen_x, screen_y)

# ปรับขนาดหน้าต่างให้เหมาะสม
driver.set_window_size(1280, 720)  # หรือขนาดที่ต้องการ
'''



# next
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(2)

# 1
q1_options = [ 
    '//span[text()="ชาย"]',
    '//span[text()="หญิง"]',
    '//span[text()="LGBTQ+"]'
]
q1_choice = random.choice(q1_options)
q1_option = driver.find_element(By.XPATH, q1_choice)
q1_option.click()

# 2
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

# 3
q3_options = [ 
    '//span[text()="โสด"]',
    '//span[text()="สมรส"]',
    '//span[text()="หย่าร้าง"]',
    '//span[text()="หม้าย"]'
]
q3_choice = random.choice(q3_options)
q3_option = driver.find_element(By.XPATH, q3_choice)
q3_option.click()

# 4
q4_options = [ 
    '//span[text()="นักเรียน/นักศึกษา"]',
    '//span[text()="พนักงานบริษัทเอกชน"]',
    '//span[text()="ข้าราชการ"]',
    '//span[text()="ธุรกิจส่วนตัว"]'
]
q4_choice = random.choice(q4_options)
q4_option = driver.find_element(By.XPATH, q4_choice)
q4_option.click()

# 5
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

# next
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(1)

# 6
q6_options = [ 
    '//span[text()="ต่ำกว่า 1 ครั้งต่อสัปดาห์"]',
    '//span[text()="1 ครั้งต่อสัปดาห์"]',
    '//span[text()="2-3 ครั้งต่อสัปดาห์"]',
    '//span[text()="4-5 ครั้งต่อสัปดาห์"]'
]
q6_choice = random.choice(q6_options)
q6_option = driver.find_element(By.XPATH, q6_choice)
q6_option.click()

# 7
q7_options = [ 
    '//span[text()="True Premier Football HD"]',
    '//span[text()="แอป TrueID"]',
    '//span[text()="เว็บไซต์ TrueVisions"]',
    '//span[text()="เว็บไซต์ใน Google"]'
]
q7_choice = random.choice(q7_options)
q7_option = driver.find_element(By.XPATH, q7_choice)
q7_option.click()

# 8 
q8_options = [
    '//span[text()="ความเสถียรในการรับชม"]',
    '//span[text()="มีการวิเคราะห์และบอกสถิติระหว่างเกม"]',
    '//span[text()="ง่ายต่อการเลือกชม"]',
    '//span[text()="ความละเอียดของภาพมีคุณภาพที่สูง"]'
]

num_choices = random.randint(1, len(q8_options)) 
choices_to_select = random.sample(q8_options, num_choices) 

for choice in choices_to_select:
    q8_option = driver.find_element(By.XPATH, choice)
    q8_option.click()

# 9
q9_options = [ 
    '//span[text()="แพ็กเกจรายเดือน"]',
    '//span[text()="แพ็กเกจรายปี"]',
    '//span[text()="ดูผ่านโปรโมชั่นหรือแพ็กเกจเสริม"]',
    '//span[text()="ไม่ได้สมัครแพ็กเกจพิเศษ"]'
]
q9_choice = random.choice(q9_options)
q9_option = driver.find_element(By.XPATH, q9_choice)
q9_option.click()

# 10
q10_options = [ 
    '//span[text()="โทรทัศน์"]',
    '//span[text()="สมาร์ตโฟน / แท็บเล็ต"]',
    '//span[text()="คอมพิวเตอร์ / โน้ตบุ๊ก"]',
    '//span[text()="อุปกรณ์สตรีมมิ่ง (เช่น Chromecast, Apple TV)"]'
]
q10_choice = random.choice(q10_options)
q10_option = driver.find_element(By.XPATH, q10_choice)
q10_option.click()

# next
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(1)

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
#-------------------------------------------------------#
# ค้นหาตัวเลือกทั้งหมดของข้อที่ 4
a = 2
b = 1

for _ in range(19):
    # Randomly choose a value for c between 0 and 3
    c = random.randint(1, 4)  
    

    b = b+1
    # Construct the XPath with the variables a and c
    options_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[{a}]/span/div[{c}]/div/div/div'
    
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
    
print("----------")

# รอจนกว่าปุ่มส่งจะปรากฏ
submit_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="ส่ง"]'))
)
submit_button.click()

# ปิดเบราว์เซอร์
driver.quit()