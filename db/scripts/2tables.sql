CREATE TABLE sos.quality_check_actions
(
  quality_check_action_id serial NOT NULL,
  quality_check_action_name text NOT NULL,
  CONSTRAINT quality_check_actions_pkey PRIMARY KEY (quality_check_action_id),
  CONSTRAINT quality_check_actions_quality_check_action_name_key UNIQUE (quality_check_action_name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.quality_check_actions
  OWNER TO sos;

CREATE TABLE sos.quality_check_operands
(
  quality_check_operand_id serial NOT NULL,
  quality_check_operand_name text NOT NULL,
  CONSTRAINT quality_check_operand_pkey PRIMARY KEY (quality_check_operand_id),
  CONSTRAINT quality_check_operand_quality_check_operand_name_key UNIQUE (quality_check_operand_name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.quality_check_operands
  OWNER TO sos;

CREATE TABLE sos.data_qualifiers
(
  data_qualifier_id serial NOT NULL,
  data_qualifier_name character varying(12) NOT NULL,
  CONSTRAINT data_qualifiers_pkey PRIMARY KEY (data_qualifier_id),
  CONSTRAINT data_qualifiers_data_qualifier_name_key UNIQUE (data_qualifier_name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.data_qualifiers
  OWNER TO sos;

CREATE TABLE sos.units
(
  unit_id serial NOT NULL,
  unit_name text NOT NULL,
  CONSTRAINT units_pkey PRIMARY KEY (unit_id),
  CONSTRAINT units_unit_name_key UNIQUE (unit_name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.units
  OWNER TO sos;

CREATE TABLE sos.medium_types
(
  medium_type_id serial NOT NULL,
  medium_type_name text NOT NULL,
  CONSTRAINT medium_types_pkey PRIMARY KEY (medium_type_id),
  CONSTRAINT medium_types_medium_type_name_key UNIQUE (medium_type_name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.medium_types
  OWNER TO sos;

CREATE TABLE sos.parameters
(
  parameter_id integer NOT NULL,
  parameter_name text NOT NULL,
  CONSTRAINT parameters_pkey PRIMARY KEY (parameter_id),
  CONSTRAINT parameters_parameter_name_key UNIQUE (parameter_name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.parameters
  OWNER TO sos;

CREATE TABLE sos.organizations
(
  organization_id character varying(8) NOT NULL,
  parent_organization_id character varying(8),
  name text NOT NULL,
  url text NOT NULL,
  contact_name text NOT NULL,
  contact_email text NOT NULL,
  sos_url text NOT NULL,
  CONSTRAINT organizations_pkey PRIMARY KEY (organization_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.organizations
  OWNER TO sos;

CREATE TABLE sos.sensors
(
  sensor_id serial NOT NULL,
  organization_id character varying(8) NOT NULL,
  org_sensor_id text NOT NULL,
  data_qualifier_id integer NOT NULL,
  medium_type_id integer NOT NULL,
  short_name text NOT NULL,
  long_name text NOT NULL,
  latitude numeric,
  longitude numeric,
  altitude numeric,
  timezone text,
  ingest_frequency integer NOT NULL,
  ingest_status character varying(8) NOT NULL DEFAULT 'unknown'::character varying,
  last_ingest timestamp without time zone,
  next_ingest timestamp without time zone,  
  data_url text NOT NULL,
  data_format integer,
  timestamp_column_id integer NOT NULL,
  qc_rules_apply boolean,
  active boolean,
  CONSTRAINT sensors_pkey PRIMARY KEY (sensor_id),
  CONSTRAINT sensors_organization_id_fkey FOREIGN KEY (organization_id)
      REFERENCES sos.organizations (organization_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT sensors_qualifier_id_fkey FOREIGN KEY (data_qualifier_id)
      REFERENCES sos.data_qualifiers (data_qualifier_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT sensors_medium_type_id_fkey FOREIGN KEY (medium_type_id)
      REFERENCES sos.medium_types (medium_type_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.sensors
  OWNER TO sos;

CREATE TABLE sos.sensor_parameters
(
  sensor_id integer NOT NULL,
  parameter_id integer NOT NULL,
  unit_id integer NOT NULL,
  parameter_column_id integer NOT NULL,
  CONSTRAINT sensor_parameters_pkey PRIMARY KEY (sensor_id, parameter_id),
  CONSTRAINT sensor_parameters_parameter_id_fkey FOREIGN KEY (parameter_id)
      REFERENCES sos.parameters (parameter_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT sensor_units_unit_id_fkey FOREIGN KEY (unit_id)
      REFERENCES sos.units (unit_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,      
  CONSTRAINT sensor_parameters_sensor_id_fkey FOREIGN KEY (sensor_id)
      REFERENCES sos.sensors (sensor_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.sensor_parameters
  OWNER TO sos;

CREATE TABLE sos.organization_parameter_quality_checks
(
  org_parameter_quality_check_id serial NOT NULL,
  organization_id character varying(8) NOT NULL,
  parameter_id integer NOT NULL,
  quality_check_operand_id integer NOT NULL,
  quality_check_action_id integer NOT NULL,
  threshold double precision NOT NULL,
  CONSTRAINT organization_parameter_quality_checks_pkey PRIMARY KEY (org_parameter_quality_check_id),
  CONSTRAINT organization_parameter_quality_ch_quality_check_operand_id_fkey FOREIGN KEY (quality_check_operand_id)
      REFERENCES sos.quality_check_operands (quality_check_operand_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT organization_parameter_quality_che_quality_check_action_id_fkey FOREIGN KEY (quality_check_action_id)
      REFERENCES sos.quality_check_actions (quality_check_action_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT organization_parameter_quality_checks_organization_id_fkey FOREIGN KEY (organization_id)
      REFERENCES sos.organizations (organization_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT organization_parameter_quality_checks_parameter_id_fkey FOREIGN KEY (parameter_id)
      REFERENCES sos.parameters (parameter_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sos.organization_parameter_quality_checks
  OWNER TO sos;
  
CREATE TABLE sos.ingestions
(
   ingestion_id serial, 
   sensor_id integer, 
   ingestion_start_time timestamp without time zone, 
   ingestion_stop_time timestamp without time zone, 
   status character varying(4), 
   PRIMARY KEY (ingestion_id)
) 
WITH (
  OIDS = FALSE
)
;
ALTER TABLE sos.ingestions
  OWNER TO sos;  

CREATE VIEW sos.all_sensors AS
   select sensor_id, org_sensor_id as stationid, short_name as "shortName", 
      long_name as "longName", longitude::text as easting, latitude::text as northing, 
      coalesce(altitude,0)::text as altitude, o.name as "organizationName", o.url as "organizationURL", 
      o.contact_name || ':' || o.contact_email as contact, 
      medium_type_name as "waterbodyType", o.parent_organization_id as "urn-org", o.organization_id as suborg 
   from sos.sensors s, sos.organizations o, medium_types m
   where s.organization_id = o.organization_id 
   and s.medium_type_id = m.medium_type_id;

ALTER VIEW sos.all_sensors
   OWNER TO sos;

CREATE VIEW sos.all_sensor_parameters AS
   select s.sensor_id, parameter_name, data_qualifier_name, u.unit_name, sp.parameter_column_id
   from sensors s, sensor_parameters sp, parameters p, data_qualifiers d, units u
   where s.sensor_id = sp.sensor_id
   and sp.parameter_id = p.parameter_id
   and s.data_qualifier_id = d.data_qualifier_id
   and u.unit_id = sp.unit_id;

ALTER VIEW sos.all_sensor_parameters 
   OWNER TO sos;

