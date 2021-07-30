from enum import unique
from typing import Text
from peewee import *

db = SqliteDatabase('db/database.db')
db.connect()


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'



class User(BaseModel):
    username = TextField()
    email = TextField()
    unique_key = TextField()

    class Meta:
        db_table = 'users'


class Chat(BaseModel):
    chatname = TextField()

    class Meta:
        db_table = 'chats'


class Message(BaseModel):
    user_id = ForeignKeyField(User)
    message_text = TextField()
    chat_id = ForeignKeyField(Chat)
    date = DateField()

    class Meta:
        db_table = 'messages'


