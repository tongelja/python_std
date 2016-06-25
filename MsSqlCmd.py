

import sys, getpass
try:
    import pypyodbc
except:
    print('Unable to import python modules')
    sys.exit(2)


class mssqlConsole:
    def __init__(self):
        self.type      = 'SQLServer'
        self.conn = None
        self.curs = None
        self.results = []

    def open(self, server=None, user=None, password=None, port=1433):
        if server is None:
            server = input('Server ==> ')

        if user is None:
            user = input('User ==>')

        if password is None:
            password = getpass.getpass('Password ==>')

        print('Connecting to ' + user + '/*********' + '@' + server + ':' + str(port)  )
        conn_string = 'driver=/usr/local/lib/libtdsodbc.so;server=' + server + ';port=' + str(port) + ';uid=' + user + ';pwd=' + password
        conn = pypyodbc.connect(conn_string)
        self.conn = conn 

    def __sql_prompt__(self):
        sql_stmt = input('\nTSQL> ')
        return sql_stmt

    def __parse_sql__(self, sql_stmt):
        if self.conn == 'None':
                print('\nERROR: No SQL Connection')
                sys.exit(2)

        self.curs = self.conn.cursor()
        output = self.curs.execute(sql_stmt)

        self.results = []
        for r in output:
            self.results.append(r)

        for i in self.results:
            print('\n', end='')
            for j in range(len(i)):
                print(i[j], end='')

    def cmd(self):
        if self.conn is None:
            print('No Connection')
            sys.exit(2)

        while True:
            sql_stmt = self.__sql_prompt__()
            if sql_stmt.upper() == 'EXIT':
                break
            elif sql_stmt.upper() == '':
                pass
            else:
                self.__parse_sql__(sql_stmt)

