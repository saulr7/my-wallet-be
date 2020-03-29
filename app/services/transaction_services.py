
import psycopg2
from psycopg2.extras import RealDictCursor

from config import BD

from models import transaction_model

def add_transaction(trans):
    
    try:
        _validateUData(trans)
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.callproc("add_transaction",( int( trans.get("CategoryId")), float(trans.get("Amount")), trans.get("UserUID") , str( trans.get("Comment", "")) ,))
        conn.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
        return trans
    except (Exception, psycopg2.DatabaseError)  as e:
        print(e)
        raise Exception(e)

def get_transaction(UserUID):
    
    try:
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.callproc("get_transaction_byUser",( 'PyhKqeLX6ZhezX2EAvyHn1IiW772' ,))
        conn.commit()
        rows = cursor.fetchall()
        responList = []
        for row in rows:
            print(row)
            transaction = transaction_model.transaction_by_user_model(Id= row.get('id', 0),  Category=row.get('category', ""),
            Amount=row.get('amount', 0), CategoryId=  row.get('categoryid', 0), CreatedAtDate=  row.get('createdatdate',"")
            ,Comment= row.get('comment',""))
            responList.append(transaction.toDict())
        cursor.close()
        conn.close()
        responDic = {"data" :  responList}
        return responDic
    except (Exception, psycopg2.DatabaseError)  as e:
        print(e)
        raise Exception(e)

def _validateUData(trans):
    
    if trans.get("CategoryId", 0) == 0:
        raise Exception("Expected categoryId")
        return
    
    if trans.get("Amount", 0) == 0:
        raise Exception("Expected amount")
        return

    if trans.get("UserUID", "") == "":
        raise Exception("Expected user Id")
        return