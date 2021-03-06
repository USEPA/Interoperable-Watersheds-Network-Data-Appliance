INSERT INTO sos.parameters (parameter_id,parameter_name) VALUES 
(79281,'Temperature, Water')
,(79261,'Conductivity')
,(79373,'Specific Conductance')
,(79345,'Salinity')
,(78426,'pH')
,(79933,'Oxidation Reduction Potential (ORP)')
,(79607,'Depth')
,(101627,'Dissolved Oxygen')
,(79586,'Dissolved Oxygen Saturation')
,(79196,'Turbidity')
,(42916,'Chlorophyll')
,(35904,'Inorganic Nitrogen (Nitrate and Nitrite)')
,(79246,'Temperature, air')
,(79912,'Precipitation')
,(79436,'Relative humidity')
,(79645,'Wind velocity')
,(79648,'Wind direction')
,(79443,'Barometric pressure')
,(78485,'Dew point')
,(78471,'Wind gust, peak')
,(79002,'Light, photosynthetic active radiation (PAR)')
,(79771,'Flow')
,(98309,'Height, gage')
,(79287,'Stream Velocity')
,(79749,'Flow, Total')
,(79940,'Nitrate as N')
,(79950,'Escherichia coli')
,(79990,'Reservoir storage')
,(80000,'Lake or reservoir water surface elevation')
,(80010,'Phosphate as P')
,(80020,'Colored dissolved organic matter (CDOM)')
,(79970,'Phycocyanin')
,(80040,'Phosphate as PO4')
,(79960,'Petroleum Hydrocarbons')
,(79980,'Total Suspended Solids')
,(80050,'Discharge')
,(79154,'Biochemical Oxygen Demand');
INSERT INTO sos.quality_check_actions (quality_check_action_name) VALUES ('Discard');
INSERT INTO sos.quality_check_operands (quality_check_operand_name) VALUES ('='),('<'),('<='),('>'),('>=');
INSERT INTO sos.data_qualifiers (data_qualifier_name) VALUES ('Raw'),('Preliminary'),('Final');
INSERT INTO sos.medium_types (medium_type_name) VALUES ('River/Stream');
INSERT INTO sos.units (unit_name) VALUES ('%'),('mg/L'),('MPN/100ML'),('mg-N/L'),('DFU'),('degC'),('None');
