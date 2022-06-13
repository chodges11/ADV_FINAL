"""
main driver for a simple social network project
"""
# pylint: disable = import-error
# pylint: disable = unused-variable
# pylint:disable=unspecified-encoding


import csv
import time
from loguru import logger
import peewee as pw
import task_model as tm


def init_collections():
    """
    Creates and returns a new instance of the Tasks database.
    """
    tm.db.connect()
    tm.db.execute_sql()
    tm.db.create_tables([
        tm.Tasks
    ])
    tm.db.close()


def list_tasks():
    pass


def complete_task():
    pass


def delete_task():
    pass


def edit_name():
    pass


def edit_description():
    pass


def set_priority():
    pass


def set_id():
    return time.monotonic()


def set_name():
    pass


def set_description():
    pass


def set_start_date():
    pass


def set_due_date():
    pass


def add_new_task():
    """
    Adds a new Task to the database.
    """
    try:
        with tm.db:
            tm.db.connect(reuse_if_open=True)
            new_user = tm.Tasks.create(
                task_id=set_id(),
                task_name=set_name(),
                task_desc=set_description(),
                task_start=set_start_date(),
                task_due=set_due_date(),
                task_priority=set_priority(),
                task_completed=complete_task(),
                task_deleted=delete_task()
            )
            new_user.save()
            logger.info('Add New Task')
            return True

    except pw.PeeweeException as error:
        logger.info(f"{type(error)}: {error}")
        return False