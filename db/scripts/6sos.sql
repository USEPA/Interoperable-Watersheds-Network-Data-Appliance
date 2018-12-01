\c sos
CREATE TABLE public.blobvalue (
    observationid bigint NOT NULL,
    value oid
);


ALTER TABLE public.blobvalue OWNER TO sos;

--
-- Name: TABLE blobvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.blobvalue IS 'Value table for blob observation';


--
-- Name: COLUMN blobvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.blobvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN blobvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.blobvalue.value IS 'Blob observation value';


--
-- Name: booleanvalue; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.booleanvalue (
    observationid bigint NOT NULL,
    value character(1),
    CONSTRAINT booleanvalue_value_check CHECK ((value = ANY (ARRAY['T'::bpchar, 'F'::bpchar]))),
    CONSTRAINT booleanvalue_value_check1 CHECK ((value = ANY (ARRAY['T'::bpchar, 'F'::bpchar])))
);


ALTER TABLE public.booleanvalue OWNER TO sos;

--
-- Name: TABLE booleanvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.booleanvalue IS 'Value table for boolean observation';


--
-- Name: COLUMN booleanvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.booleanvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN booleanvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.booleanvalue.value IS 'Boolean observation value';


--
-- Name: categoryvalue; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.categoryvalue (
    observationid bigint NOT NULL,
    value character varying(255)
);


ALTER TABLE public.categoryvalue OWNER TO sos;

--
-- Name: TABLE categoryvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.categoryvalue IS 'Value table for category observation';


--
-- Name: COLUMN categoryvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.categoryvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN categoryvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.categoryvalue.value IS 'Category observation value';


--
-- Name: codespace; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.codespace (
    codespaceid bigint NOT NULL,
    codespace character varying(255) NOT NULL
);


ALTER TABLE public.codespace OWNER TO sos;

--
-- Name: TABLE codespace; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.codespace IS 'Table to store the gml:identifier and gml:name codespace information. Mapping file: mapping/core/Codespace.hbm.xml';


--
-- Name: COLUMN codespace.codespaceid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.codespace.codespaceid IS 'Table primary key, used for relations';


--
-- Name: COLUMN codespace.codespace; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.codespace.codespace IS 'The codespace value';


--
-- Name: codespaceid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.codespaceid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.codespaceid_seq OWNER TO sos;

--
-- Name: compositephenomenon; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.compositephenomenon (
    parentobservablepropertyid bigint NOT NULL,
    childobservablepropertyid bigint NOT NULL
);


ALTER TABLE public.compositephenomenon OWNER TO sos;

--
-- Name: TABLE compositephenomenon; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.compositephenomenon IS 'NOT YET USED! Relation table to store observableProperty hierarchies, aka compositePhenomenon. E.g. define a parent in a query and all childs are also contained in the response. Mapping file: mapping/transactional/TObservableProperty.hbm.xml';


--
-- Name: COLUMN compositephenomenon.parentobservablepropertyid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.compositephenomenon.parentobservablepropertyid IS 'Foreign Key (FK) to the related parent observableProperty. Contains "observableProperty".observablePropertyid';


--
-- Name: COLUMN compositephenomenon.childobservablepropertyid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.compositephenomenon.childobservablepropertyid IS 'Foreign Key (FK) to the related child observableProperty. Contains "observableProperty".observablePropertyid';


--
-- Name: countvalue; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.countvalue (
    observationid bigint NOT NULL,
    value integer
);


ALTER TABLE public.countvalue OWNER TO sos;

--
-- Name: TABLE countvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.countvalue IS 'Value table for count observation';


--
-- Name: COLUMN countvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.countvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN countvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.countvalue.value IS 'Count observation value';


--
-- Name: featureofinterest; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.featureofinterest (
    featureofinterestid bigint NOT NULL,
    hibernatediscriminator character(1) NOT NULL,
    featureofinteresttypeid bigint NOT NULL,
    identifier character varying(255),
    codespace bigint,
    name character varying(255),
    codespacename bigint,
    description character varying(255),
    geom public.geometry,
    descriptionxml text,
    url character varying(255)
);


ALTER TABLE public.featureofinterest OWNER TO sos;

--
-- Name: TABLE featureofinterest; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.featureofinterest IS 'Table to store the FeatureOfInterest information. Mapping file: mapping/core/FeatureOfInterest.hbm.xml';


--
-- Name: COLUMN featureofinterest.featureofinterestid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.featureofinterestid IS 'Table primary key, used for relations';


--
-- Name: COLUMN featureofinterest.featureofinteresttypeid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.featureofinteresttypeid IS 'Relation/foreign key to the featureOfInterestType table. Describes the type of the featureOfInterest. Contains "featureOfInterestType".featureOfInterestTypeId';


--
-- Name: COLUMN featureofinterest.identifier; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.identifier IS 'The identifier of the featureOfInterest, gml:identifier. Used as parameter for queries. Optional but unique';


--
-- Name: COLUMN featureofinterest.codespace; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.codespace IS 'Relation/foreign key to the codespace table. Contains the gml:identifier codespace. Optional';


--
-- Name: COLUMN featureofinterest.name; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.name IS 'The name of the featureOfInterest, gml:name. Optional';


--
-- Name: COLUMN featureofinterest.codespacename; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.codespacename IS 'The name of the featureOfInterest, gml:name. Optional';


--
-- Name: COLUMN featureofinterest.description; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.description IS 'Description of the featureOfInterest, gml:description. Optional';


--
-- Name: COLUMN featureofinterest.geom; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.geom IS 'The geometry of the featureOfInterest (composed of the “latitude” and “longitude”) . Optional';


--
-- Name: COLUMN featureofinterest.descriptionxml; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.descriptionxml IS 'XML description of the feature, used when transactional profile is supported . Optional';


--
-- Name: COLUMN featureofinterest.url; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinterest.url IS 'Reference URL to the feature if it is stored in another service, e.g. WFS. Optional but unique';


--
-- Name: featureofinterestid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.featureofinterestid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.featureofinterestid_seq OWNER TO sos;

--
-- Name: featureofinteresttype; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.featureofinteresttype (
    featureofinteresttypeid bigint NOT NULL,
    featureofinteresttype character varying(255) NOT NULL
);


ALTER TABLE public.featureofinteresttype OWNER TO sos;

--
-- Name: TABLE featureofinteresttype; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.featureofinteresttype IS 'Table to store the FeatureOfInterestType information. Mapping file: mapping/core/FeatureOfInterestType.hbm.xml';


--
-- Name: COLUMN featureofinteresttype.featureofinteresttypeid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinteresttype.featureofinteresttypeid IS 'Table primary key, used for relations';


--
-- Name: COLUMN featureofinteresttype.featureofinteresttype; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featureofinteresttype.featureofinteresttype IS 'The featureOfInterestType value, e.g. http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint (OGC OM 2.0 specification) for point features';


--
-- Name: featureofinteresttypeid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.featureofinteresttypeid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.featureofinteresttypeid_seq OWNER TO sos;

--
-- Name: featurerelation; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.featurerelation (
    parentfeatureid bigint NOT NULL,
    childfeatureid bigint NOT NULL
);


ALTER TABLE public.featurerelation OWNER TO sos;

--
-- Name: TABLE featurerelation; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.featurerelation IS 'Relation table to store feature hierarchies. E.g. define a parent in a query and all childs are also contained in the response. Mapping file: mapping/transactional/TFeatureOfInterest.hbm.xml';


--
-- Name: COLUMN featurerelation.parentfeatureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featurerelation.parentfeatureid IS 'Foreign Key (FK) to the related parent featureOfInterest. Contains "featureOfInterest".featureOfInterestid';


--
-- Name: COLUMN featurerelation.childfeatureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.featurerelation.childfeatureid IS 'Foreign Key (FK) to the related child featureOfInterest. Contains "featureOfInterest".featureOfInterestid';


--
-- Name: geometryvalue; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.geometryvalue (
    observationid bigint NOT NULL,
    value public.geometry
);


ALTER TABLE public.geometryvalue OWNER TO sos;

--
-- Name: TABLE geometryvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.geometryvalue IS 'Value table for geometry observation';


--
-- Name: COLUMN geometryvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.geometryvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN geometryvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.geometryvalue.value IS 'Geometry observation value';


--
-- Name: numericvalue; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.numericvalue (
    observationid bigint NOT NULL,
    value double precision
);


ALTER TABLE public.numericvalue OWNER TO sos;

