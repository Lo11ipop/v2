from ..services import celery_dao_services

def get_last_exports(id):
    return celery_dao_services.get_last_exports(id)

def get_lists_row(param, form):
    return celery_dao_services.get_lists_row(param,form)

def update_exports(fname, id):
    celery_dao_services.update_exports(fname,id)