$(document).ready(function(){
    $("button").click(function(){
     $.ajax({
        url: "/eat-activity-api/eat-rainbow-details",
        method: "POST",
        datatype: "json",
        data: { user_id, date : },
        success: {},
    });

    });
});

