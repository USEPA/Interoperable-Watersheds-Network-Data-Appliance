var ingest = {
    globals: {
        variables: {
            orgId: null
        },
        templates: {
            yesTemplate: "<i class='fas fa-check'></i>",
            noTemplate: "<i class='fas fa-times'></i>",
            successTemplate: "<i class='fas fa-arrow-circle-up text-success'></i>",
            unknownTemplate: "<i class='fas fa-exclamation-triangle text-warning'></i>",
            failureTemplate: "<i class='fas fa-arrow-circle-down text-danger'></i>",
            sensorEditTemplate: "<a href='javascript:void(0)' onclick='ingest.showEditSensorModal([sensor_id]);'><i class='fas fa-edit'></i></a>",
            sensorDeleteTemplate: "<a href='javascript:void(0)' onclick='ingest.deleteSensor([sensor_id]);'><i class='fas fa-trash-alt'></i></a>",
            qcEditTemplate: "<a href='javascript:void(0)' onclick='ingest.showEditQcModal([qc_id]);'><i class='fas fa-edit'></i></a>",
            qcDeleteTemplate: "<a href='javascript:void(0)' onclick='ingest.deleteQc([qc_id]);'><i class='fas fa-trash-alt'></i></a>"
        },
        services: {
            orgs: config.serviceUrl + "orgs/",
            sensors: config.serviceUrl + "sensors/",
            parameters: config.serviceUrl + "parameters/",
            units: config.serviceUrl + "units/",
            domains: config.serviceUrl + "domains/"
        },
        text: {
            orgNotFound: "Organization not found. Unable to load data.",
            selectParameter: "Select a parameter",
            selectUnit: "Select a unit",
            selectMediumType: "Select the medium type",
            selectDataQuality: "Select the data quality",
            selectUnit: "Select a unit",
            enterDataColumn: "Enter the parameter data column",
            selectOperand: "Select an operand",
            selectAction: "Select an action",
            confirm: "Are you sure?",
            addSensor: "Add Sensor",
            editSensor: "Edit Sensor",
            sensorSaved: "Sensor saved!",
            sensorDeleted: "Sensor deleted!",
            addQc: "Add Quality Control",
            editQc: "Edit Quality Control",
            qcSaved: "Quality control saved!",
            qcDeleted: "Quality control deleted!"
        }
    },
    init: function () {
        //initialize page values and settings

        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //get query string parameters
        var params = helper.getQueryStringParams();
        g.variables.orgId = params["orgId"];

        if (g.variables.orgId != null) {
            //populate organization table and QC table
            $("#qcTable").bootstrapTable();
            me.callOrgService();

            //populate sensors table
            $("#sensorsTable").bootstrapTable();
            me.callSensorsService();

            //call parameters service and populate dropdowns
            helper.callService(s.parameters, "", "GET", function (data) {
                ingest.populateSelect("sensorParameter", data, "parameter_name", "parameter_id", g.text.selectParameter);
                ingest.populateSelect("qcParameter", data, "parameter_name", "parameter_id", g.text.selectParameter);
            });

            //call units service and populate dropdown
            helper.callService(s.units, "", "GET", function (data) {
                ingest.populateSelect("sensorUnit", data, "unit_name", "unit_id", g.text.selectUnit);
            });

            //call domains service and populate dropdowns
            helper.callService(s.domains, "", "GET", function (data) {
                ingest.populateSelect("sensorMediumType", data.medium_types, "medium_type_name", "medium_type_id", g.text.selectMediumType);
                ingest.populateSelect("sensorQuality", data.qualifiers, "data_qualifier_name", "data_qualifier_id", g.text.selectDataQuality);
                ingest.populateSelect("qcOperand", data.operands, "quality_check_operand_name", "quality_check_operand_id", g.text.selectOperand);
                ingest.populateSelect("qcAction", data.actions, "quality_check_action_name", "quality_check_action_id", g.text.selectAction);
            });

            //button handler for adding parameter to sensor form
            $("#btnAddSensorParameter").on("click", function () {
                ingest.addSensorParameter();
            });

            //initialize title and sensor parameters table when sensor form is shown
            $("#sensorModal").on("show.bs.modal", function () {
                $("#sensorModalTabs a[href='#sensorInfoTabContent']").tab("show");
                if ($("#sensorUid").val() == "") {
                    $("#sensorModalTitle").text(g.text.addSensor);
                    $("#sensorParametersTable").bootstrapTable();
                }
                else {
                    $("#sensorModalTitle").text(g.text.editSensor);
                }
            });

            //initialize title when QC form is shown
            $("#qcModal").on("show.bs.modal", function () {
                if ($("#qcUid").val() == "") {
                    $("#qcModalTitle").text(g.text.addQc);
                }
                else {
                    $("#qcModalTitle").text(g.text.editQc);
                }
            });

            //reset sensors form when form is hidden
            $("#sensorModal").on("hidden.bs.modal", function () {
                ingest.resetSensorModal();
            });

            //reset QC form when form is hidden
            $("#qcModal").on("hidden.bs.modal", function () {
                ingest.resetQcModal();
            });
        }
        else {
            alert(g.text.orgNotFound);
        }
    },
    callOrgService(callback) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //call org service and populate organization table and QC table
        helper.callService(s.orgs + g.variables.orgId, "", "GET", function (data) {
            if (callback) {
                callback(data);
            }
            else {
                me.loadOrgTable(data);
                me.loadQcTable(data);
            }
        });
    },
    callSensorsService(callback) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //call sensors service and populate sensors table
        helper.callService(s.sensors, "", "GET", function (data) {
            if (callback) {
                callback(data);
            }
            else {
                $("#sensorsTable").bootstrapTable("load", data);
            }
        });
    },
    loadOrgTable: function(data) {
        $("#orgParentId").text(data.parent_organization_id);
        $("#orgName").text(data.name);
        $("#orgId").text(data.organization_id);
        $("#orgUrl").text(data.sos_url);
        $("#contactName").text(data.contact_name);
        $("#contactEmail").text(data.contact_email);
    },
    loadQcTable: function(data) {
        var qcData = data.quality_checks;

        //*** temporary ***
        //add name fields from lookup data to QC data in order to display in summary table
        $.each(data.quality_checks, function (index, record) {
            var parameterId = record.parameter_id;
            var parameterData = $.grep(lookup.parameters, function (record, index) {
                return record.parameter_id == parameterId;
            });
            qcData[index].parameter_name = parameterData[0].parameter_name;
            var actionId = record.quality_check_action_id;
            var actionData = $.grep(lookup.domains.actions, function (record, index) {
                return record.quality_check_action_id == actionId;
            });
            qcData[index].quality_check_action_name = actionData[0].quality_check_action_name;
            var operandId = record.quality_check_operand_id;
            var operandData = $.grep(lookup.domains.operands, function (record, index) {
                return record.quality_check_operand_id == operandId;
            });
            qcData[index].quality_check_operand_name = operandData[0].quality_check_operand_name;
        });
        //*** end temporary ***

        $("#qcTable").bootstrapTable("load", qcData);
    },
    sensorEditFormatter: function (value) {
        //bootstrap-table formatter for editing row of sensors table
        //creates a link to launch edit sensor form

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.sensorEditTemplate.replace("\[sensor_id\]", value);
        return link;
    },
    sensorDeleteFormatter: function (value) {
        //bootstrap-table formatter for deleting row of sensors table
        //creates a link to delete sensor

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.sensorDeleteTemplate.replace("\[sensor_id\]", value);
        return link;
    },
    dateFormatter: function (value) {
        //bootstrap-table formatter for a date column
        //converts date to local date with timezone (uses moment.js)

        var formattedDate = "";
        if (value != null) {
            var utcDate = value;
            var localDate = new Date(utcDate);
            var tz = moment.tz.guess();
            formattedDate = localDate.toLocaleDateString("en-US") + " " + localDate.toLocaleTimeString("en-US") + " " + moment.tz(tz).format("z");
        }
        return formattedDate;
    },
    qcRulesApplyFormatter: function (value) {
        //boostrap-table formatter for qc rules apply column of sensors table
        //replaces column text with an icon based on text value

        var me = ingest;
        var g = me.globals;
        var t = g.templates;
        
        var icon = t.noTemplate;
        if (value == true) {
            icon = t.yesTemplate;
        }
        return icon;
    },
    ingestStatusFormatter: function (value) {
        //boostrap-table formatter for ingest status column of sensors table
        //replaces column text with an icon based on text value

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var icon = t.unknownTemplate;
        switch (value) {
            case "ingested":
                icon = t.successTemplate;
                break;
            case "error":
                icon = t.failureTemplate;
                break;
        }
        return icon;
    },
    qcEditFormatter: function (value, row) {
        //boostrap-table formatter for editing row of QC table
        //creates a link to launch edit QC form

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.qcEditTemplate.replace("\[qc_id\]", value);
        return link;
    },
    qcDeleteFormatter: function (value, row) {
        //boostrap-table formatter for deleting row of QC table
        //creates a link to delete QC

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.qcDeleteTemplate.replace("\[qc_id\]", value);
        return link;
    },
    populateSelect: function (selectId, data, nameField, idField, placeholderText) {
        //populates a select element with name and id from json object

        var ddl = $("#" + selectId);
        ddl.append($("<option />").val("").text(placeholderText).prop("selected", true));
        $.each(data, function () {
            ddl.append($("<option />").val(this[idField]).text(this[nameField]));
        });
    },
    showEditSensorModal: function (uid) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //launch edit sensor form and populate with existing sensor data based on sensor id
        $("#sensorUid").val(uid);

        //call sensors service and populate form
        helper.callService(s.sensors + uid, "", "GET", function (data) {
            $("#sensorId").val(data.org_sensor_id);
            $("#sensorId").prop("disabled", true);
            $("#sensorNameShort").val(data.short_name);
            $("#sensorNameLong").val(data.long_name);
            $("#sensorMediumType").val(data.medium_type_id);
            $("#sensorLatitude").val(data.latitude);
            $("#sensorLongitude").val(data.longitude);
            $("#sensorAltitude").val(data.altitude);
            $("#sensorLongitude").val(data.longitude);
            $("#sensorTimeZone").val(data.timezone);
            $("#sensorIngestFrequency").val(data.ingest_frequency);
            $("#sensorUrl").val(data.data_url);
            $("#sensorQuality").val(data.data_qualifier_id);
            $("#sensorTimestampColumn").val(data.timestamp_column_id);
            $("#sensorApplyQc").prop("checked", data.qc_rules_apply);

            var sensorParametersData = data.parameters;
            //*** temporary ***
            //add name fields from lookup data to sensor parameter data in order to display in table
            $.each(data.parameters, function (index, record) {
                var parameterId = record.parameter_id;
                var parameterData = $.grep(lookup.parameters, function (record, index) {
                    return record.parameter_id == parameterId;
                });
                sensorParametersData[index].parameter_name = parameterData[0].parameter_name;
                var unitId = record.unit_id;
                var unitData = $.grep(lookup.units, function (record, index) {
                    return record.unit_id == unitId;
                });
                sensorParametersData[index].unit_name = unitData[0].unit_name;
            });
            //*** end temporary ***
            $("#sensorParametersTable").bootstrapTable();
            $("#sensorParametersTable").bootstrapTable("load", sensorParametersData);
            $("#sensorModal").modal("show");
        });
    },
    addSensorParameter: function () {
        var me = ingest;
        var g = me.globals;

        var data = {};
        data.sensor_id = $("#sensorUid").val();
        data.parameter_id = $("#sensorParameter").val();
        data.unit_id = $("#sensorUnit").val();
        data.parameter_column_id = $("#sensorParameterColumn").val();
        if (data.parameter_id == "") {
            alert(g.text.selectParameter);
        }
        else if (data.unit_id == "") {
            alert(g.text.selectUnit);
        }
        else if (data.parameter_column_id == "") {
            alert(g.text.enterDataColumn);
        }
        else {
            $("#sensorParametersTable").bootstrapTable("append", [data]);
            $("#sensorParameter").val("");
            $("#sensorUnit").val("");
            $("#sensorParameterColumn").val("");
        }
    },
    resetSensorModal: function () {
        //reset sensor form
        $("#sensorUid").val("");
        $("#sensorId").val("");
        $("#sensorId").prop("disabled", false);
        $("#sensorNameShort").val("");
        $("#sensorNameLong").val("");
        $("#sensorMediumType").val("");
        $("#sensorLatitude").val("");
        $("#sensorLongitude").val("");
        $("#sensorAltitude").val("");
        $("#sensorLongitude").val("");
        $("#sensorTimeZone").val("");
        $("#sensorIngestFrequency").val("");
        $("#sensorUrl").val("");
        $("#sensorQuality").val("");
        $("#sensorTimestampColumn").val("");
        $("#sensorApplyQc").prop("checked", false);
        $("#sensorParameter").val("");
        $("#sensorUnit").val("");
        $("#sensorParameterColumn").val("");
        $("#sensorParametersTable").bootstrapTable("destroy");
    },
    saveSensor: function () {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        var uid = $("#sensorUid").val();
        
        var data = {};
        data.organization_id = g.variables.orgId;
        data.org_sensor_id = $("#sensorId").val();
        data.data_qualifier_id = $("#sensorQuality").val();
        data.medium_type_id = $("#sensorMediumType").val();
        data.short_name = $("#sensorNameShort").val();
        data.long_name = $("#sensorNameLong").val();
        data.latitude = $("#sensorLatitude").val();
        data.longitude = $("#sensorLongitude").val();
        data.altitude - $("#sensorAltitude").val();
        data.timezone = $("#sensorTimeZone").val();
        data.ingest_frequency = $("#sensorIngestFrequency").val();
        data.data_url = $("#sensorUrl").val();
        data.data_format = 0; //what is this???
        data.timestamp_column_id = $("#sensorTimestampColumn").val();
        data.qc_rules_apply = $("#sensorApplyQc").prop("checked");
        data.active = true; //what is this???
        data.parameters = $("#sensorParametersTable").bootstrapTable("getData");


        if (uid != "") {
            //call sensor update service
            helper.callService(s.sensors + uid, data, "PUT", function (data) {
                alert(g.text.sensorSaved);
                $("#sensorModal").modal("hide");
                me.callSensorsService();
            });
        }
        else {
            //*** temporary ***
            data.parameters = [];
            //*** end temporary ***

            //call sensor create service
            helper.callService(s.sensors, data, "POST", function (data) {

                //*** temporary ***
                $("#sensorUid").val(data.sensor_id);
                data.parameters = $("#sensorParametersTable").bootstrapTable("getData");
                $.each(data.parameters, function (index, record) {
                    record.sensor_id = data.sensor_id;
                });
                $("#sensorParametersTable").bootstrapTable("load", data.parameters);
                me.saveSensor();
                //*** end temporary ***

                //alert(g.text.sensorSaved);
                //$("#sensorModal").modal("hide");
                //reset
                //me.callSensorsService();
            });
        }
    },
    deleteSensor: function (uid) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        if (confirm(g.text.confirm)) {
            //call sensor delete service
            helper.callService(s.sensors + uid, "", "DELETE", function (data) {
                alert(g.text.sensorDeleted);
                $("#sensorModal").modal("hide");
                me.callSensorsService();
            });
        }
    },
    showEditQcModal: function(uid) {
        var qcData = $("#qcTable").bootstrapTable("getData");
        var rowData = $.grep(qcData, function (record, index) {
            return record.org_parameter_quality_check_id == uid;
        });
        $("#qcUid").val(uid);
        $("#qcParameter").val(rowData[0].parameter_id.toString());
        $("#qcOperand").val(rowData[0].quality_check_operand_id);
        $("#qcThreshold").val(rowData[0].threshold);
        $("#qcAction").val(rowData[0].quality_check_action_id);
        $("#qcModal").modal("show");
    },
    resetQcModal: function () {
        //reset QC form
        $("#qcUid").val("");
        $("#qcParameter").val("");
        $("#qcOperand").val("");
        $("#qcThreshold").val("");
        $("#qcAction").val("");
    },
    saveQc: function () {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        var uid = $("#qcUid").val();

        var data = {};
        data.organization_id = g.variables.orgId;
        data.parameter_id = $("#qcParameter").val();
        data.parameter_name = $("#qcParameter option:selected").text();
        data.quality_check_operand_id = $("#qcOperand").val();
        data.quality_check_operand_name = $("#qcOperand option:selected").text();
        data.threshold = $("#qcThreshold").val();
        data.quality_check_action_id = $("#qcAction").val();
        data.quality_check_action_name = $("#qcAction option:selected").text();
        if (uid != "") {
            var index = $.map($("#qcTable").bootstrapTable("getData"), function (record, index) {
                if (record.org_parameter_quality_check_id == uid) {
                    return index;
                }
            });
            $("#qcTable").bootstrapTable("updateRow", { index: index, row: data });
        }
        else {
            data.org_parameter_quality_check_id = Date.now();
            $("#qcTable").bootstrapTable("append", [data]);
        }
        var qcData = $("#qcTable").bootstrapTable("getData");
        $.each(qcData, function (index, record) {
            delete record.org_parameter_quality_check_id;
            delete record.parameter_name;
            delete record.quality_check_operand_name;
            delete record.quality_check_action_name;
            record.organization_id = g.variables.orgId;
        });
        me.callOrgService(function (data) {
            data.quality_checks = qcData;
            //call org update service to update QC data
            helper.callService(s.orgs + g.variables.orgId, data, "PUT", function (data) {
                alert(g.text.qcSaved);
                $("#qcModal").modal("hide");
                me.callOrgService(me.loadQcTable(data));
            });
        });
    },
    deleteQc: function (uid) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        if (confirm(g.text.confirm)) {
            //update organization data to remove QC record
            var qcData = $("#qcTable").bootstrapTable("getData");
            var newQcData = $.grep(qcData, function (record, index) {
                return record.org_parameter_quality_check_id != uid;
            });
            $.each(newQcData, function (index, record) {
                delete record.org_parameter_quality_check_id;
                delete record.parameter_name;
                delete record.quality_check_operand_name;
                delete record.quality_check_action_name;
                record.organization_id = g.variables.orgId;
            });
            me.callOrgService(function (data) {
                data.quality_checks = newQcData;
                //call org update service to update QC data
                helper.callService(s.orgs + g.variables.orgId, data, "PUT", function (data) {
                    alert(g.text.qcDeleted);
                    $("#qcModal").modal("hide");
                    me.callOrgService(me.loadQcTable(data));
                });
            });
        }
    }
};

$("document").ready(function () {
    //runs when page loads

    ingest.init();
});
