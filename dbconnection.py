from dbm import _Database
from multiprocessing import connection
import pymysql.cursors


def createDBConnection():
    connection = pymysql.connect(
        host="localhost", #127.0.0.1
        user="root",
        password="S##48K@qirt",
        database="specialtodolistdb",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor, #[DictCursors]
    )
    return connection
