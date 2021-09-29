#importing
import webbrowser
import time
#time
s = 1
n = 2
m = 5
#welcoming to win7 store
print("\nWelcome to Win7 Store  {Windows-7} \n")
time.sleep(n)
print("Loading...")
time.sleep(n)
print("Getting All Apps\n")
time.sleep(n)
print("[########", end="")
time.sleep(m)
print("#############]\n")
time.sleep(n)
print("All Are Done\n")
time.sleep(n)

def insappb():
    if (insapp == "1"):  # Google
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...\n")
        webbrowser.open('https://www.google.com/chrome/thank-you.html?brand=CHBD&statcb=1&installdataindex=empty&defaultbrowser=0#')
        startup()
    if (insapp == "2"):  # Zoom
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://zoom.us/client/latest/ZoomInstaller.exe")
        startup()
    if (insapp == "3"):  # Whatsapp
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://web.whatsapp.com/")
        startup()
    if (insapp == "4"):  # teams
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://www.microsoft.com/en-in/microsoft-teams/group-chat-software")
        startup()
    if (insapp == "5"):  # VLC Player
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://mirrors.estointernet.in/videolan/vlc/3.0.16/win32/vlc-3.0.16-win32.exe")
        startup()
    if (insapp == "6"):  #Games 
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://en.softonic.com/downloads/pc-games-for-windows-7")
        startup()    
    if (insapp == "7"):  #QR code
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://dw.uptodown.com/dwn/5hSD0lGVPsIsM3d1TOa1iMBJFwjj7ajK_YsfzZDvJg3bq0ihwr998YSDvahD0BPrC4unKGqzJRxpdwxun84WzAgecehSWNcBSss9wQA2SU3Ac7MuEZpEbzX3FydcNsfl/sbH-dDVaIOgZzMB2VLwwJxjGy-BY1faQQG-5Zej6mgXuYz_PNUJLaptOJboFpibjGhBnoIELz0dotFl1BsKIvYpgTTArLgSVRkB3uNXqFqQb1H27CDyeRZ1oMKQXIHtM/6HlOpMgj5m9vxG_mHNLDP_FX5k0OJ4YvDARS-s48-rPttYcd9BX95skGi0T9Jjnma0YTsyDiXlzQgMjzd24dbQ==/")
        startup() 
    if (insapp == "8"):  #Pdf To Image
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://pdf-to-jpg.en.softonic.com/download")
        startup() 
    if (insapp == "9"):  #Facebook
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://softmany.com/facebook-windows/download/")
        startup() 
    if (insapp == "10"): #Instagram 
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://en.softonic.com/download-launch?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb3dubG9hZFR5cGUiOiJyZWRpcmVjdGlvbkRvd25sb2FkIiwiZG93bmxvYWRVcmwiOiJodHRwczovL3d3dy5taWNyb3NvZnQuY29tL2VuLXVzL3N0b3JlL3AvaW5zdGFncmFtLzluYmxnZ2g1bDl4dCIsImFwcElkIjoiZjk2ZGY4N2QtOTI2Zi00OTU0LWJmNTgtZjM3N2E1NzNhNjMwIiwicGxhdGZvcm1JZCI6IndpbmRvd3MiLCJpYXQiOjE2MzE0MjkzNjYsImV4cCI6MTYzMTQzMjk2Nn0.Y8-VOrXZFokoEzPfUC8vaNepG7VqIvok-S2-96SiJeI")
        startup() 
    if (insapp == "11"): #YouTube 
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://youtube.com/")
        startup()    
    if (insapp == "12"): #K7 Antivirus
        print("\n")
        print("A WINDOW WILL OPEN AND START INSTALLING...")
        print("\n")
        webbrowser.open("https://www.k7computing.com/in/free_downloads")
        startup()      
    if (insapp == "13"): #About the Win7 store
        print("\n About the Win7 store")
        print("""
                Win7 store version : 0.01\n
                Win7 store is made by R.Vinith\n
                Win7 store Apps :-
                1 Google Chrome    6 Games           11 YouTube
                2 Zoom             7 QR code         12 k7 Antivirus
                3 Whatsapp         8 Pdf To Image    13 About the Win7 store
                4 Teams            9 Facebook
                5 VLC Player       10 Instagram \n
                Win7 store Made Date : 12/09/2021\n
                Win7 store There Is A Update\n\n
        """)
        startup()


def startup():
    #showing apps which can be install
    print("""\n
        1 Google Chrome    6 Games           11 YouTube
        2 Zoom             7 QR code         12 k7 Antivirus
        3 Whatsapp         8 Pdf To Image    13 About the Win7 store
        4 Teams            9 Facebook
        5 VLC Player       10 Instagram \n
    """)
    #Which app want to install asking as input
    #insapp is asking input to installing which app
    global insapp
    insapp = input("Type The Number Of The App To Install : ")
    #printing what have the user selected
    print("You Have Selected ", insapp)
    if (insapp == "1" or insapp == "2" or insapp == "3" or insapp == "4" or insapp == "5" or insapp == "6" or insapp == "7" or insapp == "8" or insapp == "9" or insapp == "10" or insapp == "11" or insapp == "12" ):
        #comforiming to install the app
        global yesno
        yesno = input("Do You Want to Install The Selected App (Y/N) : ")
        print("\n")
    elif (insapp == "13"):
        insappb()
    else:
        print("You Should Select Any App From Above Given Apps as number ")
        startup()


startup()

#reinsapp = input("Type The Number Of The App : ")

#function to install selected app
#insappa = reinsapp

#       1 Google Chrome    6 Games           11 YouTube
#       2 Zoom             7 QR code         12 k7 Antivirus
#       3 Whatsapp         8 Pdf To Image    13 About the Win7 store
#       4 Teams            9 Facebook
#       5 VLC Player       10 Instagram



if (yesno == "Y" or yesno == "y" or yesno == "yes" or yesno == "Yes"):
    print("\n You Have Typed ", yesno)
    insappb()
elif (yesno == "N" or yesno == "n" or yesno == "no" or yesno == "No"):
    print("You Have Typed : ", yesno)
    print("because of that it may be not installing \n")
    print("You Can Install Any Other App\n")
    startup()
else:
    print("You Have Typed : ", yesno)
    print("because of that it may be not installing \n")
    print("You Can Install Any Other App\n")
    startup()
