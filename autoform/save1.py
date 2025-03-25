import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

yes = [
    "สามารถดูได้ทุกที่ทุกเวลา",
    "ไม่ต้องรอการออกอากาศตามเวลา",
    "ใช้มือถือหรือคอมพิวเตอร์ดูได้",
    "ดูย้อนหลังได้",
    "ไม่มีการบังคับเลือกช่อง",
    "ไม่มีการจำกัดจำนวนคนดู",
    "ดูฟรีโดยไม่ต้องสมัครสมาชิก",
    "สามารถเลือกดูภาพหรือเสียงที่ต้องการ",
    "ไม่มีการหักเงินจากการดู",
    "สามารถดูได้หลายอุปกรณ์พร้อมกัน",
    "ไม่มีการแทรกโฆษณากลางรายการ",
    "สะดวกในการสลับไปมาระหว่างการชม",
    "มีฟังก์ชั่นการตั้งค่าความละเอียด",
    "มีการแสดงผลที่รองรับหน้าจอมือถือ",
    "สามารถเลือกชมเฉพาะตอนที่สนใจ",
    "ดูได้ทุกเวลาไม่ต้องรอเวลาการออกอากาศ",
    "สามารถใช้ฟังก์ชั่นการหยุดชั่วคราวได้",
    "สามารถตั้งเวลาแจ้งเตือนการถ่ายทอด",
    "ไม่ต้องใช้อุปกรณ์เสริมในการรับชม",
    "มีการแสดงข้อมูลบนหน้าจอในขณะดู",
    "สามารถแชร์ลิงค์ให้เพื่อนดูได้",
    "ไม่ต้องต่อสายเคเบิลหรือจานดาวเทียม",
    "สามารถเลือกดูหลายรายการพร้อมกัน",
    "ไม่มีการบังคับการติดตั้งซอฟต์แวร์พิเศษ",
    "ดูได้ทุกที่ที่มีอินเทอร์เน็ต",
    "สามารถดูผ่านสมาร์ททีวี",
    "สามารถควบคุมเสียงได้ดีกว่า",
    "สามารถแสดงความคิดเห็นขณะชมได้",
    "มีตัวเลือกในการดูแบบสดหรือรีรัน",
    "สามารถบันทึกรายการเพื่อดูภายหลัง",
    "มีช่องทางการรับชมหลายรูปแบบ",
    "ดูได้ทั้งภาษาไทยและภาษาอื่นๆ",
    "ไม่ต้องกลัวสัญญาณหาย",
    "ดูได้แม้กระทั่งในต่างประเทศ",
    "มีการรองรับการดูหลายหน้าจอ",
    "สามารถตั้งค่าคุณภาพภาพให้เหมาะสม",
    "สามารถเลือกดูแบบซับไตเติ้ลได้",
    "มีการควบคุมเวลาในการดู",
    "สามารถดูรายการซ้ำได้ตลอดเวลา",
    "มีระบบการจัดการบัญชีส่วนตัว",
    "สามารถดูแยกได้ตามความสนใจ",
    "สามารถติดตามช่องได้สะดวก",
    "มีความยืดหยุ่นในการรับชม",
    "ไม่มีการบังคับให้ดูทั้งหมดในครั้งเดียว",
    "ดูได้ทั้งในคอมพิวเตอร์และโทรศัพท์",
    "มีตัวเลือกในการสลับภาษา",
    "มีความสามารถในการปรับแต่งการรับชม",
    "สามารถเลือกดูช่วงเวลาที่ต้องการได้",
    "ไม่ต้องกังวลเรื่องการต่อสาย",
    "รองรับการดูในขนาดหน้าจอที่แตกต่างกัน",
    "สามารถดูได้ทุกที่ที่มีอินเทอร์เน็ต",
    "ไม่ต้องรอให้ทีวีเปิด",
    "สามารถเลือกดูย้อนหลังได้",
    "สามารถดูได้ทุกเวลา",
    "ไม่ต้องติดตั้งอุปกรณ์เพิ่มเติม",
    "ไม่ต้องกังวลเรื่องการเชื่อมต่อสัญญาณทีวี",
    "รองรับหลายอุปกรณ์",
    "ดูได้จากโทรศัพท์มือถือ",
    "สามารถเลือกดูการถ่ายทอดสดได้หลายช่องทาง",
    "ไม่ต้องใช้รีโมท",
    "ดูฟรี",
    "รองรับการดูด้วยความคมชัดสูง",
    "มีการตั้งค่าคุณภาพวิดีโอ",
    "สามารถดูการแสดงผลเต็มหน้าจอได้",
    "สามารถแชร์ลิงก์ให้เพื่อนดูได้ง่าย",
    "มีการแจ้งเตือนเมื่อมีการถ่ายทอดสด",
    "มีความยืดหยุ่นในการเลือกดู",
    "สามารถค้นหาคลิปต่าง ๆ ได้สะดวก",
    "ไม่มีโฆษณาขั้นกลาง (บางช่องทาง)",
    "ไม่จำกัดการดูในจำนวนครั้ง",
    "ดูได้โดยไม่ต้องมีเคเบิลทีวี",
    "ไม่ต้องกังวลเรื่องการตั้งเวลารับชม",
    "มีการรองรับคำบรรยายภาษาไทย",
    "สามารถสลับไปดูคลิปอื่นได้",
    "สามารถเลือกดูแบบชัดเจนหรือประหยัดข้อมูล",
    "ไม่ต้องกลัวโปรแกรมถ่ายทอดสดจะถูกยกเลิก",
    "ดูได้ไม่จำกัดช่อง",
    "สามารถดูพร้อมกับเพื่อน ๆ ผ่านแชร์ลิงก์",
    "สามารถดูในสถานที่ส่วนตัว",
    "ไม่ต้องรอเพื่อเข้าชมในช่อง",
    "สามารถตั้งการดูแบบอัตโนมัติ",
    "ดูได้ในหลายภาษาตามความสะดวก",
    "สามารถกดข้ามส่วนที่ไม่อยากดู",
    "รองรับการดูในภาพยนตร์ความคมชัดสูง (HD)",
    "ดูได้ในทุกที่ที่มีอินเทอร์เน็ต",
    "สามารถหยุดพักแล้วกลับมาดูต่อได้",
    "รองรับการดูแบบ 360 องศา (ถ้ามี)",
    "ดูได้โดยไม่ต้องใช้สายเคเบิล",
    "สามารถสตรีมจากหลายแหล่งได้",
    "ดูได้ทั้งจากคอมพิวเตอร์และโทรศัพท์",
    "ไม่ต้องกังวลเรื่องการหาช่องที่ถูกต้อง",
    "สามารถปรับเสียงให้เหมาะสมได้",
    "สามารถดูแบบ HD หรือ 4K (ถ้ามี)",
    "สามารถให้คะแนนหรือคอมเมนต์ในคลิป",
    "มีระบบค้นหาคอนเทนต์ที่ง่าย",
    "สามารถสมัครรับข้อมูลเพื่อไม่พลาดทุกการถ่ายทอดสด",
    "สามารถดูในหลากหลายอุปกรณ์เชื่อมต่อ",
    "รองรับการดูในหลายภาษาพร้อมคำบรรยาย",
    "ไม่ต้องพึ่งพาอินเทอร์เน็ตความเร็วสูงมาก",
    "สามารถดูรายการเก่าหรือย้อนหลังได้ตลอดเวลา"
]


