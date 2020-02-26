import pymysql.cursors  
 
def getConnection():                                
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',                             
                                 db='clients',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
