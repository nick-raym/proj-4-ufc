from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string, datetime

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Fighter(db.Model, SerializerMixin):
    __tablename__ = "fighter_table"
    serialize_rules= ['-order_parts.part']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # price = db.Column(db.Integer, nullable=False)
    # order_parts = db.relationship("Order_Part",back_populates="part")

class Event(db.Model, SerializerMixin):
    __tablename__ = "event_table"
    # serialize_rules= ['-part.order_parts','-order.order_parts']
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    event_num=db.Column(db.String, nullable=False)
    # order_id = db.Column(db.Integer, db.ForeignKey("order_table.id"))
    # part_id = db.Column(db.Integer, db.ForeignKey("part_table.id"))
    # order = db.relationship("Order",back_populates="order_parts")
    # part = db.relationship("Part",back_populates="order_parts")


class Match(db.Model, SerializerMixin):
    __tablename__ = "match_table"
    # serialize_rules= ['-order_parts.order','-customer.orders']
    id = db.Column(db.Integer, primary_key=True)
    fighter_1_name = db.Column(db.String, nullable=False)
    fighter_2_name = db.Column(db.String, nullable=False)
    # customer_id = db.Column(db.Integer, db.ForeignKey("customer_table.id"))
    # customer = db.relationship("Customer", back_populates="orders")
    # order_parts = db.relationship("Order_Part",back_populates="order")
    comments=db.relationship("Comment",back_populates="match")


class User(db.Model, SerializerMixin):
    __tablename__ = "user_table"
    serialize_rules = ["-reviews.user"]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    # we store the hash of the password, not the password itself
    # DO NOT store the password itself
    password_hash = db.Column(db.String)
    comments = db.relationship("Comment", back_populates="user")

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comment_table"
    serialize_rules = ["-match.comments", '-user.comments']
    # canvas serialize_rules = ('-restaurant.reviews',)
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
    reviewer_id = db.Column(db.Integer, db.ForeignKey("user_table.id"))

    user = db.relationship("User", back_populates="comments")
    match = db.relationship("Match", back_populates="comments")