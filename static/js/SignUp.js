
function signup(){ 
    var username = document.getElementById("username");
    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var password2 = document.getElementById("password2");
    var bool = false;
    if(password.value == password2.value)
        bool = true;

    if (bool != true)
        alert("The passwords do not match pls try again")
    else{
        dat = username.value+"|"+email.value+"|"+password.value;
        $.ajax({
            url: '\signup',
            type: 'POST',
            contentType:"application/json",
            data:JSON.stringify(dat)
            
        });
        window.location.replace("/Login");
        
    }
}

function login(){
    window.location.replace("/Login");
}

