$(document).ready(function(){
      $(".plus").click(function(){
        red_val = parseInt($(this).next().html())+1;
        $(this).next().html(red_val);
        });
});

$(document).ready(function(){
      $(".minus").click(function(){
        red_val = parseInt($(this).prev().html())-1;
        $(this).prev().html(red_val);
        });
});

$(document).ready(function(){
$(.btn btn-primary save_changes).click(function(){
    $.ajax({
        url : "/activity/eat_rainbow_update"
        method : "POST"
        data : {"date": $("#eat_date").val(),
                "user_id":$(""),
                "red_serving" : parseInt($("#green_serving").html()),
                "cream_serving": parseInt($("#cream_serving").html()),
                "yellow_serving": parseInt($("#yellow_serving").html()),
                "kiwi_serving": parseInt($("#kiwi_serving").html()),
                "blue_serving": parseInt($("#blue_serving").html()),
                "green_serving":parseInt($("#green_serving").html()),
                };
        success : function(data){
            alert(data);
        },

        });

    });



});