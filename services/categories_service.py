import psycopg2
from psycopg2.extras import RealDictCursor

from config import BD
from models import categories_by_useruid

def get_categories():
    
    try:
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.callproc("get_categories_by_useruid",('PyhKqeLX6ZhezX2EAvyHn1IiW772' ,))
        conn.commit()
        rows = cursor.fetchall()
        responList = []
        for row in rows:
            print(row)
            category = categories_by_useruid.categories_by_useruid_model(Id= row.get('id', 0),  Category=row.get('category', ""))
            responList.append(category.toDict())
        cursor.close()
        conn.close()
        responDic = {"data" :  responList}
        return responDic
    except Exception as e:
        raise Exception(e)