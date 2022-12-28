function call2(){
    arr_data = [];
    
    for(var i = 0; i < 4; i++){
        $.ajax({
            url: '/ed',
            type: 'GET',
            contentType: "application/json",
            success: function(data){
                newdat = data;
                arr_data[i] = newdat;

            }
        });
    }
}