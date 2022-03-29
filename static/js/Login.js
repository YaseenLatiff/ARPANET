function login(){
    var username = document.getElementById("username");
    var password = document.getElementById("password");   
    newdata = username.value + "|"+ password.value;    
    newdat = "";
    
    alert(newdat)
    $.ajax({
        url: '/login',
        type: 'POST',
        contentType:"application/json",
        data: JSON.stringify(newdata),
        success: function (data){
            $.ajax({
                url: '/confirm',
                type: 'GET',
                contentType:"application/json",
                success: function (data){
                    newdat = data;
                    alert(newdat);
                    if(newdat == "True"){
                        window.location.href = "/menu";
                    }
                    else{
                        alert("Your password or username is incorrect")
                    }
                       
        
                }
            });
        }
    });
    
    


    
}