--
-- Name: TABLE numericvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.numericvalue IS 'Value table for numeric/Measurment observation';


--
-- Name: COLUMN numericvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.numericvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN numericvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.numericvalue.value IS 'Numeric/Measurment observation value';


--
-- Name: observableproperty; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.observableproperty (
    observablepropertyid bigint NOT NULL,
    hibernatediscriminator character(1) NOT NULL,
    identifier character varying(255) NOT NULL,
    codespace bigint,
    name character varying(255),
    codespacename bigint,
    description character varying(255),
    disabled character(1) DEFAULT 'F'::bpchar NOT NULL,
    CONSTRAINT observableproperty_disabled_check CHECK ((disabled = ANY (ARRAY['T'::bpchar, 'F'::bpchar])))
);


ALTER TABLE public.observableproperty OWNER TO sos;

--
-- Name: TABLE observableproperty; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.observableproperty IS 'Table to store the ObservedProperty/Phenomenon information. Mapping file: mapping/core/ObservableProperty.hbm.xml';


--
-- Name: COLUMN observableproperty.observablepropertyid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observableproperty.observablepropertyid IS 'Table primary key, used for relations';


--
-- Name: COLUMN observableproperty.identifier; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observableproperty.identifier IS 'The identifier of the observableProperty, gml:identifier. Used as parameter for queries. Unique';


--
-- Name: COLUMN observableproperty.codespace; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observableproperty.codespace IS 'Relation/foreign key to the codespace table. Contains the gml:identifier codespace. Optional';


--
-- Name: COLUMN observableproperty.name; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observableproperty.name IS 'The name of the observableProperty, gml:name. Optional';


--
-- Name: COLUMN observableproperty.codespacename; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observableproperty.codespacename IS 'Relation/foreign key to the codespace table. Contains the gml:name codespace. Optional';


--
-- Name: COLUMN observableproperty.description; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observableproperty.description IS 'Description of the observableProperty, gml:description. Optional';


--
-- Name: COLUMN observableproperty.disabled; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observableproperty.disabled IS 'For later use by the SOS. Indicator if this observableProperty should not be provided by the SOS.';


--
-- Name: observablepropertyid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.observablepropertyid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.observablepropertyid_seq OWNER TO sos;

--
-- Name: observation; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.observation (
    observationid bigint NOT NULL,
    seriesid bigint NOT NULL,
    phenomenontimestart timestamp without time zone NOT NULL,
    phenomenontimeend timestamp without time zone NOT NULL,
    resulttime timestamp without time zone NOT NULL,
    identifier character varying(255),
    codespace bigint,
    name character varying(255),
    codespacename bigint,
    description character varying(255),
    deleted character(1) DEFAULT 'F'::bpchar NOT NULL,
    validtimestart timestamp without time zone,
    validtimeend timestamp without time zone,
    unitid bigint,
    samplinggeometry public.geometry,
    CONSTRAINT observation_deleted_check CHECK ((deleted = ANY (ARRAY['T'::bpchar, 'F'::bpchar])))
);


ALTER TABLE public.observation OWNER TO sos;

--
-- Name: TABLE observation; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.observation IS 'Stores the observations. Mapping file: mapping/series/observation/SeriesObservation.hbm.xml';


--
-- Name: COLUMN observation.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.observationid IS 'Table primary key, used in relations';


--
-- Name: COLUMN observation.seriesid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.seriesid IS 'Relation/foreign key to the associated series table. Contains "series".seriesId';


--
-- Name: COLUMN observation.phenomenontimestart; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.phenomenontimestart IS 'Time stamp when the observation was started or phenomenon was observed';


--
-- Name: COLUMN observation.phenomenontimeend; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.phenomenontimeend IS 'Time stamp when the observation was stopped or phenomenon was observed';


--
-- Name: COLUMN observation.resulttime; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.resulttime IS 'Time stamp when the observation was published or result was published/available';


--
-- Name: COLUMN observation.identifier; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.identifier IS 'The identifier of the observation, gml:identifier. Used as parameter for queries. Optional but unique';


--
-- Name: COLUMN observation.codespace; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.codespace IS 'Relation/foreign key to the codespace table. Contains the gml:identifier codespace. Optional';


--
-- Name: COLUMN observation.name; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.name IS 'The name of the observation, gml:name. Optional';


--
-- Name: COLUMN observation.codespacename; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.codespacename IS 'The name of the observation, gml:name. Optional';


--
-- Name: COLUMN observation.description; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.description IS 'Description of the observation, gml:description. Optional';


--
-- Name: COLUMN observation.deleted; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.deleted IS 'Flag to indicate that this observation is deleted or not (OGC SWES 2.0 - DeleteSensor operation or not specified DeleteObservation)';


--
-- Name: COLUMN observation.validtimestart; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.validtimestart IS 'Start time stamp for which the observation/result is valid, e.g. used for forecasting. Optional';


--
-- Name: COLUMN observation.validtimeend; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.validtimeend IS 'End time stamp for which the observation/result is valid, e.g. used for forecasting. Optional';


--
-- Name: COLUMN observation.unitid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.unitid IS 'Foreign Key (FK) to the related unit of measure. Contains "unit".unitid. Optional';


--
-- Name: COLUMN observation.samplinggeometry; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observation.samplinggeometry IS 'Sampling geometry describes exactly where the measurement has taken place. Used for OGC SOS 2.0 Spatial Filtering Profile. Optional';


--
-- Name: observationconstellation; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.observationconstellation (
    observationconstellationid bigint NOT NULL,
    observablepropertyid bigint NOT NULL,
    procedureid bigint NOT NULL,
    observationtypeid bigint,
    offeringid bigint NOT NULL,
    deleted character(1) DEFAULT 'F'::bpchar NOT NULL,
    hiddenchild character(1) DEFAULT 'F'::bpchar NOT NULL,
    CONSTRAINT observationconstellation_deleted_check CHECK ((deleted = ANY (ARRAY['T'::bpchar, 'F'::bpchar]))),
    CONSTRAINT observationconstellation_hiddenchild_check CHECK ((hiddenchild = ANY (ARRAY['T'::bpchar, 'F'::bpchar])))
);


ALTER TABLE public.observationconstellation OWNER TO sos;

--
-- Name: TABLE observationconstellation; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.observationconstellation IS 'Table to store the ObservationConstellation information. Contains information about the constellation of observableProperty, procedure, offering and the observationType. Mapping file: mapping/core/ObservationConstellation.hbm.xml';


--
-- Name: COLUMN observationconstellation.observationconstellationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationconstellation.observationconstellationid IS 'Table primary key, used for relations';


--
-- Name: COLUMN observationconstellation.observablepropertyid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationconstellation.observablepropertyid IS 'Foreign Key (FK) to the related observableProperty. Contains "observableproperty".observablepropertyid';


--
-- Name: COLUMN observationconstellation.procedureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationconstellation.procedureid IS 'Foreign Key (FK) to the related procedure. Contains "procedure".procedureid';


--
-- Name: COLUMN observationconstellation.observationtypeid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationconstellation.observationtypeid IS 'Foreign Key (FK) to the related observableProperty. Contains "observationtype".observationtypeid';


--
-- Name: COLUMN observationconstellation.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationconstellation.offeringid IS 'Foreign Key (FK) to the related observableProperty. Contains "offering".offeringid';


--
-- Name: COLUMN observationconstellation.deleted; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationconstellation.deleted IS 'Flag to indicate that this observationConstellation is deleted or not. Set if the related procedure is deleted via DeleteSensor operation (OGC SWES 2.0 - DeleteSensor operation)';


--
-- Name: COLUMN observationconstellation.hiddenchild; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationconstellation.hiddenchild IS 'Flag to indicate that this observationConstellations procedure is a child procedure of another procedure. If true, the related procedure is not contained in OGC SOS 2.0 Capabilities but in OGC SOS 1.0.0 Capabilities.';


--
-- Name: observationconstellationid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.observationconstellationid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.observationconstellationid_seq OWNER TO sos;

--
-- Name: observationhasoffering; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.observationhasoffering (
    observationid bigint NOT NULL,
    offeringid bigint NOT NULL
);


ALTER TABLE public.observationhasoffering OWNER TO sos;

--
-- Name: TABLE observationhasoffering; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.observationhasoffering IS 'Table to store relations between observation and associated offerings. Mapping file: mapping/ereporting/EReportingObservation.hbm.xml';


--
-- Name: COLUMN observationhasoffering.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationhasoffering.observationid IS 'Foreign Key (FK) to the related observation. Contains "observation".oobservationid';


