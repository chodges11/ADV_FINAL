"""
Main driver for a simple social network project
"""
# pylint: disable = import-error
# pylint: disable = unused-variable
# pylint:disable=unspecified-encoding


import csv
import time
from datetime import datetime

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


def list_tasks_sorted_by_num():
    for task in tm.Tasks.select():
        print(task.username)  # TODO: Format all the task information


def list_tasks_sorted_by_priority():
    for task in tm.Tasks.select():
        print(task.username)  # TODO: Format all the task information


def list_tasks_sorted_by_due_date():
    for task in tm.Tasks.select():
        print(task.username)  # TODO: Format all the task information


def list_closed_tasks_between_dates():
    for task in tm.Tasks.select():
        print(task.username)  # TODO: Format all the task information


def list_overdue_tasks():
    for task in tm.Tasks.select():
        print(task.username)  # TODO: Format all the task information


def complete_task():
    """Completes the task."""

    task_id = input('Task ID: ')

    try:
        with tm.db:
            tm.db.connect(reuse_if_open=True)
            task = tm.Tasks.get(tm.Tasks.task_id == task_id)
            task.task_completed = "Completed"
            task.save()
            logger.info('Complete Task.')

    except pw.DoesNotExist as error:
        print("Task was not successfully marked as completed.\n")
        logger.info(f"{type(error)}: {error}")


def delete_task():
    """Deletes the task."""

    task_id = input('Task ID: ')

    try:
        with tm.db:
            tm.db.connect(reuse_if_open=True)
            task = tm.Tasks.get(tm.Tasks.task_id == task_id)
            task.task_deleted = "Deleted"
            task.save()
            logger.info('Deletes Task.')

    except pw.DoesNotExist as error:
        print("Task was not successfully marked as deleted.\n")
        logger.info(f"{type(error)}: {error}")


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

    except pw.DoesNotExist as error:
        print("Task Name was not successfully updated.\n")
        logger.info(f"{type(error)}: {error}")


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


def set_priority():
    return str(input('Task Priority(Zero is highest): '))


def set_id():
    return time.monotonic()


def set_name():
    return input('Task Name: ')


def set_description():
    return input('Task Description(140 char max): ')


def set_start_date():

    return datetime.strptime(
        input("Enter Task Start Date in format MM/DD/YYYY: "),
        "%m/%d/%Y"
    )


def set_due_date():
    return datetime.strptime(
        input("Enter Task Due Date in format MM/DD/YYYY: "),
        "%m/%d/%Y"
    )


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
