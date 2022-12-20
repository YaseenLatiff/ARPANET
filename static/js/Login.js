function login(){
    var username = document.getElementById("username");
    var password = document.getElementById("password");   
    newdata = username.value + "|"+ password.value;    
    newdat = "";
    //sends the username and passoword values to the backend for confirmation
    $.ajax({
        url: '/login',
        type: 'POST',
        contentType:"application/json",
        data: JSON.stringify(newdata),
        success: function (data){
            //Waits to recieve true or false to determine whether the password and username was correct
            $.ajax({
                url: '/confirm',
                type: 'GET',
                contentType:"application/json",
                success: function (data){
                    newdat = data;
                    if(newdat == "True"){
                        window.location.replace("/menu");
                    }
                    else{
                        alert("Your password or username is incorrect")
                    }
                       
        
                }
            });
        }
    });
    
    


    
}

function register(){
    window.location.href = "/register";
}

