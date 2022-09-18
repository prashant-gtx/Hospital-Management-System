import mysql.connector
import views
import time
myconn=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='project') 

mycursor=myconn.cursor()

r=0
s=0

def view_menu():
    while True:
        print("\t\t...................................")
        print("\t\t***Welcome to Patient Management System***")
        print("\t\t...................................")
        print("\n\t\t*****DATA VIEWING*****")
        print("1: VIEW ALL DETAILS")
        print("2: VIEW FOOD BILL")
        print("3: VIEW HOSPITALITY CHARGES")
        print("4: Return")
        print("\t\t-----------------------------------")
        choice=int(input("Enter your Choice: "))
        if choice==1:
            views.view2()
        elif choice==2:
            views.restaurentbill()
        elif choice==3:
            views.hospitality()
        elif choice==4:
            return
        else:
            print("Error!! Invalid choice try again......")
            conti="Press any key to return to Main menu"

##def view1():
##        sql='''SELECT Patient.PAT_ID,DOC_ID,PAT_NM,ADDRESS,CONTACT_NO,D_O_AD,D_O_DIS,BED_NO,BED_TYPE,WIFI,TV,NURSE_TYPE FROM Patient,Admission,Facility WHERE Patient.PAT_ID=Admission.PAT_ID '''
##        mycursor.execute(sql)
##        rec=mycursor.fetchall()
##        for x in rec:
##                print(f'''
##+------------------------------+
##+  PAT_ID          :   {x[0]}
##+  DOC_ID          :   {x[1]}
##+  PAT_NM          :   {x[2]}
##+  ADDRESS         :   {x[3]}
##+  CONTACT_NO      :   {x[4]}
##+  D_O_AD          :   {x[5]}
##+  D_O_DIS         :   {x[6]}
##+  BED_NO          :   {x[7]}
##+  BED_TYPE        :   {x[8]}
##+  WIFI            :   {x[9]}
##+  TV              :   {x[10]}
##+  NURSE_TYPE      :   {x[11]}
##+------------------------------+''')
##        time.sleep(4)

def view2():
        sql1='''SELECT* FROM Patient'''
        mycursor.execute(sql1)
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
        time.sleep(2)
        sql2='''SELECT* FROM Admission'''
        mycursor.execute(sql2)
        rec=mycursor.fetchall()
        for x in rec:
                print(f'''
+------------------------------+
+  PAT_ID          :   {x[0]}
+  D_O_AD          :   {x[1]}
+  D_O_DIS         :   {x[2]}
+  BED_NO          :   {x[3]}
+  BED_TYPE        :   {x[4]}
+------------------------------+''')
        time.sleep(2)
        sql3='''SELECT* FROM Facility'''
        mycursor.execute(sql3)
        rec=mycursor.fetchall()
        for x in rec:
                print(f'''
+------------------------------+
+  PAT_ID          :   {x[0]}
+  CUISINE         :   {x[1]}
+  WIFI            :   {x[2]}
+  TV              :   {x[3]}
+  NURSE_TYPE      :   {x[4]}
+------------------------------+''')
        time.sleep(4)


def restaurentbill():
        global r
        print(
'''


\t#====================================================#
\t#                                                    #
\t#                      FOOD MENU                     #
\t#                                                    #
\t#     {NAME OF THE DISH}     |       {ITEM PRICE}    #
\t# 1)WATER                    |             20        #
\t# 2)TEA                      |             10        #
\t# 3)BREAKFAST COMBO          |             90        #
\t# 4)LUNCH COMBO              |             110       #
\t# 5)DINNER COMBO             |             150       #
\t#                                                    #
\t#====================================================#
                    PRESS 6 TO EXIT
'''
     )
        while (1):
            c=int(input("Enter your choice:"))
            if (c==1):
                d=int(input("Enter the quantity:"))
                r=r+20*d
            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 r=r+10*d
            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 r=r+90*d
            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 r=r+110*d
            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 r=r+150*d
            elif (c==6):
                break;
            else:
                print("Invalid option")
        print ("Total Food Cost=Rs",r,"\n")

def hospitality():
    try:
        print ("We have the Following Beds:-")
        print ("1.  Classic---->Rs 1200 P/D")
        print ("2.  Deluxe----->Rs 2000 P/D")
        x=int(input("Please Enter your Choice->"))
        y=input('Enter PATIENT ID: ')
        z=y
        sql="SELECT DATEDIFF((SELECT D_O_DIS FROM ADMISSION WHERE PAT_ID=%s), (SELECT D_O_AD FROM ADMISSION WHERE PAT_ID=%s))"
        y=mycursor.execute(sql,(y,z,))
        rec=mycursor.fetchone()
        import functools 
        import operator  
  
        def convertTuple(tup): 
           str = functools.reduce(operator.add, (tup)) 
           return str
# Driver code 
        tuple =rec 
        str = convertTuple(tuple)  
        if(x==1):
            print ("You have opted Bed Type Classic")
            s=(1200)*str
        elif (x==2):
            print ("You have opted Bed Type Deluxe")
            s=2000*str
        else:
            print ("Please choose a Bed")
        print ("Your Bed Charge is =",s,"\n")
    except:
        print("Please enter correct Patient ID","\n")
        
