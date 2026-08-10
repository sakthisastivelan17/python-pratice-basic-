s_username='emc'
s_password=123

uname=input('enter the username :')
password=int(input('enter the password:'))

def validate():
    if (s_username==uname and s_password==password):
        return True
    else:
        return False

a=validate()
print(a)
            