--
-- Name: COLUMN observationhasoffering.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationhasoffering.offeringid IS 'Foreign Key (FK) to the related offering. Contains "offering".offeringid';


--
-- Name: observationid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.observationid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.observationid_seq OWNER TO sos;

--
-- Name: observationtype; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.observationtype (
    observationtypeid bigint NOT NULL,
    observationtype character varying(255) NOT NULL
);


ALTER TABLE public.observationtype OWNER TO sos;

--
-- Name: TABLE observationtype; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.observationtype IS 'Table to store the observationTypes. Mapping file: mapping/core/ObservationType.hbm.xml';


--
-- Name: COLUMN observationtype.observationtypeid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationtype.observationtypeid IS 'Table primary key, used for relations';


--
-- Name: COLUMN observationtype.observationtype; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.observationtype.observationtype IS 'The observationType value, e.g. http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement (OGC OM 2.0 specification) for OM_Measurement';


--
-- Name: observationtypeid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.observationtypeid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.observationtypeid_seq OWNER TO sos;

--
-- Name: offering; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.offering (
    offeringid bigint NOT NULL,
    hibernatediscriminator character(1) NOT NULL,
    identifier character varying(255) NOT NULL,
    codespace bigint,
    name character varying(255),
    codespacename bigint,
    description character varying(255),
    disabled character(1) DEFAULT 'F'::bpchar NOT NULL,
    CONSTRAINT offering_disabled_check CHECK ((disabled = ANY (ARRAY['T'::bpchar, 'F'::bpchar])))
);


ALTER TABLE public.offering OWNER TO sos;

--
-- Name: TABLE offering; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.offering IS 'Table to store the offering information. Mapping file: mapping/core/Offering.hbm.xml';


--
-- Name: COLUMN offering.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offering.offeringid IS 'Table primary key, used for relations';


--
-- Name: COLUMN offering.identifier; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offering.identifier IS 'The identifier of the offering, gml:identifier. Used as parameter for queries. Unique';


--
-- Name: COLUMN offering.codespace; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offering.codespace IS 'Relation/foreign key to the codespace table. Contains the gml:identifier codespace. Optional';


--
-- Name: COLUMN offering.name; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offering.name IS 'The name of the offering, gml:name. If available, displyed in the contents of the Capabilites. Optional';


--
-- Name: COLUMN offering.codespacename; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offering.codespacename IS 'Relation/foreign key to the codespace table. Contains the gml:name codespace. Optional';


--
-- Name: COLUMN offering.description; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offering.description IS 'Description of the offering, gml:description. Optional';


--
-- Name: COLUMN offering.disabled; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offering.disabled IS 'For later use by the SOS. Indicator if this offering should not be provided by the SOS.';


--
-- Name: offeringallowedfeaturetype; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.offeringallowedfeaturetype (
    offeringid bigint NOT NULL,
    featureofinteresttypeid bigint NOT NULL
);


ALTER TABLE public.offeringallowedfeaturetype OWNER TO sos;

--
-- Name: TABLE offeringallowedfeaturetype; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.offeringallowedfeaturetype IS 'Table to store relations between offering and allowed featureOfInterestTypes, defined in InsertSensor request. Mapping file: mapping/transactional/TOffering.hbm.xml';


--
-- Name: COLUMN offeringallowedfeaturetype.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offeringallowedfeaturetype.offeringid IS 'Foreign Key (FK) to the related offering. Contains "offering".offeringid';


--
-- Name: COLUMN offeringallowedfeaturetype.featureofinteresttypeid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offeringallowedfeaturetype.featureofinteresttypeid IS 'Foreign Key (FK) to the related featureOfInterestTypeId. Contains "featureOfInterestType".featureOfInterestTypeId';


--
-- Name: offeringallowedobservationtype; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.offeringallowedobservationtype (
    offeringid bigint NOT NULL,
    observationtypeid bigint NOT NULL
);


ALTER TABLE public.offeringallowedobservationtype OWNER TO sos;

--
-- Name: TABLE offeringallowedobservationtype; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.offeringallowedobservationtype IS 'Table to store relations between offering and allowed observationTypes, defined in InsertSensor request. Mapping file: mapping/transactional/TOffering.hbm.xml';


--
-- Name: COLUMN offeringallowedobservationtype.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offeringallowedobservationtype.offeringid IS 'Foreign Key (FK) to the related offering. Contains "offering".offeringid';


--
-- Name: COLUMN offeringallowedobservationtype.observationtypeid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offeringallowedobservationtype.observationtypeid IS 'Foreign Key (FK) to the related observationType. Contains "observationType".observationTypeId';


--
-- Name: offeringhasrelatedfeature; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.offeringhasrelatedfeature (
    relatedfeatureid bigint NOT NULL,
    offeringid bigint NOT NULL
);


ALTER TABLE public.offeringhasrelatedfeature OWNER TO sos;

--
-- Name: TABLE offeringhasrelatedfeature; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.offeringhasrelatedfeature IS 'Table to store relations between offering and associated relatedFeatures. Mapping file: mapping/transactional/TOffering.hbm.xml';


--
-- Name: COLUMN offeringhasrelatedfeature.relatedfeatureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offeringhasrelatedfeature.relatedfeatureid IS 'Foreign Key (FK) to the related relatedFeature. Contains "relatedFeature".relatedFeatureid';


--
-- Name: COLUMN offeringhasrelatedfeature.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.offeringhasrelatedfeature.offeringid IS 'Foreign Key (FK) to the related offering. Contains "offering".offeringid';


--
-- Name: offeringid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.offeringid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.offeringid_seq OWNER TO sos;

--
-- Name: parameter; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.parameter (
    parameterid bigint NOT NULL,
    observationid bigint NOT NULL,
    definition character varying(255) NOT NULL,
    title character varying(255),
    value oid NOT NULL
);


ALTER TABLE public.parameter OWNER TO sos;

--
-- Name: TABLE parameter; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.parameter IS 'NOT YET USED! Table to store additional obervation information (om:parameter). Mapping file: mapping/transactional/Parameter.hbm.xml';


--
-- Name: COLUMN parameter.parameterid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.parameter.parameterid IS 'Table primary key';


--
-- Name: COLUMN parameter.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.parameter.observationid IS 'Foreign Key (FK) to the related observation. Contains "observation".observationid';


--
-- Name: COLUMN parameter.definition; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.parameter.definition IS 'Definition of the additional information';


--
-- Name: COLUMN parameter.title; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.parameter.title IS 'optional title of the additional information. Optional';


--
-- Name: COLUMN parameter.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.parameter.value IS 'Value of the additional information';


--
-- Name: parameterid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.parameterid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parameterid_seq OWNER TO sos;

--
-- Name: procdescformatid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.procdescformatid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.procdescformatid_seq OWNER TO sos;

--
-- Name: procedure; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.procedure (
    procedureid bigint NOT NULL,
    hibernatediscriminator character(1) NOT NULL,
    proceduredescriptionformatid bigint NOT NULL,
    identifier character varying(255) NOT NULL,
    codespace bigint,
    name character varying(255),
    codespacename bigint,
    description character varying(255),
    deleted character(1) DEFAULT 'F'::bpchar NOT NULL,
    disabled character(1) DEFAULT 'F'::bpchar NOT NULL,
    descriptionfile text,
    referenceflag character(1) DEFAULT 'F'::bpchar,
    CONSTRAINT procedure_deleted_check CHECK ((deleted = ANY (ARRAY['T'::bpchar, 'F'::bpchar]))),
    CONSTRAINT procedure_disabled_check CHECK ((disabled = ANY (ARRAY['T'::bpchar, 'F'::bpchar]))),
    CONSTRAINT procedure_referenceflag_check CHECK ((referenceflag = ANY (ARRAY['T'::bpchar, 'F'::bpchar])))
);


ALTER TABLE public.procedure OWNER TO sos;

--
-- Name: TABLE procedure; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.procedure IS 'Table to store the procedure/sensor. Mapping file: mapping/core/Procedure.hbm.xml';


--
-- Name: COLUMN procedure.procedureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.procedureid IS 'Table primary key, used for relations';


--
-- Name: COLUMN procedure.proceduredescriptionformatid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.proceduredescriptionformatid IS 'Relation/foreign key to the procedureDescriptionFormat table. Describes the format of the procedure description.';


--
-- Name: COLUMN procedure.identifier; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.identifier IS 'The identifier of the procedure, gml:identifier. Used as parameter for queries. Unique';


