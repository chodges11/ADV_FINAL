"""
main driver for a simple social network project
"""
# pylint: disable = import-error
# pylint: disable = unused-variable
# pylint:disable=unspecified-encoding


import csv
from loguru import logger
import peewee as pw
import task_model as tm

def init_collections():
    """
    Creates and returns a new instance of the database.
    """
    tm.db.connect()
    tm.db.execute_sql('PRAGMA foreign_keys = ON;')
    tm.db.create_tables([
        tm.Tasks,
    ])
    tm.db.close()

def add_new_task():
    pass


def list_tasks():
    pass


def set_start_date():
    pass


def set_due_date():
    pass


def complete_task():
    pass


def delete_task():
    pass


def change_name():
    pass


def edit_description():
    pass
