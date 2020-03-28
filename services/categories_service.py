import psycopg2
from psycopg2.extras import RealDictCursor

from config import BD
from models import category_model

def get_categories():
    
    try:
        conn = psycopg2.connect(BD.CONNECT_STR)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM USERS")
        conn.commit()
        rows = cursor.fetchall()
        responList = []
        for row in rows:
            # print(row)
            category = category_model.category_model(Id= row.get('id', 0), Active= row.get('active',False), Category=row.get('category', "")
            , CategoryTypeId= row.get('categorytypeid', 0), CreatedAtDate=row.get('createdatdate', ""), 
            CreatedAtTime= row.get('createdattime', ""), UpdatedAt= row.get('updatedat', ""), CreatedBy= row.get('createdby', 0))
            responList.append(category.toDict())
        cursor.close()
        conn.close()
        responDic = {"data" :  responList}
        return responDic
    except Exception as e:
        raise Exception(e)