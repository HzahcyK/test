import pymysql

def get_all(sql):
    connect = pymysql.connect(host="10.10.10.249", port=5432, user="root", password="tF!e5UN?iGMRkB7Z80Ln#O@uCsP^mS", db="dj_analytics")
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    connect.close()
    return result

def get_one(sql):
    connect = pymysql.connect(host="10.10.10.249", port=5432, user="root", password="tF!e5UN?iGMRkB7Z80Ln#O@uCsP^mS", db="dj_analytics")
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    cursor.close()
    connect.close()
    return result