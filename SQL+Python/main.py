import sys
import myconnutils
import hashlib

class login(object):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def start(self):                                               
       self.logins = self.get_logins()                             
       if self.check_login():
           password_from_SQL = self.get_password(self.login)
           for password in password_from_SQL:
               password_1 = password['pass']
           if self.check_password(password_1, self.password):
               print("Login secsessful!")
           else:
               print("Wrong password!") 
       else:
           print("Wrong login!")
        

    def check_password(self, sql_password, urer_password):
        urer_password = urer_password.encode("UTF-8")
        hash_password = hashlib.sha512(urer_password).hexdigest()
        if hash_password == sql_password:
            return True
        else:
            return False


    def check_login(self):
        check = False
        for login in self.logins:
            if login['login'] == self.login:
                check = True
        return check

    def get_logins(self):
        connection = myconnutils.getConnection()
        print ("connect successful!!")
 
        try:
            with connection.cursor() as cursor:
                logins = "SELECT login FROM clients;"    # SQL 
                cursor.execute(logins)                   # Execute Query
                return cursor
        finally:   
            connection.close()

    def get_password(self, login):
        connection = myconnutils.getConnection()
        print ("connect successful!!")
 
        try:
            with connection.cursor() as cursor:
                password = "SELECT pass FROM clients WHERE login = '%s';" % login
                
                cursor.execute(password)
                return cursor
        finally:     
            connection.close()




class registration(object):

    def __init__(self,name, repeat_password, password, login):
        self.name = name,
        self.repeat_password = repeat_password,
        self.password = password,
        self.login = login
    
    def start(self):
        self.logins = login.get_logins(self)
        if(self.check_login()):
            print("This login is already exist!")
        else:
            self.password = self.get_hash(self.password)
            self.repeat_password = self.get_hash(self.repeat_password)
            if (self.password != self.repeat_password):
                print("Passwords do not match")
            else:
                print(self.name, self.login, self.password)
                self.write_new_user_to_BD(self.name, self.login, self.password)

    def get_hash(self, password):
        password = password[0].encode("UTF-8")
        password = hashlib.sha512(password).hexdigest()
        return password

    def write_new_user_to_BD(self, name, login, password):
        connection = myconnutils.getConnection()  
        print ("Connect successful!")
        list = [name[0], login, password]
        sql = "INSERT INTO clients (name,login, pass) VALUES ('%s','%s','%s')" % tuple(list)
        print(sql)
        try :
            cursor = connection.cursor()
            cursor.execute(sql) 
            connection.commit() 
        finally: 
            connection.close()
    
    def check_login(self):
        check = False
        for login in self.logins:
            if login['login'] == self.login:
                check = True
        return check


if __name__ == "__main__":
    if (sys.argv[1]) == 'login':
        log = login(sys.argv[2], sys.argv[3])
        log.start()
        
    elif sys.argv[1] == 'reg':
        reg = registration(sys.argv[5],sys.argv[4], 
                           sys.argv[3],sys.argv[2])
        reg.start()
    else:
        raise IOError("wrong first parametr")
