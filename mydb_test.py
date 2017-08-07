import pytest

from mydb import MyDB

@pytest.fixture
def cur():
    print "\nopen DB"
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    conn.close()
    curs.close()
    print "\nclose DB"
    
def test_john_id(cur):
    id = cur.execute("select id from employees where name = John")
    assert id == 123