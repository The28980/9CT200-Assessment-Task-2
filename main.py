import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# +=================================================={ Data Frames }==================================================+
df1 = pd.read_csv('notcode/thedata.csv', on_bad_lines='warn') # df1: DataFrame 1 - Original base data

df2 = df1.drop(columns=['ISRC', 'All Time Rank', 'Track Score', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'Spotify Popularity', 'YouTube Likes', 'TikTok Posts', 'TikTok Likes', 'YouTube Playlist Reach', 'Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins', 'Deezer Playlist Count', 'Deezer Playlist Reach', 'Amazon Playlist Count' ,'Pandora Streams', 'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity', 'Explicit Track']) # df2: DataFrame 2 - Updated base data
df2.drop_duplicates(subset=['Track', 'Artist'], keep='first', inplace=True) # df2: Updated DataFrame - Cuts many columns and duplicates

newest_df = df2.sort_values(by='Release Date', ascending=False)

# viewest_df1, viewest_df2 and viewest_df3 not listed on here because they change depending on user inputs.

# +=================================================={ MatPlotLib }==================================================+
 # Due to lack of access to matplotlib and pandas at home, I am unable to prove if this code works.
# def df1plot():
    # name1 = df1['Track'].head(110)
    # streams1 = df1['Spotify Streams'].head(11)
    # fig = plt.figure(figsize =(100, 10))
    # plt.bar(name1[0:100], streams1[0:10])
    # plt.show()

# def df2plot():
    # name2 = df2['Track'].head(110)
    # streams2 = df2['Spotify Streams'].head(11)
    # fig = plt.figure(figsize =(100, 10))
    # plt.bar(name2[0:100], streams2[0:10])
    # plt.show()

# +=================================================={ Global Variables }==================================================+
getout = False # Dictates whether the program runs or not.

# +=================================================={ Defining Functions }==================================================+
def ShowOriginalData(): # Obligatory redundant function
    print(df1)

def ShowUpdatedData(): # Obligatory redundant function 2 (this is the last one)
    print(df2)

def MainMenu(): # The main menu with 4 options
    global getout
    print("""
    Menu:
    1 - Load original dataset
    2 - Load updated dataset
    3 - Sort updated dataset
    4 - Quit Program
    Please enter the number corresponding to your command""")
    
    try: # If statement but only the else part. Very useful for disobedient users.
        command = int(input('-> '))
        print("")
       
        if command == 1: # Option 1 displaying original data by using the first function
            print("Displaying Original Data...")
            time.sleep(1)
            ShowOriginalData()
            print("Menu will re-appear in 10 seconds...")
            time.sleep(10)
            # print("See as bar graph?")
            # bar1 = int(input("1: Yes/2: No -> "))
            # if bar1 == 2:
                # print("Menu will re-appear in 10 seconds")
                # time.sleep(10)

            # elif bar1 ==1:
                # df1plot()
                # print("Menu will re-appear in 10 seconds")
                # time.sleep(10)

            # else:
                # time.sleep(1)
                # print("Broken")
                

        if command == 2: # Option 2 displaying updated data, taking out unnecessary columns
            print("Displaying Updated Data...")
            time.sleep(1)
            ShowUpdatedData()
            print("Menu will re-appear in 10 seconds...")
            time.sleep(10)
            # print("See as bar graph?")
            # bar2 = int(input("1: Yes/2: No -> "))
            # if bar2 == 2:
                # print("Menu will re-appear in 10 seconds")
                # time.sleep(10)

            # elif bar2 ==1:
                # df2plot()
                # print("Menu will re-appear in 10 seconds")
                # time.sleep(10)

            # else:
                # time.sleep(1)
                # print("Broken")
            # print("Menu will re-appear in 10 seconds")
            # time.sleep(10)
        
        elif command == 3: # Option 3 opening up a whole new menu
            print("""How would you like to sort?
    1 - Newest -> Oldest
    2 - Popularity, descending
    3 - Return to main menu""")
            specify = int(input("-> "))
            if specify == 1: # Option 3a to see them in descending order, in terms of age
                time.sleep(0.5)
                print("Displaying sorted dataframe...")
                time.sleep(2)
                print(newest_df)
                time.sleep(0.5)
                print("Menu will re-appear in 10 seconds")
                time.sleep(10)

            elif specify == 2: # Option 3b to see them in descending order, in terms of streams on platforms
                time.sleep(0.5)
                print("""Which platform would you like to see?
    1 - Spotify
    2 - YouTube
    3 - TikTok
    4 - Return to main menu""")
                platform = int(input("-> "))
                if platform == 1:
                    time.sleep(0.5)
                    print("Filtering based on Spotify...")
                    viewest_df1=df2.drop(columns=['YouTube Views', 'TikTok Views'])
                    viewest_df1=viewest_df1.sort_values('Spotify Streams', ascending=False)
                    time.sleep(2)
                    print(viewest_df1)
                    print("Menu will re-appear in 10 seconds")
                    time.sleep(10)

                elif platform == 2:
                    time.sleep(0.5)
                    print("Filtering based on YouTube...")
                    viewest_df2 = df2.drop(columns=['Spotify Streams', 'TikTok Views'])
                    viewest_df2=viewest_df2.sort_values('YouTube Views',ascending=False)
                    time.sleep(2)
                    print(viewest_df2)
                    print("Menu will re-appear in 10 seconds")
                    time.sleep(10)

                elif platform == 3:
                    time.sleep(0.5)
                    print("Filtering based on TikTok...")
                    viewest_df3=df2.drop(columns=['Spotify Streams', 'YouTube Views'])
                    viewest_df3=viewest_df3.sort_values('TikTok Views',ascending=False)
                    time.sleep(2)
                    print(viewest_df3)
                    print("Menu will re-appear in 10 seconds")
                    time.sleep(10)

                elif platform ==4:
                    time.sleep(0.5)
                    print("Returning to main menu...")
                    time.sleep(2)

                else:
                    time.sleep(0.5)
                    print("What?")

            elif specify == 3: # Option 3c to return to main menu
                print("Returning to main menu...")
                time.sleep(1.5)

            else:
                time.sleep(0.5)
                print("""
Not funny. Didn't laugh. 1-3. Try again user.""")
                time.sleep(2.5)

        elif command == 4:
            print("Closing down program...") # Indicates the program is closing
            time.sleep(3)
            getout = True
        
        else:
            time.sleep(0.5)
            print("""
Don't act like you can't count to 4 on one hand. Try again user.""")
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