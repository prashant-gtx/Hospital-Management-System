import mysql.connector
import time
import patientdata
import banner
myconn=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='project') 

mycursor=myconn.cursor()
##patient1='''create table Patient(
##           PAT_ID VARCHAR(5) PRIMARY KEY,                   
##           DOC_ID VARCHAR(5),                               
##           PAT_NM VARCHAR(30),                                   
##           ADDRESS VARCHAR(40),
##           CONTACT_NO VARCHAR(15))'''
##
##mycursor.execute(patient1)

def patient_menu():
    while True:
        banner.banner()
        print("\t\t...................................")
        print("\t\t***Welcome to Patient Management System***")
        print("\t\t...................................")
        print("\n\t\t*****Patient Management*****")
        print("1: Add Patient details ")
        print("2: View Patient details ")
        print("3: Update Patient details ")
        print("4: Delete Patient details ")
        print("5: Search Patient Details ")
        print("6: Return")
        print("\t\t-----------------------------------")
        choice=int(input("Enter your Choice: "))
        if choice==1:
            patientdata.insertpatientdata()
        elif choice==2:
            patientdata.patientview()
        elif choice==3:
            patientdata.updatepatient()
        elif choice==4:
            patientdata.deletepatient()
        elif choice==5:
            patientdata.patientsearch()
        elif choice==6:
            return
        else:
            print("Error!! Invalid choice try again......")
            conti="Press any key to return to Main menu"

def insertpatientdata():
    try:
        PAT_ID=input('Enter Patient Id: ')
        DOC_ID=input('Enter Doctor Id: ')
        PAT_NM=input('Enter Patient Name: ')
        ADDRESS=input('Enter Address: ')
        CONTACT_NO=input('Enter Contact No: ')
        
        sql= "INSERT INTO Patient(PAT_ID, DOC_ID, PAT_NM, ADDRESS, CONTACT_NO) VALUES('{}','{}','{}','{}','{}')".format(PAT_ID,DOC_ID,PAT_NM,ADDRESS,CONTACT_NO)
        mycursor.execute(sql)
        time.sleep(2)
        print(mycursor.rowcount,"Record inserted")
        print("Thank you")
        myconn.commit()
    except:
        print()
        print()
        print()
        print()
        print("OOPS!")
        print("Error! Please Enter the data Correctly")



def patientview():
    sql="select * from patient"
    mycursor.execute(sql)
    rec=mycursor.fetchall()
    for x in rec:
        print(f'''
+------------------------------+
+  PAT_ID          :   {x[0]}                             
+  DOC_ID          :   {x[1]}                                              
+  PAT_NM          :   {x[2]} 
+  ADDRESS         :   {x[3]} 
+  CONTACT_NO      :   {x[4]}
+------------------------------+''')
        time.sleep(0.5)

def deletepatient():
    s=input("Enter PAT_ID to be deleted:  ")
    try:
        sql='''DELETE FROM Patient WHERE PAT_ID='''+s
        mycursor.execute(sql)
        time.sleep(1)
        print(mycursor.rowcount,"Record deleted")
        myconn.commit()  
    except:
        print("No Match Found!!")
        print("Enter Patient ID correctly!")

def updatepatient():
    print("Enter 1 to update name ")
    print("Enter 2 to update address ")
    print("Enter 3 to update contact ")
    print()
    print()
    print()
    print()
    ch=int(input("Enter your choice: "))
    try:
        if ch==1:
            s=input("Enter patient Id of the patient: ")
            x=input("ENTER THE NAME: ")
            sql="UPDATE Patient SET PAT_NM=%s WHERE PAT_ID=%s"
            mycursor.execute(sql,(x,s))
            myconn.commit()
        if ch==2:
            s=input("Enter patient id of the patient: ")
            x=input("Enter the address: ")
            sql="UPDATE Patient SET ADDRESS=%s WHERE PAT_ID=%s"
            mycursor.execute(sql,(x,s))
            myconn.commit()
        if ch==3:
            s=input("Enter patient id of the patient: ")
            x=input("Enter the Contact number: ")
            sql="UPDATE Patient SET CONTACT_NO=%s WHERE PAT_ID=%s"
            mycursor.execute(sql,(x,s))
            myconn.commit()
    except:
        print("No Match Found!!")
        print("Enter Patient ID correctly!")
    
def patientsearch():
    try:
       s=input("Enter patient Id of the patient: ")
       sql="Select PAT_ID from Patient WHERE PAT_ID=%s"
       mycursor.execute(sql,(s,))
       rec=mycursor.fetchall()
       for x in rec:
           print(x)
       time.sleep(2)
    except:
        print("Patient Id not found!!")

            
    
    
               
