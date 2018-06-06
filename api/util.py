import records

def execute_query(sql):
    db = records.Database('postgres://sos:sensors@localhost:5432/ingest')
    rows = db.query(sql)
    return rows.as_dict()