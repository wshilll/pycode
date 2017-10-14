import pymssql

try:
    conn = pymssql.connect(host='localhost',
                           user='sa',
                           password='1',
                           charset='GBK',
                           database='suihuasignet')

    cur = conn.cursor()

    if not cur:
        print('数据库连接失败...')
    else:
        print('数据库连接成功...')

    ID_id=input("请输入编号：")
    content_con=input("请输入印章内容：")
    print(type(ID_id))
    print(type(content_con))
    if ID_id == '':
        Sslect = "select * from t_signet WHERE se_content like '%s%%'" % content_con
        print(Sslect)
    elif content_con == '':
        Sslect = "select * from t_signet WHERE se_signet_id like '%s%%'" % ID_id
        print(Sslect)
    else:
        Sslect = "select * from t_signet WHERE se_signet_id='%s%%'or se_content='%s%%'" % \
                 (ID_id, content_con)
        print(Sslect)
    cur.execute(Sslect)
    result = cur.fetchall()
    print(result)
except Exception as e:
    print(e)
