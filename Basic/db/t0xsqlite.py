import sqlite3

def testBase():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('drop table user')

    sql = 'create table user (id varchar(20) primary key, name varchar(20))'
    cursor.execute(sql)
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

def testBase_():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    table = 'testres_{}'.format('202104060323')
    sql = 'create table {}('\
           'id varchar(20) primary key, '\
           'code int, '\
           'description varchar, '\
           'stableinfo varchar, '\
           'testinfo varchar,'\
           'stableurl varchar,'\
           'testurl varchar,'\
           'ssim float'.format(table)
    print(sql)
    table = 'user'
    sql = 'create table user (id varchar(20) primary key, name varchar(20))'

    print(sql)
    # cursor.execute(sql)
    cursor.execute('insert into {} (code, description) values (7, "low ssim")'.format(table))
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()


def test():
    testBase_()
    # testBase()

if __name__ == '__main__':
    test()

    print('{}xx'\
          'xxx'.format(5))