--
-- Name: COLUMN procedure.codespace; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.codespace IS 'Relation/foreign key to the codespace table. Contains the gml:identifier codespace. Optional';


--
-- Name: COLUMN procedure.name; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.name IS 'The name of the procedure, gml:name. Optional';


--
-- Name: COLUMN procedure.codespacename; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.codespacename IS 'Relation/foreign key to the codespace table. Contains the gml:name codespace. Optional';


--
-- Name: COLUMN procedure.description; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.description IS 'Description of the procedure, gml:description. Optional';


--
-- Name: COLUMN procedure.deleted; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.deleted IS 'Flag to indicate that this procedure is deleted or not (OGC SWES 2.0 - DeleteSensor operation)';


--
-- Name: COLUMN procedure.disabled; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.disabled IS 'For later use by the SOS. Indicator if this procedure should not be provided by the SOS.';


--
-- Name: COLUMN procedure.descriptionfile; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.descriptionfile IS 'Field for full (XML) encoded procedure description or link to a procedure description file. Optional';


--
-- Name: COLUMN procedure.referenceflag; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.procedure.referenceflag IS 'Flag to indicate that this procedure is a reference procedure of another procedure. Not used by the SOS but by the Sensor Web REST-API';


--
-- Name: proceduredescriptionformat; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.proceduredescriptionformat (
    proceduredescriptionformatid bigint NOT NULL,
    proceduredescriptionformat character varying(255) NOT NULL
);


ALTER TABLE public.proceduredescriptionformat OWNER TO sos;

--
-- Name: TABLE proceduredescriptionformat; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.proceduredescriptionformat IS 'Table to store the ProcedureDescriptionFormat information of procedures. Mapping file: mapping/core/ProcedureDescriptionFormat.hbm.xml';


--
-- Name: COLUMN proceduredescriptionformat.proceduredescriptionformatid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.proceduredescriptionformat.proceduredescriptionformatid IS 'Table primary key, used for relations';


--
-- Name: COLUMN proceduredescriptionformat.proceduredescriptionformat; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.proceduredescriptionformat.proceduredescriptionformat IS 'The procedureDescriptionFormat value, e.g. http://www.opengis.net/sensorML/1.0.1 for procedures descriptions as specified in OGC SensorML 1.0.1';


--
-- Name: procedureid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.procedureid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.procedureid_seq OWNER TO sos;

--
-- Name: relatedfeature; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.relatedfeature (
    relatedfeatureid bigint NOT NULL,
    featureofinterestid bigint NOT NULL
);


ALTER TABLE public.relatedfeature OWNER TO sos;

--
-- Name: TABLE relatedfeature; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.relatedfeature IS 'Table to store related feature information used in the OGC SOS 2.0 Capabilities (See also OGC SWES 2.0). Mapping file: mapping/transactionl/RelatedFeature.hbm.xml';


--
-- Name: COLUMN relatedfeature.relatedfeatureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.relatedfeature.relatedfeatureid IS 'Table primary key, used for relations';


--
-- Name: COLUMN relatedfeature.featureofinterestid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.relatedfeature.featureofinterestid IS 'Foreign Key (FK) to the related featureOfInterest. Contains "featureOfInterest".featureOfInterestid';


--
-- Name: relatedfeaturehasrole; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.relatedfeaturehasrole (
    relatedfeatureid bigint NOT NULL,
    relatedfeatureroleid bigint NOT NULL
);


ALTER TABLE public.relatedfeaturehasrole OWNER TO sos;

--
-- Name: TABLE relatedfeaturehasrole; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.relatedfeaturehasrole IS 'Relation table to store relatedFeatures and their associated relatedFeatureRoles. Mapping file: mapping/transactionl/RelatedFeature.hbm.xml';


--
-- Name: COLUMN relatedfeaturehasrole.relatedfeatureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.relatedfeaturehasrole.relatedfeatureid IS 'Foreign Key (FK) to the related relatedFeature. Contains "relatedFeature".relatedFeatureid';


--
-- Name: COLUMN relatedfeaturehasrole.relatedfeatureroleid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.relatedfeaturehasrole.relatedfeatureroleid IS 'Foreign Key (FK) to the related relatedFeatureRole. Contains "relatedFeatureRole".relatedFeatureRoleid';


--
-- Name: relatedfeatureid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.relatedfeatureid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relatedfeatureid_seq OWNER TO sos;

--
-- Name: relatedfeaturerole; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.relatedfeaturerole (
    relatedfeatureroleid bigint NOT NULL,
    relatedfeaturerole character varying(255) NOT NULL
);


ALTER TABLE public.relatedfeaturerole OWNER TO sos;

--
-- Name: TABLE relatedfeaturerole; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.relatedfeaturerole IS 'Table to store related feature role information used in the OGC SOS 2.0 Capabilities (See also OGC SWES 2.0). Mapping file: mapping/transactionl/RelatedFeatureRole.hbm.xml';


--
-- Name: COLUMN relatedfeaturerole.relatedfeatureroleid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.relatedfeaturerole.relatedfeatureroleid IS 'Table primary key, used for relations';


--
-- Name: COLUMN relatedfeaturerole.relatedfeaturerole; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.relatedfeaturerole.relatedfeaturerole IS 'The related feature role definition. See OGC SWES 2.0 specification';


--
-- Name: relatedfeatureroleid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.relatedfeatureroleid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relatedfeatureroleid_seq OWNER TO sos;

--
-- Name: resulttemplate; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.resulttemplate (
    resulttemplateid bigint NOT NULL,
    offeringid bigint NOT NULL,
    observablepropertyid bigint NOT NULL,
    procedureid bigint NOT NULL,
    featureofinterestid bigint NOT NULL,
    identifier character varying(255) NOT NULL,
    resultstructure text NOT NULL,
    resultencoding text NOT NULL
);


ALTER TABLE public.resulttemplate OWNER TO sos;

--
-- Name: TABLE resulttemplate; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.resulttemplate IS 'Table to store resultTemplates (OGC SOS 2.0 result handling profile). Mapping file: mapping/transactionl/ResultTemplate.hbm.xml';


--
-- Name: COLUMN resulttemplate.resulttemplateid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.resulttemplateid IS 'Table primary key';


--
-- Name: COLUMN resulttemplate.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.offeringid IS 'Foreign Key (FK) to the related offering. Contains "offering".offeringid';


--
-- Name: COLUMN resulttemplate.observablepropertyid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.observablepropertyid IS 'Foreign Key (FK) to the related observableProperty. Contains "observableProperty".observablePropertyId';


--
-- Name: COLUMN resulttemplate.procedureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.procedureid IS 'Foreign Key (FK) to the related procedure. Contains "procedure".procedureId';


--
-- Name: COLUMN resulttemplate.featureofinterestid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.featureofinterestid IS 'Foreign Key (FK) to the related featureOfInterest. Contains "featureOfInterest".featureOfInterestid';


--
-- Name: COLUMN resulttemplate.identifier; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.identifier IS 'The resultTemplate identifier, required for InsertResult requests.';


--
-- Name: COLUMN resulttemplate.resultstructure; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.resultstructure IS 'The resultStructure as XML string. Describes the types and order of the values in a GetResultResponse/InsertResultRequest';


--
-- Name: COLUMN resulttemplate.resultencoding; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.resulttemplate.resultencoding IS 'The resultEncoding as XML string. Describes the encoding of the values in a GetResultResponse/InsertResultRequest';


--
-- Name: resulttemplateid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.resulttemplateid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resulttemplateid_seq OWNER TO sos;

--
-- Name: sensorsystem; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.sensorsystem (
    parentsensorid bigint NOT NULL,
    childsensorid bigint NOT NULL
);


ALTER TABLE public.sensorsystem OWNER TO sos;

--
-- Name: TABLE sensorsystem; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.sensorsystem IS 'Relation table to store procedure hierarchies. E.g. define a parent in a query and all childs are also contained in the response. Mapping file: mapping/transactional/TProcedure.hbm.xml';


--
-- Name: COLUMN sensorsystem.parentsensorid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.sensorsystem.parentsensorid IS 'Foreign Key (FK) to the related parent procedure. Contains "procedure".procedureid';


--
-- Name: COLUMN sensorsystem.childsensorid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.sensorsystem.childsensorid IS 'Foreign Key (FK) to the related child procedure. Contains "procedure".procedureid';


