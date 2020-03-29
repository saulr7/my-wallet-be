
import psycopg2
from psycopg2.extras import RealDictCursor
import bcrypt

from config import BD

def add_user(user):
    
    try:
        _validateUserData(user)
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        hashed = bcrypt.hashpw(user.get("password", "").encode(), bcrypt.gensalt())
        cursor.callproc("add_user",(user.get("email"),str(hashed), user.get("firstName"), user.get("lastName"), user.get("uid") ,))
        conn.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
        return "added"
    except (Exception, psycopg2.DatabaseError)  as e:
        print(e)
        raise Exception(e)

def _validateUserData(user):
    
    print(user)
    if user.get("email", "") == "":
        raise Exception("Expected email")
        return
    
    if user.get("password", "") =="":
        raise Exception("Expected password")
        return
    
    if user.get("firstName", "") =="":
        raise Exception("Expected password")
        return

    if user.get("uid", "") =="":
        raise Exception("Expected user Id")
        return