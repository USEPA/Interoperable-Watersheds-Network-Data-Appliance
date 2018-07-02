var ingest = {
    globals: {
        templates: {
            yesTemplate: "<i class='fas fa-check'></i>",
            noTemplate: "<i class='fas fa-times'></i>",
            successTemplate: "<i class='fas fa-arrow-circle-up text-success'></i>",
            unknownTemplate: "<i class='fas fa-exclamation-triangle text-warning'></i>",
            failureTemplate: "<i class='fas fa-arrow-circle-down text-danger'></i>",
            sensorIdLinkTemplate: "<a href='javascript:void(0)' onclick='ingest.editSensor([sensor_id]);'>[sensor_id]</a>",
            parameterLinkTemplate: "<a href='javascript:void(0)' onclick='ingeset.editQc([qc_id]);'>[parameter_name]</a>"
        },
        services: {
            orgs: config.serviceUrl + "orgs/",
            sensors: config.serviceUrl + "sensors/"
        }
    },
    init: function () {
        //initialize page values and settings

        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //get query string parameters
        var params = helper.getQueryStringParams();
        var orgId = params["orgId"];

        if (orgId != null) {
            //call orgs service and populate organization table and QC table
            helper.callService(s.orgs + orgId, "", "GET", function (data) {
                $("#orgParentId").text(data.parent_organization_id);
                $("#orgName").text(data.name);
                $("#orgId").text(data.organization_id);
                $("#orgUrl").text(data.sos_url);
                $("#contactName").text(data.contact_name);
                $("#contactEmail").text(data.contact_email);
                $("#qcTable").bootstrapTable({ data: data.quality_checks });
            });

            //call sensors service and populate sensors table
            helper.callService(s.sensors, "", "GET", function (data) {
                $("#sensorsTable").bootstrapTable({ data: data });
            });



            //reset sensors form when form is hidden
            $("#sensorModal").on("hidden.bs.modal", function () {
                ingest.resetSensorModal();
            });

            //reset sensors form when form is hidden
            $("#qcModal").on("hidden.bs.modal", function () {
                ingest.resetQcModal();
            });
        }
        else {
            //redirect?
        }
    },
    populateSelect: function (selectId, data, nameField, idField) {
        //populates a select element with name and id from json object

        var ddl = $("#" + selectId);
        ddl.append($("<option />").val("").text(""));
        $.each(data, function () {
            ddl.append($("<option />").val(this[idField]).text(this[nameField]));
        });
    },
    sensorIdFormatter: function (value) {
        //bootstrap-table formatter for sensor id column of sensors table
        //makes sensor id a link to launch edit sensor form

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.sensorIdLinkTemplate.replace(/\[sensor_id\]/g, value);
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
    editSensor: function (sensorId) {
        //launch edit sensor form and populate with existing sensor data based on sensor id
        $("#sensorId").val(sensorId);
        $("#sensorId").prop("disabled", true);
        $("#sensorModal").modal("show");

        //call sensors service and populate form
        helper.callService(s.sensors + sensorId, "", "GET", function (data) {
            $("#sensorNameShort").val(data.short_name);
            $("#sensorNameLong").val(data.long_name);
            $("#sensorLatitude").val(data.latitude);
            $("#sensorLongitude").val(data.longitude);
            $("#sensorAltitude").val(data.altitude);
            $("#sensorLongitude").val(data.longitude);
            $("#sensorTimeZone").val(data.timezone);
            $("#sensorIngestFrequency").val(data.ingest_frequency);
            $("#sensorUrl").val(data.data_url);
            $("#sensorQuality").val(data.data_qualifier_id);
            $("#sensorResultTimeStamp").val(data.timestamp_column_id);
            $("#sensorResultTimeStamp").val(data.timestamp_column_id);
            $("#sensorApplyQc").prop("checked", data.qc_rules_apply);
            //$("#sensorParameter").val(data.parameters[0]); ???

        });
    },
    resetSensorModal: function () {
        //reset sensor form

        $("#sensorId").val("");
        $("#sensorId").prop("disabled", false);
        $("#sensorNameShort").val("");
        $("#sensorNameLong").val("");
        $("#sensorLatitude").val("");
        $("#sensorLongitude").val("");
        $("#sensorAltitude").val("");
        $("#sensorLongitude").val("");
    },
    parameterFormatter: function (value, row) {
        //boostrap-table formatter for parameter column of QC table
        //makes parameter a link to launch edit QC form

        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.parameterLinkTemplate.replace("\[parameter_name\]", value);
        link = link.replace("\[qc_id\]", row.org_parameter_quality_check_id);
        return link;
    },
    editQc: function(qcId) {

    },
    resetQcModal: function () {
        //reset QC form

        
    },
};

$("document").ready(function () {
    //runs when page loads

    ingest.init();
});
