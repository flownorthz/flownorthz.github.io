import subprocess
from datetime import datetime, timedelta

file = 'Tudubon.py'
time = 41
round = 2
count = 1

# บันทึกเวลาเริ่มต้น
start_time = datetime.now()
print("---------------")
print(f"เริ่มต้นการรันเวลา: {start_time.strftime('%H:%M:%S')}")

# คำนวณเวลาที่จะใช้ทั้งหมด (time * round) แล้วแปลงเป็น timedelta
total_time_seconds = time * round
total_time = timedelta(seconds=total_time_seconds)

# คำนวณเวลาที่จะเสร็จ
end_time = start_time + total_time

# แสดงเวลาที่จะเสร็จ
print(f"การรันทั้งหมดจะเสร็จประมาณเวลา: {end_time.strftime('%H:%M:%S')}")
print("---------------")

# รันโปรแกรมในรอบที่กำหนด
for _ in range(round):
    subprocess.run(['python', file])
    print("---------------")
    print(f"Round ({count}/{round}) ")
    count = count + 1
    print(f"การรันทั้งหมดจะเสร็จประมาณเวลา: {end_time.strftime('%H:%M:%S')}")
    print("---------------")

finishtime = datetime.now()
ftime = finishtime - start_time

# แสดงเวลาเริ่มต้นและจบ
print(f"End ({round}/{round})")
print(f"เริ่มต้นการรันเวลา: {start_time.strftime('%H:%M:%S')}")
print(f"จบการรันเวลา: {datetime.now().strftime('%H:%M:%S')}")
print(f"ใช้เวลาการรันไป {ftime}")
