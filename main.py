import mysql.connector
from tabulate import  tabulate
import Registerall
import re
con=mysql.connector.connect(host="localhost",user="root",password="#86089070j",database="Admins")


# def Adminregister(admin_email,admin_password):
#     try:
#         res = con.cursor()
#         sql = "insert into Adminregister (admin_email,admin_password) values (%s,%s)"
#         data=(admin_email,admin_password)
#         res.execute(sql,data)
#         con.commit()
#         print("Registerd successfully")
#     except Error as e:
#         print(e)
#     finally:
#         res.close()
#         con.close()
    # admin_email=input("Enter your login mail :")
    # admin_password=int(input("Enter your password :"))
    # adminlogin(admin_email, admin_password)
spl_char = ['.', '#''!', '@', '%', '^', '&', '/', '=', '?', '-', '$']

def UserRegister(user_email,user_password):
    try:
        res = con.cursor()
        sql = "insert into UserRegister (user_email,user_password) values (%s,%s)"
        data=(user_email,user_password)
        res.execute(sql,data)
        con.commit()
        print("Registerd successfully")
        print("!-----Welcome to User Home Page-----!")
        user_email = input("USER Email :")
        user_password = input("USER passcode :")
        userlogin(user_email,user_password)
    except Error as e:
        print(e)
    finally:
        res.close()
        con.close()


def adminlogin(admin_email, admin_password):
    try:
        res = con.cursor()
        sql = "select admin_email from Adminregister where admin_email = %s and admin_password =%s"
        data = (admin_email, admin_password)
        res.execute(sql, data)
        result = res.fetchone()

        if result is not None:
            if admin_email == str(result[0]):
                print("Logged in..!")
                # Registerall.fun1()
                print("!---1 is Insert,Update,Detele Student personal data || 2 is show Student records || 3 is Insert student activities---!")
                choose=int(input("Enter the choices :"))
                if choose==1:
                    Registerall.fun1()
                elif choose==2:
                    # id=int(input("Enter your student id :"))
                    Registerall.select()
                elif choose==3:
                    id = int(input("Enter student id :"))
                    studentname = input("Enter the Student name :")
                    skills = input("Enter student skills :")
                    performance = input("Enter student performance :")
                    rate = input("Student Rating :")
                    Registerall.insertactivities(id, studentname, skills, performance, rate)
                else :
                    print("Invalid number ,Try Again")

        #                 field1 = cursor.fetchone()
        else:
            print("Invalid credentials...Try again")

    except Error as e:
        print(e)
    finally:
        res.close()
        con.close()


def userlogin(user_email, user_password):
    try:
        res = con.cursor()
        sql = "select user_email from Userregister where user_email = %s and user_password =%s"
        data = (user_email, user_password)
        res.execute(sql, data)
        result = res.fetchone()

        if result is not None:
            if user_email == str(result[0]):
                print("!---Logged in---!")
                print("PRESS 1 is Personal Detail || 2 is Your Activity :")
                choose=int(input("Enter your choice :"))
                if choose==1:
                    id = int(input("Your id :"))
                    Registerall.select1(id)
                elif choose==2:
                    ids = int(input("Your id :"))
                    Registerall.activity(ids)

        #                 field1 = cursor.fetchone()
        else:
            print("Invalid credentials...Try again")

    except Exception as e:
        print(e)
    finally:
        res.close()
        con.close()


# def login():
#     try:
#         res = con.cursor()
#         sql = "select * from register"
#         res.execute(sql)
#         result=res.fetchall()
#         print(tabulate(result,headers=['id','user_email','user_password']))
#         print("Registerd successfully")
#     except Error as e:
#         print(e)
#     finally:
#         res.close()
#         con.close()


print("!--------------WELCOME TO ALL---------------! ")
print(" Press 1 USERS-REGISTER || Press 2 ADMIN-LOGIN || PRESS 3 USER-LOGIN")
choices = int(input("Enter Your Status (Admin or User):"))
# if choices == 1:
#
#     admin_email = input("Enter the emailn :")
#     admin_password =  input("Enter the passwordn :")
#     # import mailmod
#     # import passwordmod
#     # Adminregister(mailmod.email(admin_email),passwordmod.password(admin_password))
#     Adminregister(admin_email,admin_password)

if choices == 1:
    # user_email = input("USER REGISTER Email :")
    # user_password = input("USER passcode :")
    # email=""
    while True:
        try:
            user_email = input("Enter Mail id:")
            m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", user_email)
            if m != None:
                print("Valid Mail Id");
            else:
                print("Invalid Mail id")
        except ValueError:
            print("Enter Email in valid format")
            # email=str(m)
        break


    # user_email=input("Enter the E-mail :")
    while True:
        try:
            user_password = input('please enter user_password ')
            if (len(user_password) < 8):
                raise ValueError(" Password should contain at least 6 character ")
            if not any(char.isdigit() for char in user_password):
                raise ValueError("Password should atleast a number")
            if not any(char.isupper() for char in user_password):
                raise KeyError()
            if not any(char.islower() for char in user_password):
                raise KeyError
            if not any(char in spl_char for char in user_password):
                raise KeyError
            break
        except ValueError:
            print(
                "Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 8 ch")
    UserRegister(user_email,user_password)
    # if UserRegister(user_email, user_password) is not None:

elif choices == 2:
    admin_email = input("ADMIN Email :")
    admin_password = input("ADMIN passcode :")
    adminlogin(admin_email, admin_password)
elif choices == 3:
    user_email = input("USER Email :")
    user_password = input("USER passcode :")
    userlogin(user_email, user_password)

else:
    print("!---sorry ,please select valid number---!")
