let id = "";

function call2(){
    arr_data = [];
    let email = document.getElementById("email");
    let password = document.getElementById("password");
    let company = document.getElementById("company");

    $.ajax({
        url: '/edit',
        type: 'GET',
        contentType: "application/json",
        success: function(data){
            newdat = data;
            arr_data = newdat.split('|');
            id = arr_data[0];
            email.value = arr_data[1];
            password.value = arr_data[2];
            company.value = arr_data[3];    
        }
    });
}

function save(){
    line = id + "~" + email.value + "|" + password.value + "|" + company.value;
    $.ajax({
        url: '/save',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(line)
    });
    $.ajax({
        url: '/save',
        type: 'GET',
        contentType: "application/json",
        success:function(data){
            newdats = data;
            if(newdats == "True"){
                alert("Your changes have been saved");
                window.location.href = '/menu';
            }
        }
    });
}

function menu (){
    window.location.href = '/menu';
    
}