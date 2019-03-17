from huey.contrib.sqlitedb import SqliteHuey

huey = SqliteHuey('db.sqlite3')

@huey.task()
def handling(request):
    