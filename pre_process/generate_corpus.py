import pymysql.cursors

comments = 'comments.txt'
shop_ids = 'shop_ids.txt'

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='shops',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "SELECT `content`, `shop_id` FROM `home_comment`"
        cursor.execute(sql)
        # debug
        with open(comments, 'w') as fc:
            with open(shop_ids, 'w') as fs:
                comment = ""
                shop_id = 0
                while True:
                    temp = cursor.fetchone()
                    if not temp == None:
                        comment = temp['content'] + "\n"
                        fc.write(comment)
                        shop_id = str(temp['shop_id']) + "\n"
                        fs.write(shop_id)
                    else:
                        break
finally:
    connection.close()