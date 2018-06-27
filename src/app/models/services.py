from flask_restplus import abort
from flask import jsonify
from marshmallow import ValidationError
from . import domains , sensors, organizations, session, schemas
from ingest.scheduler import add_to_schedule
from utils.exception import ErrorResponse
class Service(object):
    
    
    def __init__(self,name, model, schema, list_schema=None, post_save_hook=None,post_delete_hook=None):
        self.model = model
        if list_schema is None:
            self.list_schema = schema
        else:
            self.list_schema = list_schema
        self.schema = schema
        self.name = name
        self.post_save_hook = post_save_hook
        self.post_delete_hook = post_delete_hook

    @property
    def objects(self):
        return self.list_schema.jsonify(self.model.query.all(), many=True)

    def _save(self, data, many=False, use_bulk=False):
        if many:
            if use_bulk:
                session.bulk_save_objects(data)
            else:
                session.add_all(data)
        else:
            session.add(data)
        session.commit()
        
    def _build_error_response(self, response, status_code):
        return { 'errors' : response.errors}, status_code

    def get(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))

        return self.schema.jsonify(obj)
    
    def create(self,data):
        obj = self.schema.load(data,session=session)
        if not obj.errors:
            self._save(obj.data)
            response = self.schema.dump(obj.data)
            if self.post_save_hook is not None:
                try:
                    self.post_save_hook(obj.data)
                except:
                    message = 'Error adding {0} Entity to cron'.format(self.name) 
                    raise ErrorResponse(message, 500, response.data)
            
            return response.data, 201
        
        return self._build_error_response(obj, 422)

    def create_all(self,data,use_bulk):
        collection = self.schema.load(data,session=session,many=True)
        if not collection.errors:
            self._save(collection.data, many=True, use_bulk=use_bulk)
            response = self.schema.dump(collection.data)
            return response, 201
        
        return self._build_error_response(collection,422)

    def update(self, id, data):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))

        obj = self.schema.load(data, instance=obj, partial=True)
        if not obj.errors:
            session.commit()
            response = self.schema.dump(obj.data)
            return response.data, 202
        
        return self._build_error_response(obj, 422)
    
    def delete(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        session.delete(obj)
        session.commit()
        return {}, 204

sensors_service = Service('Sensor',sensors.Sensors,schemas.SensorSchema(),schemas.SensorListSchema(many=True), add_to_schedule)
parameter_service = Service('Parameter',domains.Parameters, schemas.ParameterSchema())
units_service = Service('Unit', domains.Units, schemas.UnitSchema())
medium_service = Service('Medium Type',domains.MediumTypes, schemas.MediumTypeSchema())
quality_check_operand_service = Service('Quality Check Operand', domains.QualityCheckOperands, schemas.QualityCheckOperandSchema())
quality_check_action_service = Service('Quality Check Action', domains.QualityCheckActions, schemas.QualityCheckActionSchema())
data_qualifier_service = Service('Data Qualifier', domains.DataQualifiers, schemas.DataQualifierSchema())
organizations_service = Service('Organization', organizations.Organizations, schemas.OrganizationSchema())
