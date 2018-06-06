var ingest = {
    globals: {
        templates: {
            yesTemplate: "<i class='fas fa-check'></i>",
            noTemplate: "<i class='fas fa-times'></i>",
            successTemplate: "<i class='fas fa-arrow-circle-up text-success'></i>",
            unknownTemplate: "<i class='fas fa-exclamation-triangle text-warning'></i>",
            failureTemplate: "<i class='fas fa-arrow-circle-down text-danger'></i>",
            sensorIdLinkTemplate: "<a href='javascript:void(0)' onclick='ingest.showSensorModal([sensor_id]);'>[sensor_id]</a>"
        }
    },
    init: function() {
        helper.callService("http://havasu.rtp.rti.org:8000/sensors/", "{}", function (data) {
            //ingest.populateSensorsTable(data);
            $("#tblSensors").bootstrapTable({ data: data });
        });
        $("#sensorModal").on("hidden.bs.modal", function () {
            ingest.resetSensorModal();
        });
    },
    populateSelect: function (selectId) {
        var ddl = $("#" + selectId);
        ddl.append($("<option />").val("").text(""));
        $.each(result.d, function () {
            ddl.append($("<option />").val(this.ProjectEmsId).text(this.ProjectName));
        });
    },
    sensorIdFormatter: function(value) {
        var me = ingest;
        var g = me.globals;
        var t = g.templates;

        var link = t.sensorIdLinkTemplate.replace(/\[sensor_id\]/g, value);
        return link;
    },
    dateFormatter: function(value) {
        var formattedDate = " ";
        if (value != null) {
            var rawDate = new Date(value);
            formattedDate = rawDate.toLocaleDateString("en-US") + " " + rawDate.toLocaleTimeString("en-US");
        }
        return formattedDate;
    },
    qcRulesApplyFormatter: function (value) {
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
    showSensorModal: function (sensorId) {
        $("#sensorId").val(sensorId);
        $("#sensorId").prop("disabled", true);
        $("#sensorModal").modal("show");
        //retrieve sensor data here
    },
    resetSensorModal: function () {
        //reset sensor modal fields
        $("#sensorId").val("");
        $("#sensorId").prop("disabled", false);
    }
};

$("document").ready(function () {
    ingest.init();
});