no = [
    "ต้องมีการเชื่อมต่ออินเทอร์เน็ต",
    "อาจจะมีการแสดงโฆษณาก่อน",
    "ต้องใช้เวลาในการโหลด",
    "คุณภาพของภาพไม่เสถียร",
    "อาจจะเจอปัญหาความล่าช้า",
    "ต้องใช้แอปพลิเคชันหรือเบราว์เซอร์",
    "อาจจะต้องใช้เวลาในการค้นหาช่อง",
    "ไม่สามารถเปลี่ยนช่องได้ง่ายๆ",
    "บางครั้งต้องมีการลงชื่อเข้าใช้",
    "ต้องเปิดเครื่องคอมพิวเตอร์หรือโทรศัพท์",
    "ไม่สามารถรับชมได้ถ้าไม่มีอุปกรณ์",
    "ไม่สามารถดูได้ถ้าไม่มีการเชื่อมต่อ Wi-Fi",
    "คุณภาพเสียงบางครั้งไม่คมชัด",
    "อาจจะมีการบัฟเฟอร์ระหว่างการดู",
    "ต้องเปิดเครื่องมากขึ้น",
    "แสดงผลไม่ได้ในบางทีวีที่ไม่รองรับ",
    "ต้องคอยเช็คการเชื่อมต่ออินเทอร์เน็ต",
    "อาจจะมีการขัดข้องจากการใช้แอปพลิเคชัน",
    "ไม่สามารถดูในโหมดเต็มหน้าจอเสมอไป",
    "มีข้อจำกัดในการดูย้อนหลัง",
    "ไม่มีรีโมทควบคุม",
    "ต้องมีการสลับแอปหากดูหลายช่อง",
    "การจัดการเมนูซับซ้อนกว่า",
    "แบตเตอรี่ของอุปกรณ์อาจหมดเร็ว",
    "ไม่สามารถแสดงผลในความละเอียดสูงสุดเสมอไป",
    "อาจจะต้องใช้ความเร็วอินเทอร์เน็ตที่สูง",
    "มีการขัดข้องที่เกี่ยวข้องกับแอป",
    "บางครั้งต้องรอการอัปเดตแอป",
    "ต้องเชื่อมต่อกับทีวีด้วยสาย HDMI",
    "ไม่สามารถดูได้หากไม่ได้เปิดแอปที่รองรับ",
    "ต้องมีการสมัครสมาชิกหากต้องการดูบางรายการ",
    "อาจจะต้องจ่ายค่าบริการเพื่อเข้าถึงเนื้อหาบางอย่าง",
    "บางทีอาจจะเกิดปัญหาในเรื่องของการตั้งค่าคุณภาพ",
    "ต้องอัปเดตแอปพลิเคชันก่อนการดู",
    "ไม่สามารถดูพร้อมกันได้หลายอุปกรณ์",
    "ต้องรอให้การสตรีมเริ่มต้น",
    "อาจจะมีปัญหาเกี่ยวกับไฟล์แคช",
    "ต้องตั้งค่าการดูแบบเต็มหน้าจอ",
    "บางทีอาจจะเกิดการขัดข้องทางเทคนิค",
    "ใช้เวลานานในการเริ่มต้นการถ่ายทอดสด",
    "ไม่สามารถรับชมแบบสดได้เสมอไป",
    "บางทีต้องรอการถ่ายทอดสด",
    "อาจจะถูกจำกัดการดูบางช่อง",
    "ไม่สามารถควบคุมการดูได้ละเอียดเท่าทีวี",
    "ใช้เวลาในการค้นหาคอนเทนต์",
    "ต้องรอการเริ่มต้นของการถ่ายทอดสด",
    "การดูแบบออนไลน์อาจจะไม่สะดวกในบางกรณี",
    "บางครั้งต้องปรับเสียงหรือภาพด้วยตนเอง",
    "บางช่องไม่สามารถดูได้ในพื้นที่บางแห่ง",
    "อาจจะเจอปัญหาการแสดงผลในบางอุปกรณ์",
    "ต้องใช้การเชื่อมต่ออินเทอร์เน็ต",
    "ความเร็วอินเทอร์เน็ตไม่เสถียร",
    "ต้องเปิดอุปกรณ์หลายตัว",
    "ต้องดาวน์โหลดแอป",
    "ต้องกดเพื่อเลือกคลิปทุกครั้ง",
    "อาจเจอโฆษณาระหว่างการชม",
    "ต้องคอยควบคุมเสียง",
    "บางครั้งคลิปไม่สามารถเล่นได้",
    "บางคลิปอาจไม่มีคำบรรยาย",
    "ไม่สามารถดูช่องเดียวได้ตลอดเวลา",
    "ต้องมีบัญชี Google เพื่อสมัครใช้งาน",
    "ยากในการเลือกช่องที่ต้องการ",
    "ถ้าอินเทอร์เน็ตไม่ดี ภาพเบลอ",
    "ต้องใช้เวลาดาวน์โหลดวิดีโอ",
    "ระบบค้นหาไม่แม่นยำ",
    "บางคลิปอาจถูกจำกัดในบางประเทศ",
    "บางครั้งคลิปต้องรอจนกว่าจะมีการอัพโหลด",
    "ดูในมือถืออาจขัดจังหวะการใช้งานอื่น",
    "ไม่สามารถแชร์การดูพร้อมกันในครอบครัว",
    "ไม่สามารถดูแบบสดได้ทุกครั้ง",
    "ไม่สามารถดูหลายรายการในเวลาเดียวกัน",
    "บางครั้งเกิดปัญหาการเชื่อมต่อ",
    "คุณภาพการดูขึ้นอยู่กับอินเทอร์เน็ต",
    "ต้องใช้เวลามากในการค้นหา",
    "อาจมีการโหลดภาพช้า",
    "ต้องมีอุปกรณ์ที่รองรับ YouTube",
    "ไม่สามารถใช้งานได้ในบางอุปกรณ์",
    "ขนาดหน้าจอไม่เหมาะสมเมื่อดูบนมือถือ",
    "ต้องกดเพื่อเริ่มชมรายการทุกครั้ง",
    "คุณภาพเสียงอาจไม่ดีเท่าการดูทีวี",
    "ต้องใช้แอปที่เหมาะสมในการดู",
    "ไม่สามารถดูด้วยวิธีการง่ายๆ",
    "ไม่สามารถเห็นภาพในขนาดเต็ม",
    "บางคลิปอาจมีความละเอียดต่ำ",
    "การดูผ่านมือถืออาจทำให้หมดแบตเร็ว",
    "ต้องจัดการกับการตั้งค่าความละเอียด",
    "ต้องรอการโหลดจาก YouTube",
    "บางครั้งคลิปไม่แสดงตามที่ต้องการ",
    "ฟังก์ชันของ YouTube ไม่เหมือนทีวี",
    "ต้องมีการควบคุมด้วยมือในการเลือกรายการ",
    "การดูแบบย้อนกลับอาจทำได้ยาก",
    "ระบบค้นหามีข้อจำกัด",
    "ต้องใช้หลายขั้นตอนในการเปลี่ยนแปลง",
    "อาจมีการกระตุกระหว่างการเล่น",
    "ต้องเข้าสู่ระบบเพื่อเข้าถึงเนื้อหาบางอย่าง",
    "ไม่สามารถดูในบางช่วงเวลา",
    "บางคลิปไม่สามารถปรับขนาดหน้าจอได้",
    "การตั้งค่าของ YouTube อาจยุ่งยาก",
    "ยากในการค้นหาส่วนที่สนใจในคลิปยาว",
    "อาจมีข้อจำกัดในการดูย้อนหลัง"
]

