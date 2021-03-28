
from .db_session import db_session, engine
from .base import Base
import csv


def init_db():
    from ..models.users import Users
    from ..models.vendors import Vendors

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    user = Users(first_name="Test", last_name="User")
    db_session.add(user)

    # db_session.add(Vendors(
    #             name="Bitly",
    #             category="Software",
    #             external_link="https://bitly.com/",
    #             description="Bitly is used by businesses",
    #             status=1,
    #             risk="High",
    #             tier="Tier 3"
    #         ))
    with open('vendors.csv', 'r') as f:
        for i, line in enumerate(csv.reader(f)):
            if i == 0: continue
            name, category, website, description, status, risk, tier = line
            db_session.add(Vendors(
                name=name,
                description=description,
                external_link=website,
                category=category,
                status=int(status),
                risk=risk,
                tier=tier
            ))
    db_session.commit()
