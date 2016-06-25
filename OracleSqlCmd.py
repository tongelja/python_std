

import sys, getpass
try:
    import cx_Oracle
except:
    print('Unable to import python modules')
    sys.exit(2)


class oraConsole:
    def __init__(self):
        self.type      = 'Oracle'
        self.conn = None
        self.curs = None

    def open(self, server=None, database=None, user=None, password=None):
        if server is None:
            server = input('Server ==> ')

        if database is None:
            database = input('Database ==> ')

        if user is None:
            user = input('User ==>')

        if password is None:
            password = getpass.getpass('Password ==>')

        if user.upper() == 'SYS':
            mode =  cx_Oracle.SYSDBA
        else: 
            mode = ''
        dsn = server + ':1521/' + database
        print('Connecting to ' +dsn)
        conn = cx_Oracle.connect(user, password, dsn, mode) 
        self.conn = conn 

    def cmd(self):
        sql_stmt = input('SQL> ')
        self.curs = self.conn.cursor()
        self.curs.execute(sql_stmt)
        