randomyes = random.choice(yes)
randomno = random.choice(no)



# กำหนด path ของ WebDriver (เช่น ChromeDriver)
driver_path = r'C:\Windows\chromedriver.exe'

# ใช้ Service ในการกำหนด path ของ chromedriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# เปิด Google Form
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSd1ccRGcdxf_k2LwTSEkGgn5Ei_lUtDHBDtzzvt3DHg2J1esQ/formResponse')

# รอให้ฟอร์มโหลด
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

# 1
gender_options = [
    '//span[text()="ชาย"]',
    '//span[text()="หญิง"]',
    '//span[text()="LGBTQ+"]'
]
gender_choice = random.choice(gender_options)
gender_option = driver.find_element(By.XPATH, gender_choice)
gender_option.click()
time.sleep(1)

# 2
age_options = [
    '//span[text()="น้อยกว่า 20 ปี"]',
    '//span[text()="20-30 ปี"]',
    '//span[text()="41-50 ปี"]',
    '//span[text()="มากกว่า 50 ปีขึ้นไป"]'
]
age_choice = random.choice(age_options)
age_option = driver.find_element(By.XPATH, age_choice)
age_option.click()
time.sleep(1)

# 3
status_options = [
    '//span[text()="โสด"]',
    '//span[text()="สมรส"]',
    '//span[text()="หย่าร้าง"]',
    '//span[text()="หม้าย"]'
]
status_choice = random.choice(status_options)
status_option = driver.find_element(By.XPATH, status_choice)
status_option.click()
time.sleep(1)

