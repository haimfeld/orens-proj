class dataManeger():
    host = 'localhost'
    user = 'root'
    password = '9246865'
    database = 'licence_plate_proj'
    conn =[]
    sql =[]


    def __init__(self):

        import pymysql
        self.sql = pymysql


    def connectDB(self):
        try:
            self.conn = self.sql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                DB=self.database)
        except Exception:
            print('cant connect to database')

    def ShowAllData(self):

        conncDB = self.conn.cursor()
        conncDB.execute("SELECT * FROM car_num_names")
        print(conncDB.description)

        for row in conncDB:
            print(row)