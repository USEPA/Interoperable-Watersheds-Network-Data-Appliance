var ingest = {
    globals: {
        //global variables
        variables: {
            token: null,
            orgId: null,
            username: null,
            isadmin: null
        },
        //html templates for bootstrap tables
        templates: {
            yesTemplate: "<i class='fas fa-check'></i>",
            noTemplate: "<i class='fas fa-times'></i>",
            successTemplate: "<i class='fas fa-arrow-circle-up text-success'></i>",
            unknownTemplate: "<i class='fas fa-exclamation-triangle text-warning'></i>",
            failureTemplate: "<i class='fas fa-arrow-circle-down text-danger'></i>",
            sensorEditTemplate: "<a href='javascript:void(0)' onclick='ingest.showEditSensorModal([sensor_id]);'><i class='fas fa-edit'></i></a>",
            sensorDeleteTemplate: "<a href='javascript:void(0)' onclick='ingest.deleteSensor([sensor_id]);'><i class='fas fa-trash-alt'></i></a>",
            paramDeleteTemplate: "<input name='grpDeleteParams' type='checkbox' value='[parameter_id]' />",
            qcEditTemplate: "<a href='javascript:void(0)' onclick='ingest.showEditQcModal([qc_id]);'><i class='fas fa-edit'></i></a>",
            qcDeleteTemplate: "<a href='javascript:void(0)' onclick='ingest.deleteQc([qc_id]);'><i class='fas fa-trash-alt'></i></a>",
            adminEditTemplate: "<a href='javascript:void(0)' onclick='ingest.showEditAdminModal([admin_id]);'><i class='fas fa-edit'></i></a>",
            adminDeleteTemplate: "<a href='javascript:void(0)' onclick='ingest.deleteAdmin([admin_id]);'><i class='fas fa-trash-alt'></i></a>"
        },
        //web services
        services: {
            orgs: config.serviceUrl + "orgs/",
            sensors: config.serviceUrl + "sensors/",
            parameters: config.serviceUrl + "parameters/",
            units: config.serviceUrl + "units/",
            domains: config.serviceUrl + "domains/",
            users: config.authUrl + "users/",
            user: config.authUrl + "user/"
        },
        //site text
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
            qcDeleted: "Quality control deleted!",
            addAdmin: "Add User",
            editAdmin: "Edit User",
            adminSaved: "User saved!",
            adminDeleted: "User deleted!"
        }
    },
    validToken: function (token) {
        var me = ingest;
        var base64Url = token.split('.')[1];
        var base64 = base64Url.replace('-', '+').replace('_', '/');
        var roles = JSON.parse(window.atob(base64)).authorities;

        if(roles!=null)
            var arrayLength = roles.length;
            if(arrayLength>0){
              me.globals.username = JSON.parse(window.atob(base64)).user_name;
                for (var i = 0; i < arrayLength; i++) {
                    //console.log(roles[i]);
                    if(roles[i]=='ADMIN_USER'){
                      me.globals.isAdmin=true;
                    }
                }
            }
        return me.globals.username!=null;
    },
    init: function () {
        //initialize page values and settings

        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //get query string parameters
        var params = helper.getQueryStringParams();
        g.variables.token = params["access_token"];
        g.variables.orgId = params["orgId"];

        if (g.variables.token != null && this.validToken(g.variables.token)) {

            if (g.variables.orgId != null) {
                //populate organization table and QC table
                $("#qcTable").bootstrapTable();
                me.callOrgService();

                //populate sensors table
                $("#sensorsTable").bootstrapTable();
                me.callSensorsService();

                //call parameters service and populate dropdowns
                helper.callService(s.parameters, "", g.variables.token, "GET", function (data) {
                    ingest.populateSelect("sensorParameter", data, "parameter_name", "parameter_id", g.text.selectParameter);
                    ingest.populateSelect("qcParameter", data, "parameter_name", "parameter_id", g.text.selectParameter);
                });

                //call units service and populate dropdown
                helper.callService(s.units, "", g.variables.token,"GET", function (data) {
                    ingest.populateSelect("sensorUnit", data, "unit_name", "unit_id", g.text.selectUnit);
                });

                //call domains service and populate dropdowns
                helper.callService(s.domains, "", g.variables.token,"GET", function (data) {
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
                    $("#sensorValidityWarning").hide();
                    $("#sensorModalTabs a[href='#sensorInfoTabContent']").tab("show");
                    if ($("#sensorUid").val() == "") {
                        $("#sensorModalTitle").text(g.text.addSensor);
                        $("#sensorParametersTable").bootstrapTable();
                    } else {
                        $("#sensorModalTitle").text(g.text.editSensor);
                    }
                });

                //initialize title when QC form is shown
                $("#qcModal").on("show.bs.modal", function () {
                    if ($("#qcUid").val() == "") {
                        $("#qcModalTitle").text(g.text.addQc);
                    } else {
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

                //reset Admin form when form is hidden
                $("#adminModal").on("hidden.bs.modal", function () {
                    ingest.resetAdminModal();
                });
                //admin section
                $("#adminSection").hide();
                if(g.isAdmin){
                    $("#adminSection").show();
                    $("#adminTable").bootstrapTable();
                    me.callUserService();
/*                    //call users service and populate dropdowns
                    helper.callService(s.users, "", g.variables.token,"GET", function (data) {
                        ingest.populateSelect("id", data.medium_types, "id", "medium_type_id", g.text.selectMediumType);
                        ingest.populateSelect("username", data.qualifiers, "user_name", "data_qualifier_id", g.text.selectDataQuality);
                        ingest.populateSelect("email", data.operands, "email", "quality_check_operand_id", g.text.selectOperand);
                        ingest.populateSelect("roles", data.actions, "roles", "quality_check_action_id", g.text.selectAction);
                    });*/
                }
            } else {
                //display alert when no organization ID found in query string
                alert(g.text.orgNotFound);
            }
        }else{
            window.location.href = config.authLogin;
        }
    },
    callOrgService(callback) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //call org service and populate organization table and QC table
        helper.callService(s.orgs + g.variables.orgId, "", g.variables.token,"GET", function (data) {
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
        helper.callService(s.sensors, "", g.variables.token,"GET", function (data) {
            if (callback) {
                callback(data);
            }
            else {
                $("#sensorsTable").bootstrapTable("load", data);
            }
        });
    },
    callUserService(callback) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //call user service and populate user table
        helper.callService(s.users, "", g.variables.token,"GET", function (data) {
            if (callback) {
                callback(data);
            }
            else {
                me.loadUserTable(data);
            }
        });
    },
    loadUserTable: function (data) {
        if(data && data.data){
          $("#adminTable").bootstrapTable("load", data.data[0]);
        }
    },
    loadOrgTable: function (data) {
        //load data into organizations table

        $("#orgParentId").text(data.parent_organization_id);
        $("#orgName").text(data.name);
        $("#orgId").text(data.organization_id);
        $("#orgUrl").text(data.sos_url);
        $("#contactName").text(data.contact_name);
        $("#contactEmail").text(data.contact_email);
    },
    loadQcTable: function(data) {
        var qcData = data.quality_checks;

        //load QC data into table
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
    paramDeleteFormatter: function (value, row) {
        //boostrap-table formatter for deleting row of params table
        //creates a link to delete param

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.paramDeleteTemplate.replace("\[parameter_id\]", value);
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
    adminEditFormatter: function (value, row) {
        //boostrap-table formatter for editing row of QC table
        //creates a link to launch edit QC form

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.adminEditTemplate.replace("\[admin_id\]", value);
        return link;
    },
    adminDeleteFormatter: function (value, row) {
        //boostrap-table formatter for deleting row of QC table
        //creates a link to delete QC

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.adminDeleteTemplate.replace("\[admin_id\]", value);
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
            $("#sensorParametersTable").bootstrapTable({ data: sensorParametersData });

            //display sensor modal
            $("#sensorModal").modal("show");
        });
    },
    addSensorParameter: function () {
        //add a sensor parameter to the sensor parameters table

        var me = ingest;
        var g = me.globals;

        var data = {};
        data.sensor_id = $("#sensorUid").val();
        data.parameter_id = $("#sensorParameter").val();
        data.parameter_name = $("#sensorParameter :selected").text();
        data.unit_id = $("#sensorUnit").val();
        data.unit_name = $("#sensorUnit :selected").text();
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
        //save sensor data to database

        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //check form validity
        $("#sensorValidityWarning").hide();
        if ($("#frmSensor")[0].checkValidity()) {

            //get sensor data from form
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
            data.data_format = 0;
            data.timestamp_column_id = $("#sensorTimestampColumn").val();
            data.qc_rules_apply = $("#sensorApplyQc").prop("checked");
            data.active = true;
            data.parameters = $("#sensorParametersTable").bootstrapTable("getData");

            //determine parameters to be deleted
            var deleteParams = [];
            $.each($("input[name='grpDeleteParams']:checked"), function () {
                deleteParams.push($(this).val());
            });

            if (uid != "") {
                //UID exists so call sensor update service

                //remove existing parameters from parameters list
                var newParams = [];
                $.each(data.parameters, function () {
                    var currentParam = this;

                    //remove unnecessary fields
                    delete currentParam.parameter_name;
                    delete currentParam.unit_name;
                    var addToDeleteList = false;
                    if (currentParam.sensor_parameter_id) {
                        delete currentParam.sensor_parameter_id;
                        //if existing parameter, also need to add it to delete list so parameters are updated successfully (*service could be improved here*)
                        addToDeleteList = true;
                    }
                    
                    //only add parameter to new parameters list if not marked for deletion
                    if (deleteParams.find(function (paramId) { return paramId == currentParam.parameter_id }) == null) {
                        newParams.push(this);
                        if (addToDeleteList) {
                            deleteParams.push(this.parameter_id);
                        }
                    }
                });
                data.parameters = newParams;
                //delete parameters if parameters were marked for deletion
                if (deleteParams.length > 0) {
                    $.each(deleteParams, function (index) {
                        var deleteParam = this;
                        helper.callService(s.sensors + uid + /parameters/ + deleteParam, "{}", "DELETE", function () {
                            //if this is was the last parameter for deletion then continue with updating sensor
                            if (index == deleteParams.length - 1) {
                                helper.callService(s.sensors + uid, data, "PUT", function (data) {
                                    //alert user, hide modal, refresh sensors table data
                                    alert(g.text.sensorSaved);
                                    $("#sensorModal").modal("hide");
                                    me.callSensorsService();
                                });
                            }
                        });
                    });
                }
                else {
                    //otherwise just update sensor
                    helper.callService(s.sensors + uid, data, "PUT", function (data) {
                        //alert user, hide modal, refresh sensors table data
                        alert(g.text.sensorSaved);
                        $("#sensorModal").modal("hide");
                        me.callSensorsService();
                    });
                }
            }
            else {
                //new sensor

                data.parameters = [];

                //call sensor create service
                helper.callService(s.sensors, data, "POST", function (data) {

                    //add sensor ID to parameters data after saving sensor, then resave with parameters (*service could be improved here*)
                    $("#sensorUid").val(data.sensor_id);
                    data.parameters = $("#sensorParametersTable").bootstrapTable("getData");
                    var newParams = [];
                    $.each(data.parameters, function (index) {
                        var currentParam = this;
                        //only add parameter to new parameters list if not marked for deletion
                        if (deleteParams.find(function (paramId) { return paramId == currentParam.parameter_id }) == null) {
                            currentParam.sensor_id = data.sensor_id;
                            newParams.push(currentParam)
                        }
                    });
                    data.parameters = newParams;
                    $("#sensorParametersTable").bootstrapTable("load", data.parameters);
                    me.saveSensor();

                });
            }
        }
        else {
            $("#sensorValidityWarning").show();
        }
    },
    deleteSensor: function (uid) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        if (confirm(g.text.confirm)) {
            //call sensor delete service
            helper.callService(s.sensors + uid, "", "DELETE", function (data) {
                //alert user, hide modal, refresh sensors table data
                alert(g.text.sensorDeleted);
                $("#sensorModal").modal("hide");
                me.callSensorsService();
            });
        }
    },
    showEditQcModal: function (uid) {
        //display QC modal with data from table

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
        //save QC data to database

        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //get QC data from form
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

        //*this is a workaround - ideally QC should be handled through separate services*
        if (uid != "") {
            //UID exists so

            //find the table row index and update data in the QC table
            var index = $.map($("#qcTable").bootstrapTable("getData"), function (record, index) {
                if (record.org_parameter_quality_check_id == uid) {
                    return index;
                }
            });
            $("#qcTable").bootstrapTable("updateRow", { index: index, row: data });
            
        }
        else {
            //new QC

            //create a temp UID so new row can be added to QC table
            data.org_parameter_quality_check_id = Date.now();
            $("#qcTable").bootstrapTable("append", [data]);
        }
        //get data from table, remove extraneous fields
        var qcData = $("#qcTable").bootstrapTable("getData");
        $.each(qcData, function (index, record) {
            delete record.org_parameter_quality_check_id;
            delete record.parameter_name;
            delete record.quality_check_operand_name;
            delete record.quality_check_action_name;
            record.organization_id = g.variables.orgId;
        });

        //first call org service to retrieve org data
        me.callOrgService(function (data) {
            //add updated QC data to org data
            data.quality_checks = qcData;
            //call org update service to update org data with new QC data (not pretty!)
            helper.callService(s.orgs + g.variables.orgId, data, "PUT", function (data) {
                //alert user, hide modal, refresh QC table data
                alert(g.text.qcSaved);
                $("#qcModal").modal("hide");
                me.callOrgService(me.loadQcTable(data));
            });
        });
        //*end workaround*
    },
    deleteQc: function (uid) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;

        if (confirm(g.text.confirm)) {

            //*this is a workaround - ideally QC should be handled through separate services*
            //update QC table data to remove QC record and extraneous fields
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
            //first call org service to retrieve org data
            me.callOrgService(function (data) {
                data.quality_checks = newQcData;
                //then call org update service to update QC data without the deleted record (ugly!)
                helper.callService(s.orgs + g.variables.orgId, data, "PUT", function (data) {
                    //alert user, hide modal, refresh QC table data
                    alert(g.text.qcDeleted);
                    $("#qcModal").modal("hide");
                    me.callOrgService(me.loadQcTable(data));
                });
            });
            //*end workaround*
        }
    },
    showEditAdminModal: function (uid) {
        //Display Admin Model on Edit
        var adminData = $("#adminTable").bootstrapTable("getData");
        var rowData = $.grep(adminData, function (record, index) {
            return record.id == uid;
        });
        $("#adminUid").val(uid);
        //console.log(rowData);
        $("#adminUsername").val(rowData[0].username);
        $("#adminEmail").val(rowData[0].email);
        $("#adminRole").val(rowData[0].role);
        $("#adminModal").modal("show");
    },
    resetAdminModal: function () {
        //reset QC form
        $("#adminUid").val("");
        $("#adminUsername").val("");
        $("#adminRole").val("");
        $("#adminEmail").val("");
    },
    saveAdmin: function () {

        var me = ingest;
        var g = me.globals;
        var s = g.services;
        //get QC data from form
        var uid = $("#adminUid").val();

        var data = {};
        data.id = uid;
        data.username = $("#adminUsername").val();
        data.roles = [$("#adminRole option:selected").val()];
        data.email = $("#adminEmail").val();

        //update
        if (uid) {

            helper.callService(s.user+uid, data, g.variables.token,"post", function (data) {
                //alert user, hide modal, refresh QC table data
                alert(g.text.adminSaved);
                $("#adminModal").modal("hide");
                me.callUserService();
            });
        }else{
            //insert
            //data
            helper.callService(s.user, data, g.variables.token,"post", function (data) {
                //alert user, hide modal, refresh admin table data
                alert(g.text.adminSaved);
                $("#adminModal").modal("hide");
                me.callUserService();
            });
        }
    },
    deleteAdmin: function (uid) {
        var me = ingest;
        var g = me.globals;
        var s = g.services;
        if (confirm(g.text.confirm)) {

            helper.callService(s.user+uid, "", g.variables.token,"delete", function (data) {
                alert(g.text.adminDeleted);
                $("#adminModal").modal("hide");
                me.callUserService();
            });
        }
    },
};

$("document").ready(function () {
    //runs when page loads

    ingest.init();
});
