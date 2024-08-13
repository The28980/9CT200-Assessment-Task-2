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
    print("""Welcome User to:
    Top Songs of 2024: Data Analyser
    
    Menu:
    1 - Load original dataset
    2 - Search for something more specific
    3 - Quit Program
    Please enter the number corresponding to your command
          """)
    
    try:
        command = int(input('-> '))
        if command == 1:
            ShowOriginalData()
            print("Menu will re-appear in 10 seconds")
            time.sleep(10)
        elif command == 2:
            print("This is filler. Area not completed yet!")
        elif command == 3:
            print("Closing down program...")
            time.sleep(3)
            getout = True
        else:
            print("""Don't act like you can't count to 3 on one hand. Try again user.
                  """)
    except:
        print("""Number. N-U-M-B-E-R. I don't even KNOW what this is meant to be. Try again user.
              """)

# +=================================================={ The Actual Code }==================================================+
while not getout:
    MainMenu()