from flask_restplus import abort
from . import domains , sensors, organizations, session, schemas


class GenericModelService(object):
    
    
    def __init__(self, model, schema, name):
        self.model = model
        self.schema = schema
        self.name = name


    def __deserialize__(self, data):
        if self.schema is not None:
            return self.schema.load(data,session=session).data
        else:
            return self.model(**data)

    @property
    def objects(self):
        return self.model.query.all()
    
    def get(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        return obj
    
    def create(self, data):
        obj = self.__deserialize__(data)
        session.add(obj)
        session.commit()
        return obj
    
    def update(self, id, data):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        if self.schema is not None:
            obj = self.schema.load(data, session=session, instance=obj, partial=True)
        else:
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
        

sensors_service = GenericModelService(sensors.Sensors,schemas.SensorSchema(),'Sensor')
parameter_service = GenericModelService(domains.Parameters, schemas.ParameterSchema(), 'Parameter')
units_service = GenericModelService(domains.Units, schemas.UnitSchema(), 'Unit')
medium_service = GenericModelService(domains.MediumTypes, schemas.MediumTypeSchema(), 'Medium Type')
quality_check_operand_service = GenericModelService(domains.QualityCheckOperands, schemas.QualityCheckOperandSchema(), 'Quality Check Operand')
quality_check_action_service = GenericModelService(domains.QualityCheckActions, schemas.QualityCheckActionSchema(), 'Quality Check Action')
data_qualifier_service = GenericModelService(domains.DataQualifiers, schemas.DataQualifierSchema(), 'Data Qualifier')
organizations_service = GenericModelService(organizations.Organizations, schemas.OrganizationSchema(), 'Organization')
