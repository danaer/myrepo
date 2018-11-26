jQuery("document").ready(function(){
    jQuery("#like").on('click', function(){
            var href = document.getElementById('like').name;
            jQuery.ajax({
                type: "GET",
                url: "/games/videolike/ajax/",
                data:{ "addlike" : href,},
                dataType: "text",
                catch: false,
                success: function(data){
                    jQuery("#count_likes").html(data);
                }
            });
    });
});