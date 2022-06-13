"""
Implement a SQL database, using the PeeWee ORM, that will contain both user
account and well as user status data.
"""

# pylint: disable=too-few-public-methods

import os
import peewee as pw
from loguru import logger

FILE = 'tasks.db'
if os.path.exists(FILE):
    os.remove(FILE)

db = pw.SqliteDatabase(FILE)


class DBModel(pw.Model):
    """This model uses the PeeWee Model."""
    logger.info("Database class extending PeeWee Model.")

    class Meta:
        """Override the default name by specifying a table_name attribute."""
        database = db


class Tasks(DBModel):
    """
        This class defines tasks.
    """
    logger.info("Tasks")
    task_id = pw.CharField(primary_key=True, max_length=30)
    task_name = pw.CharField(max_length=30, null=False)
    task_desc = pw.CharField(max_length=140, null=False)
    task_start = pw.CharField(max_length=10)
    task_due = pw.DateField(max_length=10)
    task_priority = pw.IntegerField()
    task_completed = pw.BooleanField(default=False)
    task_deleted = pw.BooleanField(default=False)
