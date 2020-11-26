import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '10.0.0.69'
database = 'mydb'
username = 'sa'
password = 'Karthik@123'


try:
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate)

#print(cursor)
# conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=server.domain.local;PORT=1433;UID=DOMAIN\user;PWD=mypassword;DATABASE=mydatabasename;UseNTLMv2=yes;TDS_Version=8.0;Trusted_Domain=domain.local;')
# cursor = conn.cursor()
#print(s_code)
s_code="mytable"

string = "CREATE TABLE  "+s_code+"(Name varchar(15), Age integer, City varchar(50))"
cursor.execute(string)
# cursor.execute("SELECT * FROM TestTable")
# #cursor.execute('SELECT * FROM TestDB.dbo.Person')
#
cursor.execute('''
                INSERT INTO TestTable (Name, Age, City)
                VALUES
                ('Bob',55,'Montreal'),
                ('Jenny',66,'Boston')
                ''')
cnxn.commit()
r=cursor.execute('SELECT * FROM mytable')
#rows = cursor.fetchall()
#for i in rows:
print(r)