import pandas as pd
import matplotlib.pyplot as plt
import time

# +=================================================={ Data Frames }==================================================+
df1 = pd.read_csv('notcode/thedata.csv', on_bad_lines='warn') # df1: DataFrame 1 - Original base data

df2 = df1 # df2: DataFrame 2 - Updated base data

# +=================================================={ Global Variables }==================================================+
getout = False # Dictates whether the program runs or not.

# +=================================================={ Defining Functions }==================================================+
def ShowOriginalData(): # Obligatory redundant function
    print(df1)

def MainMenu(): # The main menu with 3 options
    global getout
    print("""
    Menu:
    1 - Load original dataset
    2 - Search for something more specific
    3 - Quit Program
    Please enter the number corresponding to your command""")
    
    try: # If statement but only the else part. Very useful for disobedient users.
        command = int(input('-> '))
        print("")
       
        if command == 1: # Option 1 displaying original data by using the first function
            print("Displaying Original Data...")
            time.sleep(1)
            ShowOriginalData()
            print("Menu will re-appear in 10 seconds")
            time.sleep(10)
        
        elif command == 2: # Option 2 opening up a whole new menu
            print("""What would you like to search for?
    1 - Artist
    2 - Album
    3 - Return to main menu""")
            specify = int(input("-> "))
            if specify == 1: # Option 2a for a specific artist
                time.sleep(0.5)
                print("")
                print("Didn't think you'd make it this far (W.I.P)")
                time.sleep(0.5)
            elif specify == 2: # Option 2b for a specific album
                time.sleep(0.5)
                print("")
                print("Go back go back go back (W.I.P)")
                time.sleep(0.5)
            elif specify == 3: # Option 2c to return to main menu
                print("Returning to main menu...")
                time.sleep(1.5)
            else:
                time.sleep(0.5)
                print("""
Not funny. Didn't laugh. 1-3. Try again user.""")
                time.sleep(2.5)

        
        elif command == 3:
            print("Closing down program...") # Indicates the program is closing
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
        time.sleep(2.5) # Small breaks to let the sass really set in for the user.

# +=================================================={ The Actual Code }==================================================+
print("""
Initiating 2024 Music Analysis System. Welcome User.""")
time.sleep(2)
while not getout:
    MainMenu()