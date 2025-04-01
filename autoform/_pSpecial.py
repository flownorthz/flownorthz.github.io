import subprocess
print("---------")
print("1.Choice 2.MultiChoice")
print("---------")
choose = int(input("Choose Type: "))
if choose == 1:
    subprocess.run(['python', '_pSpecialChoice.py'])
elif choose == 2:
    subprocess.run(['python', '_pSpecialMultiChoice.py'])
else:
    print("Invalid choice. Please select a valid option.")