--
-- Name: series; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.series (
    seriesid bigint NOT NULL,
    featureofinterestid bigint NOT NULL,
    observablepropertyid bigint NOT NULL,
    procedureid bigint NOT NULL,
    offeringid bigint,
    deleted character(1) DEFAULT 'F'::bpchar NOT NULL,
    published character(1) DEFAULT 'T'::bpchar NOT NULL,
    firsttimestamp timestamp without time zone,
    lasttimestamp timestamp without time zone,
    firstnumericvalue double precision,
    lastnumericvalue double precision,
    unitid bigint,
    CONSTRAINT series_deleted_check CHECK ((deleted = ANY (ARRAY['T'::bpchar, 'F'::bpchar]))),
    CONSTRAINT series_published_check CHECK ((published = ANY (ARRAY['T'::bpchar, 'F'::bpchar])))
);


ALTER TABLE public.series OWNER TO sos;

--
-- Name: TABLE series; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.series IS 'Table to store a (time-) series which consists of featureOfInterest, observableProperty, and procedure. Mapping file: mapping/series/Series.hbm.xml';


--
-- Name: COLUMN series.seriesid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.seriesid IS 'Table primary key, used for relations';


--
-- Name: COLUMN series.featureofinterestid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.featureofinterestid IS 'Foreign Key (FK) to the related featureOfInterest. Contains "featureOfInterest".featureOfInterestId';


--
-- Name: COLUMN series.observablepropertyid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.observablepropertyid IS 'Foreign Key (FK) to the related observableProperty. Contains "observableproperty".observablepropertyid';


--
-- Name: COLUMN series.procedureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.procedureid IS 'Foreign Key (FK) to the related procedure. Contains "procedure".procedureid';


--
-- Name: COLUMN series.offeringid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.offeringid IS 'Foreign Key (FK) to the related procedure. Contains "offering".offeringid';


--
-- Name: COLUMN series.deleted; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.deleted IS 'Flag to indicate that this series is deleted or not. Set if the related procedure is deleted via DeleteSensor operation (OGC SWES 2.0 - DeleteSensor operation)';


--
-- Name: COLUMN series.published; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.published IS 'Flag to indicate that this series is published or not. A not published series is not contained in GetObservation and GetDataAvailability responses';


--
-- Name: COLUMN series.firsttimestamp; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.firsttimestamp IS 'The time stamp of the first (temporal) observation associated to this series';


--
-- Name: COLUMN series.lasttimestamp; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.lasttimestamp IS 'The time stamp of the last (temporal) observation associated to this series';


--
-- Name: COLUMN series.firstnumericvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.firstnumericvalue IS 'The value of the first (temporal) observation associated to this series';


--
-- Name: COLUMN series.lastnumericvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.lastnumericvalue IS 'The value of the last (temporal) observation associated to this series';


--
-- Name: COLUMN series.unitid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.series.unitid IS 'Foreign Key (FK) to the related unit of the first/last numeric values . Contains "unit".unitid';


--
-- Name: seriesid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.seriesid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seriesid_seq OWNER TO sos;

--
-- Name: swedataarrayvalue; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.swedataarrayvalue (
    observationid bigint NOT NULL,
    value text
);


ALTER TABLE public.swedataarrayvalue OWNER TO sos;

--
-- Name: TABLE swedataarrayvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.swedataarrayvalue IS 'Value table for SweDataArray observation';


--
-- Name: COLUMN swedataarrayvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.swedataarrayvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN swedataarrayvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.swedataarrayvalue.value IS 'SweDataArray observation value';


--
-- Name: textvalue; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.textvalue (
    observationid bigint NOT NULL,
    value text
);


ALTER TABLE public.textvalue OWNER TO sos;

--
-- Name: TABLE textvalue; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.textvalue IS 'Value table for text observation';


--
-- Name: COLUMN textvalue.observationid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.textvalue.observationid IS 'Foreign Key (FK) to the related observation from the observation table. Contains "observation".observationid';


--
-- Name: COLUMN textvalue.value; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.textvalue.value IS 'Text observation value';


--
-- Name: unit; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.unit (
    unitid bigint NOT NULL,
    unit character varying(255) NOT NULL
);


ALTER TABLE public.unit OWNER TO sos;

--
-- Name: TABLE unit; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.unit IS 'Table to store the unit of measure information, used in observations. Mapping file: mapping/core/Unit.hbm.xml';


--
-- Name: COLUMN unit.unitid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.unit.unitid IS 'Table primary key, used for relations';


--
-- Name: COLUMN unit.unit; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.unit.unit IS 'The unit of measure of observations. See http://unitsofmeasure.org/ucum.html';


--
-- Name: unitid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.unitid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.unitid_seq OWNER TO sos;

--
-- Name: validproceduretime; Type: TABLE; Schema: public; Owner: sos
--

CREATE TABLE public.validproceduretime (
    validproceduretimeid bigint NOT NULL,
    procedureid bigint NOT NULL,
    proceduredescriptionformatid bigint NOT NULL,
    starttime timestamp without time zone NOT NULL,
    endtime timestamp without time zone,
    descriptionxml text NOT NULL
);


ALTER TABLE public.validproceduretime OWNER TO sos;

--
-- Name: TABLE validproceduretime; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON TABLE public.validproceduretime IS 'Table to store procedure descriptions which were inserted or updated via the transactional Profile. Mapping file: mapping/transactionl/ValidProcedureTime.hbm.xml';


--
-- Name: COLUMN validproceduretime.validproceduretimeid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.validproceduretime.validproceduretimeid IS 'Table primary key';


--
-- Name: COLUMN validproceduretime.procedureid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.validproceduretime.procedureid IS 'Foreign Key (FK) to the related procedure. Contains "procedure".procedureid';


--
-- Name: COLUMN validproceduretime.proceduredescriptionformatid; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.validproceduretime.proceduredescriptionformatid IS 'Foreign Key (FK) to the related procedureDescriptionFormat. Contains "procedureDescriptionFormat".procedureDescriptionFormatid';


--
-- Name: COLUMN validproceduretime.starttime; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.validproceduretime.starttime IS 'Timestamp since this procedure description is valid';


--
-- Name: COLUMN validproceduretime.endtime; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.validproceduretime.endtime IS 'Timestamp since this procedure description is invalid';


--
-- Name: COLUMN validproceduretime.descriptionxml; Type: COMMENT; Schema: public; Owner: sos
--

COMMENT ON COLUMN public.validproceduretime.descriptionxml IS 'Procedure description as XML string';


--
-- Name: validproceduretimeid_seq; Type: SEQUENCE; Schema: public; Owner: sos
--

CREATE SEQUENCE public.validproceduretimeid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.validproceduretimeid_seq OWNER TO sos;

--
-- Data for Name: blobvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.blobvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: booleanvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.booleanvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: categoryvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.categoryvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: codespace; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.codespace (codespaceid, codespace) FROM stdin;
\.


--
-- Data for Name: compositephenomenon; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.compositephenomenon (parentobservablepropertyid, childobservablepropertyid) FROM stdin;
\.


--
-- Data for Name: countvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.countvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: featureofinterest; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.featureofinterest (featureofinterestid, hibernatediscriminator, featureofinteresttypeid, identifier, codespace, name, codespacename, description, geom, descriptionxml, url) FROM stdin;
\.


--
-- Data for Name: featureofinteresttype; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.featureofinteresttype (featureofinteresttypeid, featureofinteresttype) FROM stdin;
\.


--
-- Data for Name: featurerelation; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.featurerelation (parentfeatureid, childfeatureid) FROM stdin;
\.


--
-- Data for Name: geometryvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.geometryvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: numericvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.numericvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: observableproperty; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.observableproperty (observablepropertyid, hibernatediscriminator, identifier, codespace, name, codespacename, description, disabled) FROM stdin;
\.


--
-- Data for Name: observation; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.observation (observationid, seriesid, phenomenontimestart, phenomenontimeend, resulttime, identifier, codespace, name, codespacename, description, deleted, validtimestart, validtimeend, unitid, samplinggeometry) FROM stdin;
\.


--
-- Data for Name: observationconstellation; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.observationconstellation (observationconstellationid, observablepropertyid, procedureid, observationtypeid, offeringid, deleted, hiddenchild) FROM stdin;
\.


--
-- Data for Name: observationhasoffering; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.observationhasoffering (observationid, offeringid) FROM stdin;
\.


--
-- Data for Name: observationtype; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.observationtype (observationtypeid, observationtype) FROM stdin;
\.


