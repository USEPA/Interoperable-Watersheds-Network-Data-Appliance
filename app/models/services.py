from flask_restplus import abort
from . import domains , sensors, organizations, session, schemas


class GenericModelService(object):
    
    
    def __init__(self, model, schema, name):
        self.model = model
        self.schema = schema
        self.name = name

    @property
    def objects(self):
        return self.model.query.all(), 200
    
    def get(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        return obj, 200
    
    def create(self, data):
        validation_errors = self.schema.validate(data, session=session)
        if len(validation_errors) is not 0:
            return validation_errors , 400

        obj = self.schema.load(data,session=session)
        if len(obj.errors) is 0 or None:
            session.add(obj.data)
            session.commit()
            
        return obj , 201
    
    def create_all(self, data, use_bulk=None):
        validation_errors = self.schema.validate(data,session=session,many=True)
        if len(validation_errors) is not 0:
            return validation_errors, 400

        collection = self.schema.load(data, session=session, many=True).data
        if use_bulk is True:
            session.bulk_save_objects(collection)
        else:
            session.add_all(collection)
        session.commit()
        return collection, 201

    def update(self, id, data):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))

        validation_errors = self.schema.validate(data, session=session)
        if len(validation_errors) is not 0:
            return validation_errors, 400
        
        obj = self.schema.load(data, session=session, instance=obj, partial=True)
        session.commit()
        return obj.data, 202
    
    def delete(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        session.delete(obj)
        session.commit()
        return {}, 204

sensors_service = GenericModelService(sensors.Sensors,schemas.SensorSchema(),'Sensor')
parameter_service = GenericModelService(domains.Parameters, schemas.ParameterSchema(), 'Parameter')
units_service = GenericModelService(domains.Units, schemas.UnitSchema(), 'Unit')
medium_service = GenericModelService(domains.MediumTypes, schemas.MediumTypeSchema(), 'Medium Type')
quality_check_operand_service = GenericModelService(domains.QualityCheckOperands, schemas.QualityCheckOperandSchema(), 'Quality Check Operand')
quality_check_action_service = GenericModelService(domains.QualityCheckActions, schemas.QualityCheckActionSchema(), 'Quality Check Action')
data_qualifier_service = GenericModelService(domains.DataQualifiers, schemas.DataQualifierSchema(), 'Data Qualifier')
organizations_service = GenericModelService(organizations.Organizations, schemas.OrganizationSchema(), 'Organization')
