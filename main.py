import pandas as pd
import matplotlib.pyplot as plt
import time

# df1: DataFrame 1 - Original data
df1 = pd.read_csv('notcode/thedata.csv', on_bad_lines='warn')

# +=================================================={ Global Variables }==================================================+
getout = False

# +=================================================={ Defining Functions }==================================================+
def ShowOriginalData():
    print(df1)

def MainMenu():
    global getout
    print("""
    Menu:
    1 - Load original dataset
    2 - Search for something more specific
    3 - Quit Program
    Please enter the number corresponding to your command""")
    
    try:
        command = int(input('-> '))
        print("")
       
        if command == 1:
            print("Displaying Original Data...")
            time.sleep(1)
            ShowOriginalData()
            print("Menu will re-appear in 10 seconds")
            time.sleep(10)
        
        elif command == 2:
            print("""What would you like to search for?
    1 - Artist
    2 - Album
    3 - Return to main menu""")
            specify = int(input("-> "))
            if specify == 1:
                time.sleep(0.5)
                print("")
                print("Didn't think you'd make it this far (W.I.P)")
                time.sleep(0.5)
            elif specify == 2:
                time.sleep(0.5)
                print("")
                print("Go back go back go back (W.I.P)")
                time.sleep(0.5)
            elif specify == 3:
                print("Returning to main menu...")
                time.sleep(1.5)

        
        elif command == 3:
            print("Closing down program...")
            time.sleep(3)
            getout = True
        
        else:
            time.sleep(0.5)
            print("""
Don't act like you can't count to 3 on one hand. Try again user.""")
            time.sleep(2.5)
    except:
        time.sleep(0.5)
        print("""
Number. N-U-M-B-E-R. I don't even KNOW what this is meant to be. Try again user.""")
        time.sleep(2.5)

# +=================================================={ The Actual Code }==================================================+
print("""
Initiating 2024 Music Analysis System. Welcome User.""")
time.sleep(2)
while not getout:
    MainMenu()