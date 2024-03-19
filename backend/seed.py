from app import app
from models import db, Fighter, Event, Match,User,Comment
from faker import Faker
from random import randint, choice, choices, uniform
# import requests


fake = Faker()

if __name__ == "__main__":
    with app.app_context():
        Fighter.query.delete()
        Event.query.delete()
        Match.query.delete()
        Comment.query.delete()
        User.query.delete()

        fighter_list=[]
        for _ in range(10):
            f=Fighter(name=fake.name())
            fighter_list.append(f)
        db.session.add_all(fighter_list)
        db.session.commit()

        event_list=[]
        for _ in range(10):
            e=Event(location=fake.sentence(),event_num=randint(1,300))
            event_list.append(e)
        db.session.add_all(event_list)
        db.session.commit()

        match_list=[]
        for _ in range(15):
            m=Match(fighter_1_name=str(choice(fighter_list).name), fighter_2_name=str(choice(fighter_list).name))
            match_list.append(m)
        db.session.add_all(match_list)
        db.session.commit()

