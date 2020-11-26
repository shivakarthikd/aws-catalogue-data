#from test import ser_cat,s_code
import mysql.connector



def uploadtodb(ser_cat,s_code,diffkeys):
    table_service_list=[]
    mydb = mysql.connector.connect(
        host="db host",
        user="db user",
        port="3360",
        password="db password",
        database="db name"
    )
    coloumns=''
    for i in ser_cat.keys():
        coloumns=coloumns+ '`'+ i +'` varchar(255),'
    #
    # coloumns=','.join(rds_cat.keys())
    # print(coloumns)
    # for i in rds_cat.values():
    #     values=values+' '+str(i)+','
    cursor=mydb.cursor()
    columns = ', '.join('`'+x+'`' for x in ser_cat.keys())
    values = ', '.join('\''+x+'\'' for x in ser_cat.values())
    #values=','.join(rds_cat.values())
    #print(values)
    coloumns=coloumns[:-1]
    print(columns, values, coloumns)
    #print(coloumns)
    # cursor.execute('drop table if exists '+ s_code)
    query=" create table if not exists "+s_code+"_table(id INT AUTO_INCREMENT PRIMARY KEY, "+coloumns+");"
    print(query)
    cursor.execute(query)
    cursor.execute("show columns from "+s_code+"_table;")
    rs=cursor.fetchall()
    for i in rs:
        table_service_list.append(i[0])

    if diffkeys != {}:
        for col in diffkeys:
            if col not in table_service_list:
                alt_query='ALTER TABLE '+s_code+'_table ADD  `'+ col +'` varchar(255)'
                cursor.execute(alt_query)
    #insterquery='INSERT INTO '+s_code+'( Name ) VALUES('+ values+')'

    sql = 'INSERT INTO ' + s_code +'_table'+'('+columns+') values('+values+');'
    #cursor.execute('''INSERT INTO '''+ s_code +'''()('''+ values +'')''')
    cursor.execute(sql)
    mydb.commit()
    mydb.close()
    # cursor.execute('SELECT * FROM AWSDatabaseMigrationSvc_table')
    # rows = cursor.fetchall()
    # for i in rows:
    #     print(i)