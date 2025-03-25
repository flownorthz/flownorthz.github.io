import subprocess

file = 'EgoSports.py'
round = 500
count = 1

for _ in range(round):
    subprocess.run(['python', file])
    print(f"Round --- ({count}/{round}) ")
    count = count + 1
    
print(f"End ({round}/{round})")
