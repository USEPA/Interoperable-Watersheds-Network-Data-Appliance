from flask_restplus import abort
from flask import jsonify
from marshmallow import ValidationError
from . import domains , sensors, organizations, session, schemas


class GenericModelService(object):
    
    
    def __init__(self, model, schema, list_schema, name):
        self.model = model
        self.list_schema = list_schema
        self.schema = schema
        self.name = name

    @property
    def objects(self):
        dump = self.list_schema.dump(self.model.query.all())
        return self._build_response(dump,200)

    def _save(self, data, many=False, use_bulk=False):
        if many:
            if use_bulk:
                session.bulk_save_objects(data)
            else:
                session.add_all(data)
        else:
            session.add(data)
        session.commit()
        
    def _build_response(self, response,status_code):
        
        return {
            'data' : response.data,
            'errors' : response.errors
        }, status_code

    def _deserialize(self, data, many=False,partial=True,instance=None):
        return self.schema.load(data,session=session,instance=instance,partial=partial, many=many)

    def get(self, id):

        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))

        response = self.schema.dump(obj)
        return self._build_response(response, 200)
    
    def create(self,data):

        obj = self._deserialize(data)
        if not obj.errors:
            self._save(obj.data)
            return self._build_response(obj,201)
        
        return self._build_response(obj,422)
    
    def create_all(self, data, use_bulk=None):
        obj = self._deserialize(data,many=True,partial=False)

        if not obj.errors:
            self._save(obj.data, many=True)
            return self._build_response(obj,201)
        
        return self._build_response(obj,422)

    def update(self, id, data):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))

        obj = self._deserialize(data, instance=obj, partial=True)
        if not obj.errors:
            session.commit()
            return self._build_response(obj,202)
        
        return self._build_response(obj,422)
    
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
