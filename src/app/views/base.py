from flask_restplus import fields

def build_generic_view(model):
    return {
        'errors' : fields.Nested(model, allow_null=False, skip_none=True),
        'data' : fields.Nested(model, allow_null=False)
    }