from flask_restplus import abort
from flask import jsonify
from marshmallow import ValidationError
from . import domains , sensors, organizations, session, schemas


class GenericModelService(object):
    
    
    def __init__(self, model, schema, list_schema, name, post_save_hook=None):
        self.model = model
        self.list_schema = list_schema
        self.schema = schema
        self.name = name
        self.post_save_hook = post_save_hook

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
            if self.post_save_hook is not None:
                self.post_save_hook(obj)
            response = self.schema.dump(obj.data)
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

sensors_service = GenericModelService(sensors.Sensors,schemas.SensorSchema(),schemas.SensorListSchema(many=True),'Sensor')
parameter_service = GenericModelService(domains.Parameters, schemas.ParameterSchema(),schemas.ParameterSchema(many=True), 'Parameter')
units_service = GenericModelService(domains.Units, schemas.UnitSchema(),schemas.UnitSchema(many=True), 'Unit')
medium_service = GenericModelService(domains.MediumTypes, schemas.MediumTypeSchema(),schemas.MediumTypeSchema(many=True), 'Medium Type')
quality_check_operand_service = GenericModelService(domains.QualityCheckOperands, schemas.QualityCheckOperandSchema(),schemas.QualityCheckOperandSchema(many=True), 'Quality Check Operand')
quality_check_action_service = GenericModelService(domains.QualityCheckActions, schemas.QualityCheckActionSchema(), schemas.QualityCheckActionSchema(many=True), 'Quality Check Action')
data_qualifier_service = GenericModelService(domains.DataQualifiers, schemas.DataQualifierSchema(), schemas.DataQualifierSchema(many=True), 'Data Qualifier')
organizations_service = GenericModelService(organizations.Organizations, schemas.OrganizationSchema(), schemas.OrganizationSchema(many=True), 'Organization')
