import psycopg2
from psycopg2.extras import RealDictCursor

from app.config import BD
from app.models import categories_by_useruid

def get_categories(useruid):
    
    try:
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.callproc("get_categories_by_useruid",(str(useruid) ,))
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