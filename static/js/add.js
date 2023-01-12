function add(){
    let username = document.getElementById("Susername");
    let password = document.getElementById("Spassword");
    let company = document.getElementById("Scompany");
    
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

function menu(){
    window.location.href = '/menu';
}