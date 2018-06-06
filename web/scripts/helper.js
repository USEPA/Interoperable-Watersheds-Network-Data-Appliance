var helper = {

    callService: function (url, data, successFunction) {

        //make ajax call
        var promise = $.ajax({
            type: "GET",
            url: url,
            data: data,
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        });

        //success
        promise.done(successFunction);

        //failure
        promise.fail(function (xhr, status, error) {
            console.log("xhr.status: " + xhr.status);
            console.log("xhr.readyState: " + xhr.readyState);
            console.log("xhr.responseText: " + xhr.responseText);
            console.log("xhr.responseXML: " + xhr.responseXML);
            console.log("status: " + status);
            console.log("error: " + error);
            console.log("url: " + url);
            console.log("data: " + data);
        });

    }
};