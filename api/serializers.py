from flask_restplus import Model, fields

greeter =  Model('Model',{
    'name' : fields.String,
    'message' : fields.String
})