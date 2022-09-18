import mysql.connector
import time
import facility
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database='project')

mycursor=myconn.cursor()
##facilites='''create table Facility(
##            PAT_ID VARCHAR(5) REFERENCES Patient(PAT_ID),
##            cusisine varchar(10),  
##            tv varchar(3), 
##            wifi varchar(3), 
##            nurse_type varchar(10))'''
##mycursor.execute(facilites)

def facility_menu():
    while True:
        print("\t\t...................................")
        print("\t\t***Welcome to Patient Management System***")
        print("\t\t...................................")
        print("\n\t\t*****Patient Management*****")
        print("1: Add Facility details ")
        print("2: View Facility details ")
        print("3: Return")
        print("\t\t-----------------------------------")
        choice=int(input("Enter your Choice: "))
        if choice==1:
            facility.insert_facility_data()
        elif choice==2:
            facility.view_facility_data()
        elif choice==3:
            return
        else:
            print("Error!! Invalid choice try again......")
            conti="Press any key to return to Main menu"

def insert_facility_data():
    PAT_ID = input('ENTER PATIENT ID: ')
    cusisine = input('ENTER cusisine: ')
    tv = input('ENTER TV NEEDED OR NOT (Y FOR YES, N FOR NO): ')
    wifi = input('ENTER WIFI NEEDED OR NOT (Y FOR YES, N FOR NO): ')
    nurse_type = input('ENTER NURSE TYPE(REGULAR/INTENSIVE): ')
    sql = "INSERT INTO Facility(PAT_ID, cusisine, tv, wifi, nurse_type) VALUES('{}','{}','{}','{}','{}')".format(
        PAT_ID, cusisine, tv, wifi, nurse_type)
    mycursor.execute(sql)
    time.sleep(2)
    print(mycursor.rowcount, "RECORD INSERTED")
    print("THANK YOU")
    myconn.commit()


def view_facility_data():
    sql = "select * from Facility"
    mycursor.execute(sql)
    rec = mycursor.fetchall()
    for x in rec:
        print(f'''
+  PAT_ID          :   {x[0]}                               
+  cusisine        :   {x[1]}                                              
+  tv              :   {x[2]}
+  wifi            :   {x[3]}
+  nurse_type      :   {x[4]}\n\n''')
        time.sleep(0.5)