# 4
edu_options = [
    '//span[text()="ต่ำกว่าปริญญาตรี"]',
    '//span[text()="ปริญญาตรี"]',
    '//span[text()="สูงกว่าปริญญาตรี"]',
]
edu_choice = random.choice(edu_options)
edu_option = driver.find_element(By.XPATH, edu_choice)
edu_option.click()
time.sleep(1)

# 5
money_options = [
    '//span[text()="ต่ำกว่า 10,000 บาท"]',
    '//span[text()="10,001-20,000 บาท"]',
    '//span[text()="20,001-30,000 บาท"]',
    '//span[text()="30,001-40,000 บาท"]',
    '//span[text()="40,001 บาทขึ้นไป"]',
]
money_choice = random.choice(money_options)
money_option = driver.find_element(By.XPATH, money_choice)
money_option.click()
time.sleep(1)

# next
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(1)

# 6
offen_options = [
    '//span[text()="ทุกสัปดาห์"]',
    '//span[text()="2-3 ครั้งต่อเดือน"]',
    '//span[text()="1 ครั้งต่อเดือน"]',
    '//span[text()="30,001-40,000 บาท"]',
    '//span[text()="น้อยกว่าหนึ่งครั้งต่อเดือน"]',
]
offen_choice = random.choice(offen_options)
offen_option = driver.find_element(By.XPATH, offen_choice)
offen_option.click()
time.sleep(1)

