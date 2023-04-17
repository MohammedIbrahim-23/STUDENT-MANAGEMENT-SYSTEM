from mysqlx import Error
from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="#86089070j", database="Admins")


# insert
def insert(studentname, age, ph_no, DOB, Address, gender, result, CGPA):
    try:
        store_insert = con.cursor()
        sql = "insert into records (studentname,age,ph_no,DOB,Address,gender,result,CGPA) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (studentname, age, ph_no, DOB, Address, gender, result, CGPA)
        store_insert.execute(sql, data)
        con.commit()
        print("Data successfully inserted")
    except Error as e:
        print(e)
    # finally:
    #     store_insert.close()
    #     con.close()


# update
def update(studentname, age, ph_no, DOB, Address, gender, result, CGPA, id):
    global store_update
    try:
        store_update = con.cursor()
        sql = "update records set studentname=%s,age=%s,ph_no=%s,DOB=%s,Address=%s,gender=%s,result=%s,CGPA=%s where id=%s"
        data = (studentname, age, ph_no, DOB, Address, gender, result, CGPA, id)
        store_update.execute(sql, data)
        con.commit()
        print("Data successfully updated ")

    except Error as e:
        print(e)
    finally:
        store_update.close()
        con.close()


# delete
def delete(id):
    global store_delete
    try:
        store_delete = con.cursor()
        sql = "delete from records where id=%s"
        data = (id,)
        store_delete.execute(sql, data)
        con.commit()
        print("Data successfully deleted ")

    except Error as e:
        print(e)
    finally:
        store_delete.close()
        con.close()


# select
def select():
    global res
    try:
        res = con.cursor()
        sql = "select id,studentname,age,ph_no,DOB,Address,gender,result,CGPA from records"
        res.execute(sql)
        # result=store.fetchone()
        result = res.fetchall()
        print(tabulate(result, headers=['id', 'name', 'age', 'ph_no', 'DOB', 'Address', 'gender', 'result', 'CGPA']))
    except Error as e:
        print(e)
    finally:
        res.close()
        con.close()

def select1(id):
    global res
    try:
        res = con.cursor()
        sql = "select id,studentname,age,ph_no,DOB,Address,gender,result,CGPA from records where id=%s"
        data = (id,)
        res.execute(sql,data)
        # result=store.fetchone()
        result = res.fetchall()
        print(tabulate(result, headers=['id', 'name', 'age', 'ph_no', 'DOB', 'Address', 'gender', 'result', 'CGPA']))
    except Error as e:
        print(e)
    finally:
        res.close()
        con.close()

def activity(ids):
    global res
    try:
        res = con.cursor()
        sql = "select id,studentname,skills,performance,rate from activity where id='%s' "
        data=(ids,)
        res.execute(sql,data)
        # result=store.fetchone()
        result = res.fetchall()
        print(tabulate(result, headers=['id', 'studentname', 'skills', 'performance','rate']))
    except Error as e:
        print(e)
    finally:
        res.close()
        con.close()

def insertactivities(id,studentname,skills,performance,rate):
    try:
        store_insert = con.cursor()
        sql = "insert into activity (id,studentname,skills,performance,rate) values (%s,%s,%s,%s,%s)"
        data = (id,studentname,skills,performance,rate)
        store_insert.execute(sql, data)
        con.commit()
        print("Data successfully inserted")
    except Error as e:
        print(e)
# exit
def exit():
    pass

    # sql querys
def fun1():
    print("press 1 it is insert :")
    print("press 2 it is update :")
    print("press 3 it is delete :")
    print("press 4 it is select :")
    print("press 5 it is exit :")
    choice = int(input("Enter the command :"))
    if choice == 1:
        studentname = input("ENter your name :")
        age = int(input("Enter your age :"))
        ph_no = int(input("Enter your Ph-Number :"))
        DOB = input("Enter yor DOB (YYYY-MM-DD):")
        Address = input("Enter your Address :")
        gender = input("Enter your gender :")
        m1 = int(input("Enter M1 :"))
        m2 = int(input("Enter M2 :"))
        m3 = int(input("Enter M3 :"))
        m4 = int(input("Enter M4 :"))
        m5 = int(input("Enter M5 :"))
        import result
        res = result.results(m1, m2, m3, m4, m5)
        CGPA = int(input("Enter your CGPA :"))
        insert(studentname, age, ph_no, DOB, Address, gender, res, CGPA)

    elif choice == 2:
        id = int(input("Enter the user id :"))
        studentname = input("ENter your name :")
        age = int(input("Enter your age :"))
        ph_no = int(input("Enter your Ph-Number :"))
        DOB = input("Enter yor DOB :")
        Address = input("Enter your Address :")
        gender = input("Enter your gender :")
        result = input("Enter your result :")
        CGPA = int(input("Enter your CGPA :"))
        update(studentname, age, ph_no, DOB, Address, gender, result, CGPA, id)

    elif choice == 3:
        id = int(input("Enter the ID :"))
        delete(id)

    elif choice == 4:
        select()

    elif choice == 5:
        exit()

