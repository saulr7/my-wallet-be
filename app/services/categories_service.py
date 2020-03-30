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


def add_category(category):
    
    try:
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.callproc("add_category",( category.get('Category', ''), str(category.get('UserUID', '')) ,))
        conn.commit()
        rows = cursor.fetchall()
        responList = []
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
        return "added"
    except Exception as e:
        raise Exception(e)


def remove_category(categoryId, useruid):
    print(categoryId, useruid)
    try:
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.callproc("remove_category",( int(categoryId), str(useruid) ,))
        conn.commit()
        rows = cursor.fetchall()
        responList = []
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
        return "removed"
    except Exception as e:
        raise Exception(e)