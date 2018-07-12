from . import domains , sensors, organizations, session
from ingest.scheduler import add_to_schedule, remove_from_schedule, update
from utils.exception import ErrorResponse
class Service(object):
    
    
    def __init__(self, model, post_save_hook=None, post_update_hook=None, pre_delete_hook=None):
        self.model = model
        self.post_save_hook = post_save_hook
        self.pre_delete_hook = pre_delete_hook
        self.post_update_hook = post_update_hook


    @property
    def objects(self):
        return self.model.query.all()

    def query(self):
        return session.query(self.model)

    def get(self, id):
        return self.model.query.get(id)


    def create(self,obj):
        session.add(obj.data)
        session.commit()
        if self.post_save_hook is not None:
            self.post_save_hook(obj.data)
        return obj


    def update(self, data=None):
        session.commit()
        if self.post_update_hook is not None and data is not None:
            self.post_update_hook(data)


    def delete(self, obj):
        if self.pre_delete_hook is not None:
            self.pre_delete_hook(obj)
        session.delete(obj)
        session.commit()


sensors_service = Service(sensors.Sensors,add_to_schedule,update,remove_from_schedule)
sensor_parameters_service = Service(sensors.SensorParameters)
parameter_service = Service(domains.Parameters)
units_service = Service(domains.Units)
medium_service = Service(domains.MediumTypes)
quality_check_operand_service = Service(domains.QualityCheckOperands)
quality_check_action_service = Service(domains.QualityCheckActions)
data_qualifier_service = Service(domains.DataQualifiers)
organizations_service = Service(organizations.Organizations)
org_qual_checks_service = Service(organizations.OrganizationParameterQualityChecks)
