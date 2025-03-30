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
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdQVDXe3Ph4VxPKPDRFm9g9dsj43WUcftUV9xmTPo4Y4adSXA/viewform')

# รอให้ฟอร์มโหลด
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

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
    '//span[text()="21 - 30 ปี"]',
    '//span[text()="31 - 40 ปี"]',
    '//span[text()="41 - 50 ปี"]',
    '//span[text()="50 ปีขึ้นไป"]'
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
    '//span[text()="ต่ำกว่าปริญญาตรี"]',
    '//span[text()="ปริญญาตรี"]',
    '//span[text()="สูงกว่าปริญญาตรี"]'
]
q4_choice = random.choice(q4_options)
q4_option = driver.find_element(By.XPATH, q4_choice)
q4_option.click()

# 5
q5_options = [ 
    '//span[text()="ต่ำกว่า 10,000 บาท"]',
    '//span[text()="10,001 - 20,000 บาท"]',
    '//span[text()="20,001 - 30,000 บาท"]',
    '//span[text()="30,001 - 40,000 บาท"]',
    '//span[text()="40,001 บาท ขึ้นไป"]'
]
q5_choice = random.choice(q5_options)
q5_option = driver.find_element(By.XPATH, q5_choice)
q5_option.click()

# next
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(2)

# 6
q6_options = [ 
    '//span[text()="น้อยกว่า 5 ปี"]',
    '//span[text()="6 - 10 ปี"]',
    '//span[text()="11 - 15 ปี"]',
    '//span[text()="16 - 20 ปี"]',
    '//span[text()="มากกว่า 21 ปีขึ้นไป"]'
]
q6_choice = random.choice(q6_options)
q6_option = driver.find_element(By.XPATH, q6_choice)
q6_option.click()

# 7
q7_options = [ 
    '//span[text()="ใช่"]',
    '//span[text()="ไม่ใช่"]'
]
q7_choice = random.choice(q7_options)
q7_option = driver.find_element(By.XPATH, q7_choice)
q7_option.click()

# 8
q9_options = [ 
    '//span[text()="น้อยกว่า 2 ครั้ง"]',
    '//span[text()="3 - 4 ครั้ง"]',
    '//span[text()="7 - 8 ครั้ง"]',
    '//span[text()="มากกว่า 9 ครั้ง"]'
]
q9_choice = random.choice(q9_options)
q9_option = driver.find_element(By.XPATH, q9_choice)
q9_option.click()

# 9
q8_options = [ 
    '//span[text()="ครอบครัว"]',
    '//span[text()="เพื่อนหรือคนรู้จัก"]',
    '//span[text()="สื่อโซเชียล"]',
    '//span[text()="ช่องทางโทรทัศน์"]'
]
q8_choice = random.choice(q8_options)
q8_option = driver.find_element(By.XPATH, q8_choice)
q8_option.click()
    


# 10
q10_options = [ 
    '//span[text()="เห็นด้วย"]',
    '//span[text()="ไม่เห็นด้วย"]'
]
q10_choice = random.choice(q10_options)
q10_option = driver.find_element(By.XPATH, q10_choice)
q10_option.click()

# 11
q11_options = [
    '//span[text()="Facebook"]',
    '//span[text()="เพื่อติดตามการแข่งขันทั้งในประเทศและระดับนานาชาติ"]',
    '//span[text()="Instagram"]',
    '//span[text()="x ( Twitter )"]',
    '//span[text()="TikTok"]',
    '//span[text()="YouTube"]'
]

num_choices = random.randint(1, len(q11_options)) 
choices_to_select = random.sample(q11_options, num_choices) 

for choice in choices_to_select:
    q11_option = driver.find_element(By.XPATH, choice)
    q11_option.click()
    
# 12
q12_options = [
    '//span[text()="รับชมเพื่อความสนุกสนาน"]',
    '//span[text()="คุณภาพของการแข่งขัน"]',
    '//span[text()="ความหลงใหลในการแข่งขัน English Premier League"]',
    '//span[text()="ความเคยชินที่ติดตามมานาน"]',
    '//span[text()="ติดตามเพื่อเข้าสังคมกับกลุ่มเพื่อน"]',
    '//span[text()="ติดตามเพื่อความผ่อนคลาย"]'
]

num_choices = random.randint(1, len(q12_options)) 
choices_to_select = random.sample(q12_options, num_choices) 

for choice in choices_to_select:
    q12_option = driver.find_element(By.XPATH, choice)
    q12_option.click()
    
# 13
q13_options = [
    '//span[text()="18:00 - 20:00"]',
    '//span[text()="20:00 - 22:00"]',
    '//span[text()="22:00 - 00:00"]',
    '//span[text()="00:00 - 02:00"]',
    '//span[text()="02:00 - 04:00"]'
]

num_choices = random.randint(1, len(q13_options)) 
choices_to_select = random.sample(q13_options, num_choices) 

for choice in choices_to_select:
    q13_option = driver.find_element(By.XPATH, choice)
    q13_option.click()
    
# 14
q14_options = [
    '//span[text()="ช่องทางโทรทัศน์"]',
    '//span[text()="ช่องทาง Streaming ถูกลิขสิทธิ์"]'
]

num_choices = random.randint(1, len(q14_options)) 
choices_to_select = random.sample(q14_options, num_choices) 

for choice in choices_to_select:
    q14_option = driver.find_element(By.XPATH, choice)
    q14_option.click()

# 15
q15_options = [
    '//span[text()="บ้าน"]',
    '//span[text()="ร้านอาหาร"]',
    '//span[text()="บ้านเพื่อน"]'
]

num_choices = random.randint(1, len(q15_options)) 
choices_to_select = random.sample(q15_options, num_choices) 

for choice in choices_to_select:
    q15_option = driver.find_element(By.XPATH, choice)
    q15_option.click()
    
# next
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