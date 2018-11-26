jQuery("document").ready(function(){
    console.log("hello")
    jQuery(".likec").on('click', function(){

            var href = document.getElementById('likec').name;
            jQuery.ajax({
                type: "GET",
                url: "/games/commentlike/ajaxcom/",
                data:{ "addlikecom" : href,},
                dataType: "text",
                catch: false,
                success: function(data){
                    jQuery("#"+ id +"countcom").html(data);
                }
            });
    });
});