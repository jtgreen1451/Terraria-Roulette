from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import random

from db_models import *


engine = create_engine("sqlite:///./terraria.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


stage_map = {
    "pre-boss": "1 pre-boss",
    "pre-hm": "2 pre-hm",
    "pre-mech": "3 pre-mech",
    "pre-plant": "4 pre-plant",
    "pre-golem": "5 pre-golem",
    "pre-lunar": "6 pre-lunar",
    "post-moonlord": "7 post-moonlord"
}

accessory_stage_map = {
    "pre-boss": "1 pre-boss",
    "pre-skeletron": "2 pre-skeletron",
    "pre-hm": "3 pre-hm",
    "pre-mech": "4 pre-mech",
    "pre-plant": "5 pre-plant",
    "pre-golem": "6 pre-golem",
    "pre-lunar": "7 pre-lunar",
    "post-moonlord": "8 post-moonlord"
}

stages = [
    "pre-boss",
    "pre-hm",
    "pre-mech",
    "pre-plant",
    "pre-golem",
    "pre-lunar",
    "post-moonlord"
]

acc_stages = [
    "pre-boss",
    "pre-skeletron",
    "pre-hm",
    "pre-mech",
    "pre-plant",
    "pre-golem",
    "pre-lunar",
    "post-moonlord"
]

wep_amount = 2 # amount of weapons per stage
acc_amount = 5 # amount of accessories per stage

def random_weapons(stage):
    with Session() as session:

        stmt = select(WeaponDB).where(
        WeaponDB.Stage == stage_map[stage]
        )

        weapons = session.scalars(stmt).all()

        count = min(wep_amount, len(weapons))
        random_weapons = random.sample(weapons, count)

        for weapon in random_weapons:
            print(f"{weapon.Name}, {weapon.Image}")


def random_accessories(stage):
    with Session() as session:

        stmt = select(AccessoryDB).where(
            AccessoryDB.Stage == accessory_stage_map[stage]
        )

        accessories = session.scalars(stmt).all()

        count = min(acc_amount, len(accessories))

        if stage in ["pre-boss", "pre-skeletron", "pre-hm"]:
            count = min(acc_amount - 1, len(accessories))

        selected_accessories = random.sample(accessories, count)

        for accessory in selected_accessories:
            print(f"{accessory.Name}, {accessory.Image}")


for stage in stages:
    print("=" * 90)
    print(f"Stage: {stage}")
    random_weapons(stage)

print("=" * 90)
print("")

for stage in acc_stages:
    print("=" * 90)
    print(f"Stage: {stage}")
    random_accessories(stage)
print("=" * 90)