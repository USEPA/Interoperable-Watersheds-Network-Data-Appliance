from . import session
from app.models.sensors import Sensors
from app.models.organizations import Organizations
from flask_restplus import abort
class GenericModelService(object):
    
    
    def __init__(self, model, name):
        self.model = model
        self.name = name

    
    @property
    def objects(self):
        return self.model.query.all()

    
    def get(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        return obj
    
    
    def create(self, data):
        obj = self.model(**data)
        session.add(obj)
        session.commit()
        return obj
    
    
    def update(self, id, data):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))

        for key, value in data.items():
            setattr(obj,key,value)
        session.commit()
        return obj
    
    
    def delete(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        session.delete(obj)
        session.commit()
        

sensors_service = GenericModelService(Sensors,'Sensor')
organizations_service = GenericModelService(Organizations, 'Organization')