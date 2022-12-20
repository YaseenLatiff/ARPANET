function add(){
    username = document.getElementById("username");
    password = document.getElementById("password");
    company = document.getElementById("company");
    if(!(username.value = "") && !(password.value = "") && !(company.value = "")){
        sdata = username.value+"|"+password.value+"|"+company.value;

        $.ajax({
            url: '/addd',
            type: 'POST',
            contentType:"application/json",
            data: JSON.stringify(sdata)
        });
        $.ajax({
            url:'/addd',
            type: 'GET',
            contentType: "application/json",
            success: function(data){
                if(data == "True"){
                    alert("Your passwords have been saved");
                    window.location.href = '/menu';
                }
                else{
                    alert("Error your passwords were not saved please check you network");
                }
            }
        });
    }
    else{
        alert("Please fill in all fields");
    }
    
    

}

function menu(){
    window.location.href = '/menu';
}