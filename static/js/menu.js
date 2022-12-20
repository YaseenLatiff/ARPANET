
function call(){
    arr = [];
    arr_ID = [];
    my_Arr = [];
    i = 0;
    counts = 0;
    $("#table tbody tr").remove();
    var x  =  document.getElementById("table").rows.length;
    let table = document.getElementById("table");
    
    //Gets the number of passwords stored in the database
    $.ajax({
        url: '/count',
        type: 'GET',
        contentType:"application/json",
        success: function (data){
            newdat = data;
            counts = parseInt(newdat);
            for(count=0; count <= counts; count++){//uses the number gained from the first ajax statement to loop a second ajax statement calling for 
                $.ajax({//a second ajax statement calling for all the passwords associated with the account
                    url: '/call',
                    type: 'GET',
                    contentType:"application/json",
                    success: function (data){
                        if(data != "False"){
                            newdat = data;
                            my_Arr = newdat.split("~");
    
                            arr[i] = my_Arr[0];
                            arr_ID[i] = my_Arr[1];
                            
                            my_Arr = [];
    
                            my_Arr = arr[i].split("|");
                            
    
                            tabody = document.getElementsByTagName("tbody").item(0);
                            row = document.createElement("tr");
                            row.id = x;
                            
                            col2 = document.createElement("td");
                            col3 = document.createElement("td");
                            col4 = document.createElement("td");
    
                        
                            col2.width = 200 + "px";
                            col3.width = 200 + "px";
                            col4.width = 200 + "px";
    
                            email = document.createElement("input");
                            email.value = my_Arr[0];
                            password = document.createElement("input");
                            password.value = my_Arr[1];
                            Company = document.createElement("input");
                            Company.value = my_Arr[2];
                            
    
                        
                            col2.appendChild(email);
                            col3.appendChild(password);
                            col4.appendChild(Company);
                           
                            row.appendChild(col2);
                            row.appendChild(col3);
                            row.appendChild(col4);
    
                            tabody.appendChild(row);
    
                            //displays the value in the textarea html component
                            i++;
            
                        }
                        
                    }
                });
            }
        }
    });
    
    
}

function save(){
   //retrieves the contents of a text area component using jquery
    line = "";
    tab = document.getElementById("table");
    for( i of tab.rows){
        for( j of i.cells.innerHTML.value){
            val = document.createElement("input");
            val = j.innerHTML;
            console.log(val);
        }
    }
    
    
    /**$.ajax({
        url: '/save',
        type: 'POST',
        contentType:"application/json",
        data: JSON.stringify(line)//sends the entire line of text to the python backend
    });
    $.ajax({
        url: '/save',
        type: 'GET',
        contentType:"application/json",
        success: function(data){
            if(data = "True"){
                alert("Your passwords have been saved");
            }
            else
                alert("Your passwords were not saved issue with connection to server please try again later.");
        }
    })
    alert("Your passwords have been saved");**/
    
}

function logout(){
    window.location.replace("http://127.0.0.1:5000/");//calls the index html page
}
function add(){
    window.location.href = "/adddat";
}
