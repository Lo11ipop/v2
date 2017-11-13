from celery import Celery
from .services import celery_dao_services
import datetime
from openpyxl.workbook import Workbook
import time

app = Celery('tasks', broker = 'redis://localhost/0')

@app.task
def crrfil(id):
    time.sleep(10)
    woa = 'Without amount'
    wa = 'With the amount'
    param = celery_dao_services.get_last_exports(id)

    if param[0][0] == woa:
        rows = celery_dao_services.get_lists_row(param, 1)
    if param[0][0] == wa:
        rows = celery_dao_services.get_lists_row(param, 0)

    wb = Workbook()
    ws = wb.active
    rows_name = [['Name', 'created', 'updated', ]]
    if param[0][0] == wa:
        rows_name = [['Name', 'price', 'created', 'updated', ]]
    for row in rows_name:
        ws.append(row)

    for row in rows:
        ws.append(row)
    fname = "/tmp/date%s.xlsx" % (datetime.datetime.now())
    wb.save(fname)

    celery_dao_services.update_exports(fname, id)

