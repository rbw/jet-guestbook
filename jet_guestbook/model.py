# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import Model, ForeignKeyField, CharField, DateTimeField


class VisitorModel(Model):
    class Meta:
        table_name = 'visitor'
        indexes = (
            (('name', 'ip_addr'), True),
        )

    name = CharField()
    ip_addr = CharField()
    location = CharField(null=True)


class VisitModel(Model):
    class Meta:
        table_name = 'visit'

    created_on = DateTimeField(default=datetime.now)
    message = CharField(null=False)
    visitor = ForeignKeyField(VisitorModel)

    @classmethod
    def extended(cls, *fields):
        return cls.select(VisitModel, VisitorModel, *fields).join(VisitorModel)

