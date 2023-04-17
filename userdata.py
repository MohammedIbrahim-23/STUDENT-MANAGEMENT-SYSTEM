
import re
def email(gmail):
    email = gmail
    # a = r'[a-z0-9_\.\-]+[@a-z]+[\.][a-z]'
    # b = re.compile(a)
    result = re.fullmatch(r'[a-z0-9_\.\--]+[@a-z]+[\.][a-z]', email)
    if result:
        return email
    else:
        print("Invalid")

admin_email = input("Enter the email :")
email(admin_email)

# password
def password(admin_password):
    pas = admin_password
    a = r'[A-Za-z]+[@ # %][0-9a-z]'
    c = re.compile(a)
    b = re.fullmatch(r'[A-Za-z]+[@ # %][0-9a-z]', pas)
    if b:
        return b
    else:
        print("Invalid")

password(admin_password=input("Enter your password :"))

# phno checking
# import re
# ph=input()
# d=r'[9][0-9$]'
# e=re.compile(d)
# f=re.search(e,ph)
# if f and len(ph)==10:
#     print("valid")
# else:
#     print("not")