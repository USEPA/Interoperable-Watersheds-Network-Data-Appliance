INSERT INTO sos.organizations (organization_id, parent_organization_id, name, url, contact_name, contact_email, sos_url)
VALUES('epa', '', 'U.S. EPA', 'www.epa.gov', 'Dwane Young', 'Young.Dwane@epa.gov', '');

INSERT INTO sos.organizations (organization_id, parent_organization_id, name, url, contact_name, contact_email, sos_url)
VALUES('epar10', 'epa', 'U.S. EPA Region 10', 'https://www.epa.gov/aboutepa/epa-region-10-pacific-northwest', 'Anne Dalrymple', 'dalrymple.anne@epa.gov', 'http://ingest_sos:8080/52n-sos-webapp/service');

INSERT INTO sos.sensors (organization_id, org_sensor_id, data_qualifier_id, medium_type_id, short_name, long_name, latitude, longitude, altitude, timezone, ingest_frequency, ingest_status, last_ingest, next_ingest, data_url, data_format, timestamp_column_id, qc_rules_apply, active)
VALUES('epar10', '213204', 1, 1, 'Nooksack@Ferndale', 'Nooksack@Ferndale', 48.838672, -122.592769, 0, '(GMT-08:00) Pacific Time (US & Canada)', 10, 'unknown', null, now(), 'http://cdn.zapstechnologies.com/region10/213204-nooksack_at_ferndale.csv', 1, 2, false, true);

INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79950, 1, 3);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79940, 2, 4);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79960, 3, 5);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79980, 4, 6);

INSERT INTO sos.sensors (organization_id, org_sensor_id, data_qualifier_id, medium_type_id, short_name, long_name, latitude, longitude, altitude, timezone, ingest_frequency, ingest_status, last_ingest, next_ingest, data_url, data_format, timestamp_column_id, qc_rules_apply, active)
VALUES('epar10', '213205', 1, 1, 'Nooksack@Lynden', 'Nooksack@Lynden', 48.936025, -122.4416861, 0, '(GMT-08:00) Pacific Time (US & Canada)', 10, 'unknown', null, now(), 'http://cdn.zapstechnologies.com/region10/213205-nooksack_at_lynden.csv', 1, 2, false, true);

INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79950, 1, 3);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79940, 2, 4);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79960, 3, 5);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79980, 4, 6);

INSERT INTO sos.sensors (organization_id, org_sensor_id, data_qualifier_id, medium_type_id, short_name, long_name, latitude, longitude, altitude, timezone, ingest_frequency, ingest_status, last_ingest, next_ingest, data_url, data_format, timestamp_column_id, qc_rules_apply, active)
VALUES('epar10', '213206', 1, 1, 'Fishtrap@Lynden', 'Fishtrap@Lynden', 48.93538333, -122.4802361, 0, '(GMT-08:00) Pacific Time (US & Canada)', 10, 'unknown', null, now(), 'http://cdn.zapstechnologies.com/region10/213206-fishtrap_at_lynden.csv', 1, 2, false, true);

INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79950, 1, 3);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79940, 2, 4);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79960, 3, 5);
INSERT INTO sos.sensor_parameters(sensor_id, parameter_id, unit_id, parameter_column_id)
VALUES(currval('sensors_sensor_id_seq'), 79980, 4, 6);