--
-- Data for Name: offering; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.offering (offeringid, hibernatediscriminator, identifier, codespace, name, codespacename, description, disabled) FROM stdin;
\.


--
-- Data for Name: offeringallowedfeaturetype; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.offeringallowedfeaturetype (offeringid, featureofinteresttypeid) FROM stdin;
\.


--
-- Data for Name: offeringallowedobservationtype; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.offeringallowedobservationtype (offeringid, observationtypeid) FROM stdin;
\.


--
-- Data for Name: offeringhasrelatedfeature; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.offeringhasrelatedfeature (relatedfeatureid, offeringid) FROM stdin;
\.


--
-- Data for Name: parameter; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.parameter (parameterid, observationid, definition, title, value) FROM stdin;
\.


--
-- Data for Name: procedure; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.procedure (procedureid, hibernatediscriminator, proceduredescriptionformatid, identifier, codespace, name, codespacename, description, deleted, disabled, descriptionfile, referenceflag) FROM stdin;
\.


--
-- Data for Name: proceduredescriptionformat; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.proceduredescriptionformat (proceduredescriptionformatid, proceduredescriptionformat) FROM stdin;
\.


--
-- Data for Name: relatedfeature; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.relatedfeature (relatedfeatureid, featureofinterestid) FROM stdin;
\.


--
-- Data for Name: relatedfeaturehasrole; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.relatedfeaturehasrole (relatedfeatureid, relatedfeatureroleid) FROM stdin;
\.


--
-- Data for Name: relatedfeaturerole; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.relatedfeaturerole (relatedfeatureroleid, relatedfeaturerole) FROM stdin;
\.


--
-- Data for Name: resulttemplate; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.resulttemplate (resulttemplateid, offeringid, observablepropertyid, procedureid, featureofinterestid, identifier, resultstructure, resultencoding) FROM stdin;
\.


--
-- Data for Name: sensorsystem; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.sensorsystem (parentsensorid, childsensorid) FROM stdin;
\.


--
-- Data for Name: series; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.series (seriesid, featureofinterestid, observablepropertyid, procedureid, offeringid, deleted, published, firsttimestamp, lasttimestamp, firstnumericvalue, lastnumericvalue, unitid) FROM stdin;
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: swedataarrayvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.swedataarrayvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: textvalue; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.textvalue (observationid, value) FROM stdin;
\.


--
-- Data for Name: unit; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.unit (unitid, unit) FROM stdin;
\.


--
-- Data for Name: validproceduretime; Type: TABLE DATA; Schema: public; Owner: sos
--

COPY public.validproceduretime (validproceduretimeid, procedureid, proceduredescriptionformatid, starttime, endtime, descriptionxml) FROM stdin;
\.


--
-- Name: codespaceid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.codespaceid_seq', 1, false);


--
-- Name: featureofinterestid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.featureofinterestid_seq', 1, false);


--
-- Name: featureofinteresttypeid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.featureofinteresttypeid_seq', 1, false);


--
-- Name: observablepropertyid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.observablepropertyid_seq', 1, false);


--
-- Name: observationconstellationid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.observationconstellationid_seq', 1, false);


--
-- Name: observationid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.observationid_seq', 1, false);


--
-- Name: observationtypeid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.observationtypeid_seq', 1, false);


--
-- Name: offeringid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.offeringid_seq', 1, false);


--
-- Name: parameterid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.parameterid_seq', 1, false);


--
-- Name: procdescformatid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.procdescformatid_seq', 1, false);


--
-- Name: procedureid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.procedureid_seq', 1, false);


--
-- Name: relatedfeatureid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.relatedfeatureid_seq', 1, false);


--
-- Name: relatedfeatureroleid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.relatedfeatureroleid_seq', 1, false);


--
-- Name: resulttemplateid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.resulttemplateid_seq', 1, false);


--
-- Name: seriesid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.seriesid_seq', 1, false);


--
-- Name: unitid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.unitid_seq', 1, false);


--
-- Name: validproceduretimeid_seq; Type: SEQUENCE SET; Schema: public; Owner: sos
--

SELECT pg_catalog.setval('public.validproceduretimeid_seq', 1, false);


--
-- Name: blobvalue blobvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.blobvalue
    ADD CONSTRAINT blobvalue_pkey PRIMARY KEY (observationid);


--
-- Name: booleanvalue booleanvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.booleanvalue
    ADD CONSTRAINT booleanvalue_pkey PRIMARY KEY (observationid);


--
-- Name: categoryvalue categoryvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.categoryvalue
    ADD CONSTRAINT categoryvalue_pkey PRIMARY KEY (observationid);


--
-- Name: codespace codespace_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.codespace
    ADD CONSTRAINT codespace_pkey PRIMARY KEY (codespaceid);


--
-- Name: codespace codespaceuk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.codespace
    ADD CONSTRAINT codespaceuk UNIQUE (codespace);


--
-- Name: compositephenomenon compositephenomenon_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.compositephenomenon
    ADD CONSTRAINT compositephenomenon_pkey PRIMARY KEY (childobservablepropertyid, parentobservablepropertyid);


--
-- Name: countvalue countvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.countvalue
    ADD CONSTRAINT countvalue_pkey PRIMARY KEY (observationid);


--
-- Name: featureofinterest featureofinterest_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinterest
    ADD CONSTRAINT featureofinterest_pkey PRIMARY KEY (featureofinterestid);


--
-- Name: featureofinteresttype featureofinteresttype_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinteresttype
    ADD CONSTRAINT featureofinteresttype_pkey PRIMARY KEY (featureofinteresttypeid);


--
-- Name: featurerelation featurerelation_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featurerelation
    ADD CONSTRAINT featurerelation_pkey PRIMARY KEY (childfeatureid, parentfeatureid);


--
-- Name: featureofinteresttype featuretypeuk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinteresttype
    ADD CONSTRAINT featuretypeuk UNIQUE (featureofinteresttype);


--
-- Name: featureofinterest featureurl; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinterest
    ADD CONSTRAINT featureurl UNIQUE (url);


--
-- Name: featureofinterest foiidentifieruk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinterest
    ADD CONSTRAINT foiidentifieruk UNIQUE (identifier);


--
-- Name: geometryvalue geometryvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.geometryvalue
    ADD CONSTRAINT geometryvalue_pkey PRIMARY KEY (observationid);


--
-- Name: numericvalue numericvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.numericvalue
    ADD CONSTRAINT numericvalue_pkey PRIMARY KEY (observationid);


--
-- Name: observableproperty observableproperty_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observableproperty
    ADD CONSTRAINT observableproperty_pkey PRIMARY KEY (observablepropertyid);


--
-- Name: observation observation_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observation
    ADD CONSTRAINT observation_pkey PRIMARY KEY (observationid);


--
-- Name: observationconstellation observationconstellation_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationconstellation
    ADD CONSTRAINT observationconstellation_pkey PRIMARY KEY (observationconstellationid);


--
-- Name: observationhasoffering observationhasoffering_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationhasoffering
    ADD CONSTRAINT observationhasoffering_pkey PRIMARY KEY (observationid, offeringid);


--
-- Name: observation observationidentity; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observation
    ADD CONSTRAINT observationidentity UNIQUE (seriesid, phenomenontimestart, phenomenontimeend, resulttime);


--
-- Name: observationtype observationtype_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationtype
    ADD CONSTRAINT observationtype_pkey PRIMARY KEY (observationtypeid);


--
-- Name: observationtype observationtypeuk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationtype
    ADD CONSTRAINT observationtypeuk UNIQUE (observationtype);


--
-- Name: observationconstellation obsnconstellationidentity; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationconstellation
    ADD CONSTRAINT obsnconstellationidentity UNIQUE (observablepropertyid, procedureid, offeringid);


--
-- Name: observableproperty obspropidentifieruk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observableproperty
    ADD CONSTRAINT obspropidentifieruk UNIQUE (identifier);


--
-- Name: offering offering_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offering
    ADD CONSTRAINT offering_pkey PRIMARY KEY (offeringid);


--
-- Name: offeringallowedfeaturetype offeringallowedfeaturetype_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringallowedfeaturetype
    ADD CONSTRAINT offeringallowedfeaturetype_pkey PRIMARY KEY (offeringid, featureofinteresttypeid);


--
-- Name: offeringallowedobservationtype offeringallowedobservationtype_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringallowedobservationtype
    ADD CONSTRAINT offeringallowedobservationtype_pkey PRIMARY KEY (offeringid, observationtypeid);


