
function call(){
    arr = [];
    arr_ID = [];
    my_Arr = [];
    arr_Data=[];
    i = 0;
    counts = 0;
    text = "";

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

                          

                            col1 = document.createElement("td")
                            col2 = document.createElement("td");
                            col3 = document.createElement("td");
                            col4 = document.createElement("td");
                            col5 = document.createElement("td");
                        
                            col2.width = 200 + "px";
                            col3.width = 200 + "px";
                            col4.width = 200 + "px";
                            
                            eddy = document.createElement("input");
                            eddy.type = "Button";

                            email = document.createTextNode(my_Arr[0]);
                            password = document.createTextNode( my_Arr[1]);
                            Company = document.createTextNode(my_Arr[2]);
                            eddy.id = arr_ID[i];
                            eddy.value = "EDIT"
                            eddy.addEventListener('click', function(){
                                col6 = document.createElement("td");
                                reddy = document.createTextNode(eddy.id);

                                col6.appendChild(reddy);
                                tabs = document.getElementsByTagName('table');
                                
                                for(var m = 0; m < tabs.length; m++){
                                    
                                    tr = tabs[m].getElementsByTagName('tr');
                                        for(var r = 1; r < tr.length; r++){
                                            td = tr[r].getElementsByTagName('td');
                                            temp = td[0].innerHTML;
                                            if(temp == eddy.id){
                                                
                                                for(var k = 0; k < td.length; k++){
                                                    $.ajax({
                                                        url:'/edit',
                                                        type:'POST',
                                                        contentType: "application/json",
                                                        data:JSON.stringify(td[k].innerHTML)
                                                    });
                                                }
                                            }
                                            
                                        
                                        }  
                                    
                                        
                                    
                                    
                                   
                                }
                                
                            });

                            col5.appendChild(document.createTextNode(arr_ID[i]));
                            col2.appendChild(email);
                            col3.appendChild(password);
                            col4.appendChild(Company);
                            col1.appendChild(eddy);

                            row.appendChild(col5);
                            row.appendChild(col2);
                            row.appendChild(col3);
                            row.appendChild(col4);
                            row.appendChild(col1);
                            
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
    val = [];
    iCount = -1;
    for( i of tab.rows){
        iCount ++;
        for( j of i.cells){
            val[iCount] = val[iCount]+j.innerHTML+"|";
        }  
       
    }
    alert(val[iCount]);
    
    
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
