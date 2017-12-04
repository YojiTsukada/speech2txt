DEBUG = True
TEMPLATE_DEBUG = DEBUG

dbh = pymysql.connect(
    host='35.184.212.142',
    user='root',
    password='all4one',
    db='yoj001',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
    )