--
-- Name: offeringhasrelatedfeature offeringhasrelatedfeature_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringhasrelatedfeature
    ADD CONSTRAINT offeringhasrelatedfeature_pkey PRIMARY KEY (offeringid, relatedfeatureid);


--
-- Name: offering offidentifieruk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offering
    ADD CONSTRAINT offidentifieruk UNIQUE (identifier);


--
-- Name: parameter parameter_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.parameter
    ADD CONSTRAINT parameter_pkey PRIMARY KEY (parameterid);


--
-- Name: proceduredescriptionformat procdescformatuk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.proceduredescriptionformat
    ADD CONSTRAINT procdescformatuk UNIQUE (proceduredescriptionformat);


--
-- Name: procedure procedure_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.procedure
    ADD CONSTRAINT procedure_pkey PRIMARY KEY (procedureid);


--
-- Name: proceduredescriptionformat proceduredescriptionformat_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.proceduredescriptionformat
    ADD CONSTRAINT proceduredescriptionformat_pkey PRIMARY KEY (proceduredescriptionformatid);


--
-- Name: procedure procidentifieruk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.procedure
    ADD CONSTRAINT procidentifieruk UNIQUE (identifier);


--
-- Name: relatedfeature relatedfeature_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.relatedfeature
    ADD CONSTRAINT relatedfeature_pkey PRIMARY KEY (relatedfeatureid);


--
-- Name: relatedfeaturehasrole relatedfeaturehasrole_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.relatedfeaturehasrole
    ADD CONSTRAINT relatedfeaturehasrole_pkey PRIMARY KEY (relatedfeatureid, relatedfeatureroleid);


--
-- Name: relatedfeaturerole relatedfeaturerole_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.relatedfeaturerole
    ADD CONSTRAINT relatedfeaturerole_pkey PRIMARY KEY (relatedfeatureroleid);


--
-- Name: relatedfeaturerole relfeatroleuk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.relatedfeaturerole
    ADD CONSTRAINT relfeatroleuk UNIQUE (relatedfeaturerole);


--
-- Name: resulttemplate resulttemplate_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.resulttemplate
    ADD CONSTRAINT resulttemplate_pkey PRIMARY KEY (resulttemplateid);


--
-- Name: sensorsystem sensorsystem_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.sensorsystem
    ADD CONSTRAINT sensorsystem_pkey PRIMARY KEY (childsensorid, parentsensorid);


--
-- Name: series series_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_pkey PRIMARY KEY (seriesid);


--
-- Name: series seriesidentity; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT seriesidentity UNIQUE (featureofinterestid, observablepropertyid, procedureid, offeringid);


--
-- Name: swedataarrayvalue swedataarrayvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.swedataarrayvalue
    ADD CONSTRAINT swedataarrayvalue_pkey PRIMARY KEY (observationid);


--
-- Name: textvalue textvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.textvalue
    ADD CONSTRAINT textvalue_pkey PRIMARY KEY (observationid);


--
-- Name: unit unit_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.unit
    ADD CONSTRAINT unit_pkey PRIMARY KEY (unitid);


--
-- Name: unit unituk; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.unit
    ADD CONSTRAINT unituk UNIQUE (unit);


--
-- Name: validproceduretime validproceduretime_pkey; Type: CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.validproceduretime
    ADD CONSTRAINT validproceduretime_pkey PRIMARY KEY (validproceduretimeid);


--
-- Name: obsconstobspropidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obsconstobspropidx ON public.observationconstellation USING btree (observablepropertyid);


--
-- Name: obsconstofferingidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obsconstofferingidx ON public.observationconstellation USING btree (offeringid);


--
-- Name: obsconstprocedureidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obsconstprocedureidx ON public.observationconstellation USING btree (procedureid);


--
-- Name: obshasoffobservationidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obshasoffobservationidx ON public.observationhasoffering USING btree (observationid);


--
-- Name: obshasoffofferingidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obshasoffofferingidx ON public.observationhasoffering USING btree (offeringid);


--
-- Name: obsphentimeendidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obsphentimeendidx ON public.observation USING btree (phenomenontimeend);


--
-- Name: obsphentimestartidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obsphentimestartidx ON public.observation USING btree (phenomenontimestart);


--
-- Name: obsresulttimeidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obsresulttimeidx ON public.observation USING btree (resulttime);


--
-- Name: obsseriesidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX obsseriesidx ON public.observation USING btree (seriesid);


--
-- Name: resulttempeobspropidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX resulttempeobspropidx ON public.resulttemplate USING btree (observablepropertyid);


--
-- Name: resulttempidentifieridx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX resulttempidentifieridx ON public.resulttemplate USING btree (identifier);


--
-- Name: resulttempofferingidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX resulttempofferingidx ON public.resulttemplate USING btree (offeringid);


--
-- Name: resulttempprocedureidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX resulttempprocedureidx ON public.resulttemplate USING btree (procedureid);


--
-- Name: seriesfeatureidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX seriesfeatureidx ON public.series USING btree (featureofinterestid);


--
-- Name: seriesobspropidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX seriesobspropidx ON public.series USING btree (observablepropertyid);


--
-- Name: seriesofferingidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX seriesofferingidx ON public.series USING btree (offeringid);


--
-- Name: seriesprocedureidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX seriesprocedureidx ON public.series USING btree (procedureid);


--
-- Name: validproceduretimeendtimeidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX validproceduretimeendtimeidx ON public.validproceduretime USING btree (endtime);


--
-- Name: validproceduretimestarttimeidx; Type: INDEX; Schema: public; Owner: sos
--

CREATE INDEX validproceduretimestarttimeidx ON public.validproceduretime USING btree (starttime);


--
-- Name: featureofinterest featurecodespaceidentifierfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinterest
    ADD CONSTRAINT featurecodespaceidentifierfk FOREIGN KEY (codespace) REFERENCES public.codespace(codespaceid);


--
-- Name: featureofinterest featurecodespacenamefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinterest
    ADD CONSTRAINT featurecodespacenamefk FOREIGN KEY (codespacename) REFERENCES public.codespace(codespaceid);


--
-- Name: featureofinterest featurefeaturetypefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featureofinterest
    ADD CONSTRAINT featurefeaturetypefk FOREIGN KEY (featureofinteresttypeid) REFERENCES public.featureofinteresttype(featureofinteresttypeid);


--
-- Name: featurerelation featureofinterestchildfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featurerelation
    ADD CONSTRAINT featureofinterestchildfk FOREIGN KEY (childfeatureid) REFERENCES public.featureofinterest(featureofinterestid);


--
-- Name: featurerelation featureofinterestparentfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.featurerelation
    ADD CONSTRAINT featureofinterestparentfk FOREIGN KEY (parentfeatureid) REFERENCES public.featureofinterest(featureofinterestid);


--
-- Name: offeringallowedfeaturetype fk_6vvrdxvd406n48gkm706ow1pt; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringallowedfeaturetype
    ADD CONSTRAINT fk_6vvrdxvd406n48gkm706ow1pt FOREIGN KEY (offeringid) REFERENCES public.offering(offeringid);


--
-- Name: relatedfeaturehasrole fk_6ynwkk91xe8p1uibmjt98sog3; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.relatedfeaturehasrole
    ADD CONSTRAINT fk_6ynwkk91xe8p1uibmjt98sog3 FOREIGN KEY (relatedfeatureid) REFERENCES public.relatedfeature(relatedfeatureid);


--
-- Name: observationhasoffering fk_9ex7hawh3dbplkllmw5w3kvej; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationhasoffering
    ADD CONSTRAINT fk_9ex7hawh3dbplkllmw5w3kvej FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: offeringallowedobservationtype fk_lkljeohulvu7cr26pduyp5bd0; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringallowedobservationtype
    ADD CONSTRAINT fk_lkljeohulvu7cr26pduyp5bd0 FOREIGN KEY (offeringid) REFERENCES public.offering(offeringid);


--
-- Name: observation obscodespaceidentifierfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observation
    ADD CONSTRAINT obscodespaceidentifierfk FOREIGN KEY (codespace) REFERENCES public.codespace(codespaceid);


--
-- Name: observation obscodespacenamefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observation
    ADD CONSTRAINT obscodespacenamefk FOREIGN KEY (codespacename) REFERENCES public.codespace(codespaceid);


--
-- Name: observationconstellation obsconstobservationiypefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationconstellation
    ADD CONSTRAINT obsconstobservationiypefk FOREIGN KEY (observationtypeid) REFERENCES public.observationtype(observationtypeid);


