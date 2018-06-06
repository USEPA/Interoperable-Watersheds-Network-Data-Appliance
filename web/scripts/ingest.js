var ingest = {
    globals: {
        templates: {
            yesTemplate: "<i class='fas fa-check'></i>",
            noTemplate: "<i class='fas fa-times'></i>",
            successTemplate: "<i class='fas fa-arrow-circle-up text-success'></i>",
            unknownTemplate: "<i class='fas fa-exclamation-triangle text-warning'></i>",
            failureTemplate: "<i class='fas fa-arrow-circle-down text-danger'></i>",
            sensorIdLinkTemplate: "<a href='javascript:void(0)' onclick='ingest.editSensor([sensor_id]);'>[sensor_id]</a>"
        },
        services: {
            sensors: "http://havasu.rtp.rti.org:8000/sensors/"
        }
    },
    init: function () {
        //initialize page values and settings

        var me = ingest;
        var g = me.globals;
        var s = g.services;

        //call sensors service and populate sensors table
        helper.callService(s.sensors, "{}", "GET", function (data) {
            $("#tblSensors").bootstrapTable({ data: data });
        });

        //reset sensors form when form is hidden
        $("#sensorModal").on("hidden.bs.modal", function () {
            ingest.resetSensorModal();
        });
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
        //converts date to en-US locale date/time string

        var formattedDate = " ";
        if (value != null) {
            var rawDate = new Date(value);
            formattedDate = rawDate.toLocaleDateString("en-US") + " " + rawDate.toLocaleTimeString("en-US");
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
        //*** retrieve sensor data from service here ***
    },
    resetSensorModal: function () {
        //reset sensor form

        $("#sensorId").val("");
        $("#sensorId").prop("disabled", false);
    }
};

$("document").ready(function () {
    //runs when page loads

    ingest.init();
});