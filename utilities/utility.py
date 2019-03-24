from helpers.database import db_session

class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()

def update_entity_fields(entity, **kwargs):
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity
