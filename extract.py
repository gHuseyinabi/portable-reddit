from sqlite3 import connect as sqlite3_connect
from querys import *


datafile = input("Please write .db name:")

connection_sql = sqlite3_connect(datafile)

cursor = connection_sql.cursor()

cursor.execute(tablo_goster)


def vaild(query) -> bool:
    return query != null


def WriteThumbnail(filename, data) -> bool:
    if vaild(data):
        open(filename, "wb").write(data)
        return True
    else:
        return False


def WriteSelfText(filename, data, **kwargs) -> bool:
    if vaild(data):
        open(filename, "w", **kwargs).write(data)
        return True
    else:
        return False


result = cursor.fetchall()
index = 0

# Post indexleri:
# post_id
# selftext
# thumbnail
# title
# author
# permalink


for post in result:
    selftext = post[1]
    thumbnail = post[2]
    id = post[0]
    if vaild(thumbnail):
        if WriteThumbnail(f"{id}.png", thumbnail):
            index = 1
    elif vaild(selftext):
        if WriteSelfText(f"{id}.txt", selftext, encoding="utf-8"):
            index = 1


print("Found total of {} posts in {}".format(index, datafile))
