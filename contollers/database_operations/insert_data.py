from models import Session

# 2 - extract a session
session = Session()


def insert_data(object):
    session.add(object)
    session.commit()
    print(object.id)


def bulk_insert(object_list):
    session.bulk_save_objects(object_list)
    session.commit()