# 7
or_options = [
    '//span[text()="ดูทุกคู่จนจบ"]',
    '//span[text()="เลือกดูเฉพาะบางคู่ที่สนใจ"]',
]
or_choice = random.choice(or_options)
or_option = driver.find_element(By.XPATH, or_choice)
or_option.click()
time.sleep(1)

# 8
tool_options = [
    '//span[text()="สมาร์ทโฟน"]',
    '//span[text()="แท็บเล็ต"]',
    '//span[text()="คอมพิวเตอร์ / โน้ตบุ๊ก"]',
    '//span[text()="สมาร์ททีวี"]',
]
tool_choice = random.choice(tool_options)
tool_option = driver.find_element(By.XPATH, tool_choice)
tool_option.click()
time.sleep(1)

# 9. 
# Multiple-choice (checkboxes)
tool9_options = [
    '//span[text()="สมาร์ทโฟน."]',
    '//span[text()="แท็บเล็ต."]',
    '//span[text()="คอมพิวเตอร์ / โน้ตบุ๊ก."]',
    '//span[text()="สมาร์ททีวี."]',
]

# สุ่มเลือกหลายตัวเลือก
num_choices = random.randint(1, len(tool9_options))  # สุ่มจำนวนตัวเลือกที่ต้องการ
choices_to_select = random.sample(tool9_options, num_choices)  # เลือกตัวเลือกที่สุ่มมา

# คลิกตัวเลือกที่เลือก
for choice in choices_to_select:
    tool9_option = driver.find_element(By.XPATH, choice)
    tool9_option.click()
time.sleep(1)

# 10. 
# Multiple-choice (checkboxes)
place_options = [
    '//span[text()="ที่บ้าน"]',
    '//span[text()="ที่ทำงาน"]',
    '//span[text()="ขณะเดินทาง"]',
]

# สุ่มเลือกหลายตัวเลือก
num_choices = random.randint(1, len(place_options))  # สุ่มจำนวนตัวเลือกที่ต้องการ
choices_to_select = random.sample(place_options, num_choices)  # เลือกตัวเลือกที่สุ่มมา

# คลิกตัวเลือกที่เลือก
for choice in choices_to_select:
    place_option = driver.find_element(By.XPATH, choice)
    place_option.click()


# 11. 
# Multiple-choice (checkboxes)
why_options = [
    '//span[text()="ดูฟรี ไม่มีค่าใช้จ่าย"]',
    '//span[text()="สามารถดูย้อนหลังได้"]',
    '//span[text()="มีภาพและเสียงที่คมชัด"]',
]

# สุ่มเลือกหลายตัวเลือก
num_choices = random.randint(1, len(why_options))  # สุ่มจำนวนตัวเลือกที่ต้องการ
choices_to_select = random.sample(why_options, num_choices)  # เลือกตัวเลือกที่สุ่มมา

# คลิกตัวเลือกที่เลือก
for choice in choices_to_select:
    why_option = driver.find_element(By.XPATH, choice)
    why_option.click()
time.sleep(1)

# 12
convenience_options = [
    '//span[text()="สะดวกกว่า"]',
    '//span[text()="ไม่สะดวกกว่า"]'
]

# สุ่มเลือกตัวเลือก
convenience_choice = random.choice(convenience_options)
convenience_option = driver.find_element(By.XPATH, convenience_choice)
convenience_option.click()
time.sleep(1)



# next
next_button = driver.find_element(By.XPATH, '//span[text()="ถัดไป"]')
next_button.click()
time.sleep(1)


# 13

# เก็บค่าตัวแปรตามการเลือก
if convenience_choice == '//span[text()="สะดวกกว่า"]':
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))
    )
    input_field.send_keys(randomyes)
else:
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))
    )
    input_field.send_keys(randomno)
time.sleep(1)


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
# ค้นหาตัวเลือกทั้งหมดของข้อที่ 1
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
# ค้นหาตัวเลือกทั้งหมดของข้อที่ 1
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

print("----------")

# รอจนกว่าปุ่มส่งจะปรากฏ
submit_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="ส่ง"]'))
)
submit_button.click()

# ปิดเบราว์เซอร์
driver.quit()


