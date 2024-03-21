from app import app
from models import db, Fighter, Event, Match, User, Comment
from faker import Faker
from random import randint, choice, choices, uniform
import json
from flask_bcrypt import Bcrypt
# import requests


fake = Faker()

if __name__ == "__main__":
    with app.app_context():
        bcrypt = Bcrypt(app)
        data = {}
        # get the json as a dict
        with open("db.json") as f:
            data = json.load(f)
        
        Fighter.query.delete()
        Event.query.delete()
        Match.query.delete()
        Comment.query.delete()
        User.query.delete()

        fighter_list=[]
        for d in data["fighters"]:
            # read the data from the dict into a Restaurant object
            f = Fighter(
                name=d.get("name"),
                nickname=d.get("nickname"),
                wins=d.get("wins"),
                losses=d.get("losses"),
                draws=d.get("draws"),
                height_cm=d.get("height_cm"),
                weight_in_kg=d.get("weight_in_kg"),
                reach_in_cm=d.get("reach_in_cm"),
                stance=d.get("stance"),
                date_of_birth=d.get("date_of_birth"),
                significant_strikes_landed_per_minute=d.get("significant_strikes_landed_per_minute"),
                significant_striking_accuracy=d.get("significant_striking_accuracy"),
                significant_strikes_absorbed_per_minute=d.get("significant_strikes_absorbed_per_minute"),
                significant_strike_defence=d.get("significant_strike_defence"),
                average_takedowns_landed_per_15_minutes=d.get("average_takedowns_landed_per_15_minutes"),
                takedown_accuracy=d.get("takedown_accuracy"),
                takedown_defense=d.get("takedown_defense"),
                average_submissions_attempted_per_15_minutes=d.get("average_submissions_attempted_per_15_minutes"),
            )
            fighter_list.append(f)
        db.session.add_all(fighter_list)
        db.session.commit()

        event_list=[]
        for _ in range(10):
            e=Event(location=fake.sentence(),event_num=randint(1,300))
            event_list.append(e)
        db.session.add_all(event_list)
        db.session.commit()

        match_list = []
        for _ in range(15):
            fighter_1 = choice(fighter_list)
            fighter_2 = choice(fighter_list)
            while(fighter_1==fighter_2):
                fighter_2 = choice(fighter_list)
            event_choice = choice(event_list)
            m = Match(fighter1_id=fighter_1.id, fighter2_id=fighter_2.id, event_id = event_choice.id)
            match_list.append(m)
        db.session.add_all(match_list)
        db.session.commit()