--
-- Name: observationconstellation obsconstobspropfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationconstellation
    ADD CONSTRAINT obsconstobspropfk FOREIGN KEY (observablepropertyid) REFERENCES public.observableproperty(observablepropertyid);


--
-- Name: observationconstellation obsconstofferingfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationconstellation
    ADD CONSTRAINT obsconstofferingfk FOREIGN KEY (offeringid) REFERENCES public.offering(offeringid);


--
-- Name: compositephenomenon observablepropertychildfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.compositephenomenon
    ADD CONSTRAINT observablepropertychildfk FOREIGN KEY (childobservablepropertyid) REFERENCES public.observableproperty(observablepropertyid);


--
-- Name: compositephenomenon observablepropertyparentfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.compositephenomenon
    ADD CONSTRAINT observablepropertyparentfk FOREIGN KEY (parentobservablepropertyid) REFERENCES public.observableproperty(observablepropertyid);


--
-- Name: blobvalue observationblobvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.blobvalue
    ADD CONSTRAINT observationblobvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: booleanvalue observationbooleanvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.booleanvalue
    ADD CONSTRAINT observationbooleanvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: categoryvalue observationcategoryvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.categoryvalue
    ADD CONSTRAINT observationcategoryvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: countvalue observationcountvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.countvalue
    ADD CONSTRAINT observationcountvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: geometryvalue observationgeometryvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.geometryvalue
    ADD CONSTRAINT observationgeometryvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: numericvalue observationnumericvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.numericvalue
    ADD CONSTRAINT observationnumericvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: observationhasoffering observationofferingfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationhasoffering
    ADD CONSTRAINT observationofferingfk FOREIGN KEY (offeringid) REFERENCES public.offering(offeringid);


--
-- Name: observation observationseriesfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observation
    ADD CONSTRAINT observationseriesfk FOREIGN KEY (seriesid) REFERENCES public.series(seriesid);


--
-- Name: swedataarrayvalue observationswedataarrayvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.swedataarrayvalue
    ADD CONSTRAINT observationswedataarrayvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: textvalue observationtextvaluefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.textvalue
    ADD CONSTRAINT observationtextvaluefk FOREIGN KEY (observationid) REFERENCES public.observation(observationid);


--
-- Name: observation observationunitfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observation
    ADD CONSTRAINT observationunitfk FOREIGN KEY (unitid) REFERENCES public.unit(unitid);


--
-- Name: observationconstellation obsnconstprocedurefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observationconstellation
    ADD CONSTRAINT obsnconstprocedurefk FOREIGN KEY (procedureid) REFERENCES public.procedure(procedureid);


--
-- Name: observableproperty obspropcodespaceidentifierfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observableproperty
    ADD CONSTRAINT obspropcodespaceidentifierfk FOREIGN KEY (codespace) REFERENCES public.codespace(codespaceid);


--
-- Name: observableproperty obspropcodespacenamefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.observableproperty
    ADD CONSTRAINT obspropcodespacenamefk FOREIGN KEY (codespacename) REFERENCES public.codespace(codespaceid);


--
-- Name: offering offcodespaceidentifierfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offering
    ADD CONSTRAINT offcodespaceidentifierfk FOREIGN KEY (codespace) REFERENCES public.codespace(codespaceid);


--
-- Name: offering offcodespacenamefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offering
    ADD CONSTRAINT offcodespacenamefk FOREIGN KEY (codespacename) REFERENCES public.codespace(codespaceid);


--
-- Name: offeringallowedfeaturetype offeringfeaturetypefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringallowedfeaturetype
    ADD CONSTRAINT offeringfeaturetypefk FOREIGN KEY (featureofinteresttypeid) REFERENCES public.featureofinteresttype(featureofinteresttypeid);


--
-- Name: offeringallowedobservationtype offeringobservationtypefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringallowedobservationtype
    ADD CONSTRAINT offeringobservationtypefk FOREIGN KEY (observationtypeid) REFERENCES public.observationtype(observationtypeid);


--
-- Name: offeringhasrelatedfeature offeringrelatedfeaturefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringhasrelatedfeature
    ADD CONSTRAINT offeringrelatedfeaturefk FOREIGN KEY (relatedfeatureid) REFERENCES public.relatedfeature(relatedfeatureid);


--
-- Name: procedure proccodespaceidentifierfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.procedure
    ADD CONSTRAINT proccodespaceidentifierfk FOREIGN KEY (codespace) REFERENCES public.codespace(codespaceid);


--
-- Name: procedure proccodespacenamefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.procedure
    ADD CONSTRAINT proccodespacenamefk FOREIGN KEY (codespacename) REFERENCES public.codespace(codespaceid);


--
-- Name: sensorsystem procedurechildfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.sensorsystem
    ADD CONSTRAINT procedurechildfk FOREIGN KEY (childsensorid) REFERENCES public.procedure(procedureid);


--
-- Name: sensorsystem procedureparenffk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.sensorsystem
    ADD CONSTRAINT procedureparenffk FOREIGN KEY (parentsensorid) REFERENCES public.procedure(procedureid);


--
-- Name: procedure procprocdescformatfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.procedure
    ADD CONSTRAINT procprocdescformatfk FOREIGN KEY (proceduredescriptionformatid) REFERENCES public.proceduredescriptionformat(proceduredescriptionformatid);


--
-- Name: relatedfeaturehasrole relatedfeatrelatedfeatrolefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.relatedfeaturehasrole
    ADD CONSTRAINT relatedfeatrelatedfeatrolefk FOREIGN KEY (relatedfeatureroleid) REFERENCES public.relatedfeaturerole(relatedfeatureroleid);


--
-- Name: relatedfeature relatedfeaturefeaturefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.relatedfeature
    ADD CONSTRAINT relatedfeaturefeaturefk FOREIGN KEY (featureofinterestid) REFERENCES public.featureofinterest(featureofinterestid);


--
-- Name: offeringhasrelatedfeature relatedfeatureofferingfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.offeringhasrelatedfeature
    ADD CONSTRAINT relatedfeatureofferingfk FOREIGN KEY (offeringid) REFERENCES public.offering(offeringid);


--
-- Name: resulttemplate resulttemplatefeatureidx; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.resulttemplate
    ADD CONSTRAINT resulttemplatefeatureidx FOREIGN KEY (featureofinterestid) REFERENCES public.featureofinterest(featureofinterestid);


--
-- Name: resulttemplate resulttemplateobspropfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.resulttemplate
    ADD CONSTRAINT resulttemplateobspropfk FOREIGN KEY (observablepropertyid) REFERENCES public.observableproperty(observablepropertyid);


--
-- Name: resulttemplate resulttemplateofferingidx; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.resulttemplate
    ADD CONSTRAINT resulttemplateofferingidx FOREIGN KEY (offeringid) REFERENCES public.offering(offeringid);


--
-- Name: resulttemplate resulttemplateprocedurefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.resulttemplate
    ADD CONSTRAINT resulttemplateprocedurefk FOREIGN KEY (procedureid) REFERENCES public.procedure(procedureid);


--
-- Name: series seriesfeaturefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT seriesfeaturefk FOREIGN KEY (featureofinterestid) REFERENCES public.featureofinterest(featureofinterestid);


--
-- Name: series seriesobpropfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT seriesobpropfk FOREIGN KEY (observablepropertyid) REFERENCES public.observableproperty(observablepropertyid);


--
-- Name: series seriesofferingfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT seriesofferingfk FOREIGN KEY (offeringid) REFERENCES public.offering(offeringid);


--
-- Name: series seriesprocedurefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT seriesprocedurefk FOREIGN KEY (procedureid) REFERENCES public.procedure(procedureid);


--
-- Name: series seriesunitfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT seriesunitfk FOREIGN KEY (unitid) REFERENCES public.unit(unitid);


--
-- Name: validproceduretime validproceduretimeprocedurefk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.validproceduretime
    ADD CONSTRAINT validproceduretimeprocedurefk FOREIGN KEY (procedureid) REFERENCES public.procedure(procedureid);


--
-- Name: validproceduretime validprocprocdescformatfk; Type: FK CONSTRAINT; Schema: public; Owner: sos
--

ALTER TABLE ONLY public.validproceduretime
    ADD CONSTRAINT validprocprocdescformatfk FOREIGN KEY (proceduredescriptionformatid) REFERENCES public.proceduredescriptionformat(proceduredescriptionformatid);


--
-- PostgreSQL database dump complete
--

