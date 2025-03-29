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
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScF9087eHHi0XFelkX_ac6VcoJW53rWG-NiHsZl_tcZm5Oxhg/viewform')

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
    '//span[text()="ต่ำกว่า 12 ปี"]',
    '//span[text()="13 - 18 ปี"]',
    '//span[text()="19 - 24 ปี"]',
    '//span[text()="25 - 29 ปี"]',
    '//span[text()="30 ปีขึ้นไป"]'
]
q2_choice = random.choice(q2_options)
q2_option = driver.find_element(By.XPATH, q2_choice)
q2_option.click()

# 3
q3_options = [ 
    '//span[text()="นักเรียน/นักศึกษา"]',
    '//span[text()="ข้าราชการ"]',
    '//span[text()="พนักงานบริษัท"]',
    '//span[text()="ธุรกิจส่วนตัว"]'
]
q3_choice = random.choice(q3_options)
q3_option = driver.find_element(By.XPATH, q3_choice)
q3_option.click()

# 4
q4_options = [ 
    '//span[text()="เพื่อนหรือคนรู้จัก"]',
    '//span[text()="โฆษณาออนไลน์"]',
    '//span[text()="สื่อสังคมออนไลน์"]'
]
q4_choice = random.choice(q4_options)
q4_option = driver.find_element(By.XPATH, q4_choice)
q4_option.click()

# 5
q5_options = [ 
    '//span[text()="Facebook"]',
    '//span[text()="YouTube"]',
    '//span[text()="TikTok"]',
    '//span[text()="เว็บไซต์เกม"]',
    '//span[text()="กลุ่มออนไลน์ที่เกี่ยวกับข้องกับ RoV "]'
]
q5_choice = random.choice(q5_options)
q5_option = driver.find_element(By.XPATH, q5_choice)
q5_option.click()


# 6
q6_options = [
    '//span[text()="ข่าวสารสำคัญและการอัปเดต"]',
    '//span[text()="ข่าวสารสตรีมสดและถ่ายทอดสด"]',
    '//span[text()="ข่าวสารเทคนิคและเคล็ดลับการเล่น"]',
    '//span[text()="ข่าวสารการแข่งขันและกิจกรรม"]',
    '//span[text()="ข่าวสารประเด็นน่าสนใจที่มีการถกเถียง"]',
    '//span[text()="ข่าวสารคอนเทนต์บันเทิง"]'
]

num_choices = random.randint(1, len(q6_options)) 
choices_to_select = random.sample(q6_options, num_choices) 

for choice in choices_to_select:
    q6_option = driver.find_element(By.XPATH, choice)
    q6_option.click()
    
# 7
q7_options = [ 
    '//span[text()="1 วันต่อสัปดาห์"]',
    '//span[text()="2-3 วันต่อสัปดาห์"]',
    '//span[text()="4-5 วันต่อสัปดาห์"]',
    '//span[text()="ทุกวัน"]'
]
q7_choice = random.choice(q7_options)
q7_option = driver.find_element(By.XPATH, q7_choice)
q7_option.click()

# 8
q6_options = [
    '//span[text()="เพื่อความสนุกสนาน"]',
    '//span[text()="เพื่อใช้เวลาและสนุกอยู่กับเพื่อน"]',
    '//span[text()="เพื่อพัฒนาทักษะการเล่นเกม"]',
    '//span[text()="ต้องการแข่งขัน"]',
    '//span[text()="ต้องการเป็นนักกีฬาอาชีพ"]'
]

num_choices = random.randint(1, len(q6_options)) 
choices_to_select = random.sample(q6_options, num_choices) 

for choice in choices_to_select:
    q6_option = driver.find_element(By.XPATH, choice)
    q6_option.click()
    
# 9
q9_options = [ 
    '//span[text()="มากกว่า 12 ชั่วโมง"]',
    '//span[text()="8 - 12 ชั่วโมง"]',
    '//span[text()="4 - 8 ชั่วโมง"]',
    '//span[text()="น้อยกว่า 4 ชั่วโมง"]'
]
q9_choice = random.choice(q9_options)
q9_option = driver.find_element(By.XPATH, q9_choice)
q9_option.click()

# 10
q10_options = [ 
    '//span[text()="เพื่อนหรือคนที่สนิท"]',
    '//span[text()="ครอบครัว"]',
    '//span[text()="คนรู้จักออนไลน์"]',
    '//span[text()="คนเดียว"]'
]
q10_choice = random.choice(q10_options)
q10_option = driver.find_element(By.XPATH, q10_choice)
q10_option.click()

# 11
q11_options = [
    '//span[text()="เพื่อต้องการอัปเดตข้อมูลใหม่ๆเกี่ยวกับแพตซ์ ตัวละคร เพื่อปรับกลยุทธ์ให้ทันสมัย"]',
    '//span[text()="เพื่อติดตามการแข่งขันทั้งในประเทศและระดับนานาชาติ"]',
    '//span[text()="เพื่อเรียนรู้เทคนิคและแนวทางการเล่นผ่านสื่ออนไลน์จากสตรีมเมอร์และนักแข่ง"]',
    '//span[text()="เพื่อติดตามโปรโมชันและกิจกรรมในเกมเกี่ยวกับสกินใหม่ อีเวนต์แจกของ"]',
    '//span[text()="เพื่อพูดคุยแลกเปลี่ยนข้อมูลกับเพื่อนในการเล่นหรือหาเพื่อนใหม่"]',
    '//span[text()="เพื่อความบันเทิงและคลายเครียด ผ่านการรับชมความสนุกเกี่ยวกับเกมหรือจากสตรีมเมอร์"]'
]

num_choices = random.randint(1, len(q11_options)) 
choices_to_select = random.sample(q11_options, num_choices) 

for choice in choices_to_select:
    q11_option = driver.find_element(By.XPATH, choice)
    q11_option.click()
    
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
submit_button.click()

# ปิดเบราว์เซอร์
driver.quit()