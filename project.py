import mysql.connector
import time
import admission
import patientdata
import banner
import facility
import views
myconn=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='project') 

mycursor=myconn.cursor()

while True:
        banner.banner()
        print("1: Patient Management ")
        print("2: Admission Management")
        print("3: Facility Management")
        print("4: Data viewing and Billing")
        print("0: Exit")
        print()
        print()
        print()
        ch=int(input("Enter your choice:"))
        if ch==1:
            patientdata.patient_menu()
        if ch==2:
            admission.admission_menu()
        if ch==3:
            facility.facility_menu()
        if ch==4:
            views.view_menu()
        if ch==0:
            exit()
        





        
        
        



    









