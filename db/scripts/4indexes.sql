CREATE INDEX sensors_organization_id_idx
  ON sos.sensors
  USING btree
  (organization_id COLLATE pg_catalog."default");
 
