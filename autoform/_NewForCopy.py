import subprocess

while True:
    print("---------")
    print("1.Choice 2.MultipleChoice 3.Next 4.FiveChoice 5.Special 6.Starts 7.Send 8.Exit")
    print("---------")
    choose = int(input("Choose Type: "))


    if choose == 1:
        subprocess.run(['python', '_pChoice.py'])
    elif choose == 2:
        subprocess.run(['python', '_pMultChoice.py'])
    elif choose == 3:
        subprocess.run(['python', '_pNext.py'])
    elif choose == 4:
        subprocess.run(['python', '_pFiveChoice.py'])
    elif choose == 5:
        subprocess.run(['python', '_pSpecial.py'])
    elif choose == 6:
        subprocess.run(['python', '_pStarts.py'])
    elif choose == 7:
        subprocess.run(['python', '_pSend.py'])
    elif choose == 8:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")



