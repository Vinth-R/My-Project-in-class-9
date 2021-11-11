try:
    import json
    import os,shutil
    import datetime
    
    import random   

    os.chdir("C://")
    check=os.path.isfile("data of students")
    if check=="False":
        os.chdir("C://")
        os.makedirs("data of students")
        os.makedirs("data backup")
        os.chdir("C://data of students")
    if check=="True":
        os.chdir("C://data of students")
    def save():
        try:
            os.chdir("C://data of students")
            name=input("Name :")
            date=input("Date of Birthday :")
            roll=input("Roll No :")
            classofs=input("Class :")
            maths=input("Maths Mark :")
            sci=input("Sci Mark :")
            sst=input("SST Mark :")
            eng=input("English Mark :")
            lang=input("Lang Mark :")
            print("Getting the data in one file...")
            book={}
            book[roll]={
                'name':name,
                'date':date,
                'roll':roll,
                'classofs':classofs,
                'maths':maths,
                'sci':sci,
                'sst':sst,
                'eng':eng,
                'lang':lang
            }
            print("\nSaving the data...\n")
            s=json.dumps(book)
            f= open(roll+".txt","w")
            f.write(s)
            # s.close()
            f.close()
            print("Data Saved...\n")
        except:
            print("Not able to save data of student")
    def load():
        try:
            l=input("Roll No :")
            print("Getting... File of Roll No ", l)
            jsonfile=open("C://data of students//"+l+".txt",'r')
            jr=jsonfile.read()
            print("\nGetting data...\n")
            bjo=json.loads(jr)
            print("Name :",bjo[l].get('name'))
            print('Date :',bjo[l].get('date'))
            print('Roll :',bjo[l].get('roll'))
            print('Class :',bjo[l].get('classofs'))
            print('Maths :',bjo[l].get('maths'))
            print('Sci :',bjo[l].get('sci'))
            print('English :',bjo[l].get('eng'))
            print('Lang :',bjo[l].get('lang'))
            print("\nData has been printed\n")
            jsonfile.close()
        except:
            print("Not able to Load data of student\n")
            print("The Roll Number of student is not There in Data\n")
    def change():
        try:
            l=input("Roll No :")
            print("Getting the Data from file...")
            jsonfile=open("C://data of students//"+l+".txt",'a')
            readfile=open("C://data of students//"+l+".txt",'r')
            jr=readfile.read()
            bjo=json.loads(jr) 
            print("\n Printing the data of ",bjo[l].get('name'),"\n")             
            print("Name :",bjo[l].get('name'))
            print('Date :',bjo[l].get('date'))
            print('Roll :',bjo[l].get('roll'))
            print('Class :',bjo[l].get('classofs'))
            print('Maths :',bjo[l].get('maths'))
            print('Sci :',bjo[l].get('sci'))
            print('English :',bjo[l].get('eng'))
            print('Lang :',bjo[l].get('lang'))
            print("\n Enter the data to change \n")
            name=input("Name :")
            date=input("Date of Birthday :")
            roll=input("Roll No :")
            classofs=input("Class :")
            maths=input("Maths Mark :")
            sci=input("Sci Mark :")
            sst=input("SST Mark :")
            eng=input("English Mark :")
            lang=input("Lang Mark :")
            if name=="":
                name=bjo[l].get('name')
            if date=="":
                bjo[l].get('date')
            if roll=="":
                roll=bjo[l].get('roll')
            if classofs=="":
                classofs=bjo[l].get('classofs')
            if maths=="":
                maths=bjo[l].get('maths')
            if sci=="":
                bjo[l].get('sci')
            if sst=="":
                bjo[l].get('sst')
            if eng=="":
                bjo[l].get('eng')
            if lang=="":
                bjo[l].get('lang')
            book={}
            print("Getting the data to file")
            book[roll]={
                'name':name,
                'date':date,
                'roll':roll,
                'classofs':classofs,
                'maths':maths,
                'sci':sci,
                'sst':sst,
                'eng':eng,
                'lang':lang
            }
            s=json.dumps(book)
            jsonfile.write(s)
            jsonfile.close()
            readfile.close()
            print("Data changed")
        except:
            print("Not able to Change data of student\n")
            print("The Roll Number of student is not There in Data\n")    
    def delete():
        try:
            roll=input("Roll No :")
            os.remove(roll+".txt")
            print("Deleted the data")
        except:
            print("Not able to Delete data of student\n")
            print("The Roll Number of student is not There in Data\n")
    def backup():
        try:
            os.chdir("C://")
            date=datetime.today()
            date.strftime('%m/%d/%y')
            shutil.copytree("data of students","data backup"+date)
            os.chdir("C://data of students")
            print("\nBackup Done\n")        
        except:
            print("Back up Failed")
    while True:
        print("""
        1.Save
        2.Read
        3.Change
        4.Delete
        5.Backup
        """)
        nexta=input("enter :")
        if nexta=="1":
            save()
        if nexta=="2":
            load()
        if nexta=="3":
            change()
        if nexta=="4":
            delete()
        if nexta=="5":
            backup()
except :
    print("++++++++++ ERROR ++++++++++")
