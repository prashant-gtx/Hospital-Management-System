import mysql.connector
import time
import admission
import banner
myconn=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='project') 

mycursor=myconn.cursor()
##admission1='''create table Admission(
##             PAT_ID VARCHAR(5) REFERENCES Patient(PID),
##             D_O_AD DATE,                                           
##             D_O_DIS DATE,
##             BED_NO VARCHAR(5),
##             BED_TYPE VARCHAR(15))'''
##
##mycursor.execute(admission1) 

def admission_menu():
    while True:
        banner.banner()
        print("\t\t...................................")
        print("\t\t***Welcome to Patient Management System***")
        print("\t\t...................................")
        print("\n\t\t*****Admission Management*****")
        print("1: Add Admission details ")
        print("2: View Admission details ")
        print("3: Count Admitted Patients ")
        print("4: Return")
        print("\t\t-----------------------------------")
        choice=int(input("Enter your Choice: "))
        if choice==1:
            admission.insertadmissiondata()
        elif choice==2:
            admission.viewadmissiondata()
        elif choice==3:
            admission.countadm()
        elif choice==4:
            return
        else:
            print("Error!! Invalid choice try again......")
            conti="Press any key to return to Main menu"

def insertadmissiondata():
        PAT_ID=input('ENTER PATIENT ID: ')
        D_O_AD=input('ENTER DATE OF ADMISSION(YYYYMMDD): ')
        D_O_DIS=input('ENTER DATE OF DISCHARGE(YYYYMMDD): ')
        BED_NO=input('ENTER BED NUMBER(B-NO): ')
        BED_TYPE=input('ENTER BED TYPE(CLASSIC/DELUXE): ')
        
        sql="INSERT INTO Admission(PAT_ID, D_O_AD, D_O_DIS, BED_NO, BED_TYPE) VALUES('{}','{}','{}','{}','{}')".format(PAT_ID,D_O_AD,D_O_DIS,BED_NO,BED_TYPE)
        mycursor.execute(sql)
        time.sleep(2)
        print(mycursor.rowcount,"RECORD INSERTED")
        print("THANK YOU")
        myconn.commit()
    

def viewadmissiondata():
    sql="select * from Admission"
    mycursor.execute(sql)
    rec=mycursor.fetchall()
    for x in rec:
        print(f'''
+  PAT_ID          :   {x[0]}                               
+  D_O_AD          :   {x[1]}                                              
+  D_O_DIS         :   {x[2]}
+  BED_NO          :   {x[3]}
+  BED_TYPE        :   {x[4]}\n\n''')
        time.sleep(0.5)

def countadm():
        print("Total Patient Capacity: 15")
        sql="select count(*) as Admitted from Admission"
        mycursor.execute(sql)
        y=mycursor.fetchall()
        import functools 
        import operator  
  
        def convertTuple(tup): 
           str = functools.reduce(operator.add, (tup)) 
           return str
  
# Driver code 
        tuplex =y 
        str = convertTuple(tuplex) 
        print("NUMBER OF ADMITTED PATIENTS ARE: ",str)


        
