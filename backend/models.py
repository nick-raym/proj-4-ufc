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
    # serialize_rules= ['-order_parts.part']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    nickname = db.Column(db.String,nullable=True)
    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    draws = db.Column(db.Integer, nullable=False)

    height_cm = db.Column(db.Float, nullable=True)
    weight_in_kg = db.Column(db.Float, nullable=True)
    reach_in_cm = db.Column(db.Float, nullable=True)

    stance = db.Column(db.String, nullable=True)
    date_of_birth = db.Column(db.String, nullable=True)
    significant_strikes_landed_per_minute = db.Column(db.Float, nullable=True)
    significant_striking_accuracy = db.Column(db.Float, nullable=True)
    significant_strikes_absorbed_per_minute = db.Column(db.Float, nullable=True)
    significant_strike_defence = db.Column(db.Float, nullable=True)
    average_takedowns_landed_per_15_minutes = db.Column(db.Float, nullable=True)
    takedown_accuracy = db.Column(db.Float, nullable=True)
    takedown_defense = db.Column(db.Float, nullable=True)
    average_submissions_attempted_per_15_minutes = db.Column(db.Float, nullable=True)

class Event(db.Model, SerializerMixin):
    __tablename__ = "event_table"
    serialize_rules= ['-event_matches.event']
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    event_num=db.Column(db.String, nullable=False)
    #### match_id = db.Column(db.Integer, db.ForeignKey("match_table.id"))
    # part_id = db.Column(db.Integer, db.ForeignKey("part_table.id"))
    event_matches = db.relationship("Match",back_populates="event")
    # part = db.relationship("Part",back_populates="order_parts")

# class Fighter_Match(db.Model, SerializerMixin):
#     __tablename__ = "fighter_match_table"
    
#     match_id = db.Column(db.Integer, db.ForeignKey("match_table.id"), primary_key=True)
#     fighter_id = db.Column(db.Integer, db.ForeignKey("fighter_table.id"), primary_key=True)


class Match(db.Model, SerializerMixin):
    __tablename__ = "match_table"
    serialize_rules= ['-event.event_matches','-comments.matches']
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event_table.id"))
    fighter1_id = db.Column(db.Integer, db.ForeignKey("fighter_table.id"))
    fighter2_id = db.Column(db.Integer, db.ForeignKey("fighter_table.id"))

    fighter1 = db.relationship("Fighter", foreign_keys=[fighter1_id])
    fighter2 = db.relationship("Fighter", foreign_keys=[fighter2_id])
    
    comments=db.relationship("Comment",back_populates="matches")
    event=db.relationship("Event",back_populates="event_matches")
    # event relationship one


class User(db.Model, SerializerMixin):
    __tablename__ = "user_table"
    serialize_rules = ["-comments.user"]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    # we store the hash of the password, not the password itself
    # DO NOT store the password itself
    password_hash = db.Column(db.String)
    comments = db.relationship("Comment", back_populates="user")

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comment_table"
    serialize_rules = ["-matches.comments", '-user.comments']
    # canvas serialize_rules = ('-restaurant.reviews',)
    id = db.Column(db.Integer, primary_key=True)
    # rating = db.Column(db.Integer)
    review = db.Column(db.String)
    reviewer_id = db.Column(db.Integer, db.ForeignKey("user_table.id"))
    match_id = db.Column(db.Integer, db.ForeignKey("match_table.id"))

    user = db.relationship("User", back_populates="comments")
    matches = db.relationship("Match", back_populates="comments")
