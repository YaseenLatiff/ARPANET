function call(){
    arr = [];
    i = 0;
    counts = 0;
    text = document.getElementById("area");
    
    
    $.ajax({
        url: '/count',
        type: 'GET',
        contentType:"application/json",
        success: function (data){
            newdat = data;
            counts = parseInt(newdat);
            for(count=0; count <= counts; count++){
                $.ajax({
                    url: '/call',
                    type: 'GET',
                    contentType:"application/json",
                    success: function (data){
                        newdat = data;
                        arr[i] = newdat;
                        text.value += arr[i]+"\n";
                        console.log(arr[i]);
                        i++;
        
                    }
                });
            }
        }
    });
    
    
}

function save(){
    i = 0;
    var arr = $('#area').val().split('\n');
    len = arr.length;
    line = "";
    for(count = 0; count <= len - 1; count++){
        if(line == "")
            line = arr[count];
        else
            line = line +"~"+ arr[count];

    }
    $.ajax({
        url: '/save',
        type: 'POST',
        contentType:"application/json",
        data: JSON.stringify(line)
    });
    
}

function logout(){
    window.location.replace("/");
}
