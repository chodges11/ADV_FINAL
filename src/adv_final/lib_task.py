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
    """Updates the task name."""

    task_id = input('Task ID: ')
    task_name = input('New Task Name: ')

    try:
        with tm.db:
            tm.db.connect(reuse_if_open=True)
            task = tm.Tasks.get(tm.Tasks.task_id == task_id)
            task.task_name = task_name
            task.save()
            logger.info('Update Task Name.')
            return True

    except pw.DoesNotExist as error:
        print("Task Name was not successfully updated.\n")
        logger.info(f"{type(error)}: {error}")
        return False


def edit_description():
    """Updates the task description."""

    task_id = input('Task ID: ')
    task_desc = input('New Task Description(140 char max): ')

    try:
        with tm.db:
            tm.db.connect(reuse_if_open=True)
            task = tm.Tasks.get(tm.Tasks.task_id == task_id)
            task.task_desc = task_desc
            task.save()
            logger.info('Update Task Description.')
            print("Task Description was not successfully updated.\n")

    except pw.DoesNotExist as error:
        print("Task Description was not successfully updated.\n")
        logger.info(f"{type(error)}: {error}")
        return False


def set_priority():
    return input('Task Priority(Zero is highest): ')


def set_id():
    return time.monotonic()


def set_name():
    return input('Task Name: ')


def set_description():
    return input('Task Description(140 char max): ')


def set_start_date():
    return input('Task Start Date: ')


def set_due_date():
    return input('Task Due Date: ')


def add_new_task():
    """
    Adds a new Task to the database.
    """

    try:
        with tm.db:
            tm.db.connect(reuse_if_open=True)
            new_task = tm.Tasks.create(
                task_id=set_id(),
                task_name=set_name(),
                task_desc=set_description(),
                task_start=set_start_date(),
                task_due=set_due_date(),
                task_priority=set_priority(),
                task_completed="Uncompleted",
                task_deleted="False"
            )
            new_task.save()
            logger.info('Add New Task')

    except pw.PeeweeException as error:
        print("An error occurred while trying to add new task.\n")
        logger.info(f"{type(error)}: {error}")
