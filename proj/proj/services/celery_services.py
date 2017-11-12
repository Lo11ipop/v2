from ..dao import celery_dao

def get_last_exports(id):
    return celery_dao.get_last_exports(id)

def get_lists_row(param, form):
    return celery_dao.get_lists_row(param,form)

def update_exports(fname, id):
    celery_dao.update_exports(fname,id)