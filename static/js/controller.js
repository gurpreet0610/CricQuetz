window.addEventListener("load",()=>{
    document.querySelector('#select_homeTeam').addEventListener("change",getHomeTeam);
    document.querySelector('#select_outsideTeam').addEventListener("change",getOutsideTeam);
    document.querySelector("#submitNames").addEventListener("click",submitTeamNames);
    document.querySelector("#submitBattingOrder").addEventListener("click",getCaptain);
    document.querySelector("#FinalSubmission").addEventListener("click",getFinalResponse)
     
})
var errorMsg;
function getHomeTeam(){
    var homeTeam =  document.querySelector('#select_homeTeam').value;
    
    return homeTeam;
}
function getOutsideTeam(){
    var outsideTeam =  document.querySelector('#select_outsideTeam').value;
    
    return outsideTeam;
}
function submitTeamNames(){
    var HT = getHomeTeam();
    var OT = getOutsideTeam();
    var team1 = document.querySelector(".team1");
    var team2 =  document.querySelector(".team2");
    team1.innerHTML = " ";
    team2.innerHTML = " ";
    
    if(HT == OT){
        
        var errorMsg = document.querySelector("#showError");
        errorMsg.innerHTML = "Choose Another Outside Team";
    }
    else{
        postData(HT,OT);
    }
}
function postData(HT,OT){
    var TeamName = {
        't1':HT,
        't2': OT,
   };
   var Toss = [HT,OT];
   Toss.forEach(function(member,index){
       var tossWinTeam = document.querySelector(".TossWinningTeam");
       var option = document.createElement("option");
       option.innerHTML = member;
       option.setAttribute("value", member);
       tossWinTeam.appendChild(option);

   })
    var formBody = [];
    for (var property in TeamName) {
      var encodedKey = encodeURIComponent(property);
      var encodedValue = encodeURIComponent(TeamName[property]);
      formBody.push(encodedKey + "=" + encodedValue);
    }
    formBody = formBody.join("&");
    
    
    fetch('https://cricquetz.herokuapp.com/players', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
      },
      body: formBody
    }).then(resp=>resp.json()).then(data=>print(data))
    
}
var source;
function print(data){
   
    data.team_1.forEach(function(member,index){
        
        var team1 = document.querySelector(".team1");
        var li = document.createElement("li");
        li.innerHTML = member;
        team1.appendChild(li);
        dragDrop(li);
        
        
    })
    
    data.team_2.forEach(function(member,index){
        
        var team2 = document.querySelector(".team2");
        var li = document.createElement("li");
        li.innerHTML = member;
        team2.appendChild(li);
        dragDrop(li)
        
    })
}
function dragDrop(li){
    li.setAttribute("draggable","true")
        li.addEventListener("dragstart",function(event){
           source = event.target;
           event.dataTransfer.setData("text/plain", event.target.innerHTML);
           event.dataTransfer.effectAllowed = "move";
    },false);
    li.addEventListener("dragover",function(event){
        event.preventDefault();
        event.dataTransfer.dropEffect ="move";
    },false);
    li.addEventListener("drop",function(event){
        event.preventDefault();
        event.stopPropagation();
        source.innerHTML = event.target.innerHTML;
        event.target.innerHTML = event.dataTransfer.getData("text/plain");
    })
}
 function  getCaptain(){
     var team1 = document.querySelector(".team1");
     var team1li = team1.getElementsByTagName("li");
     var team2 = document.querySelector(".team2");
     var team2li = team2.getElementsByTagName("li");
    
     for(var i = 0;i<team1li.length;i++){
         if(i<=10){
            
            var captain1 = document.querySelector(".captain1");
            var li = document.createElement("li");
            li.innerHTML = team1li[i].innerText;
            captain1.appendChild(li);
            var id = i;
            li.appendChild(createIcon(id,"https://melbournechapter.net/images/checkmark-transparent-box-3.png",toggleMarkUnmark))
            
         }
         else{
             break;
         }
     }
     for(var i = 0;i<team2li.length;i++){
        if(i<=10){
           
           var captain2 = document.querySelector(".captain2");
           var li = document.createElement("li");
           li.innerHTML = team2li[i].innerText;
           captain2.appendChild(li);
           var id = i;
           li.appendChild(createIcon(id,"https://melbournechapter.net/images/checkmark-transparent-box-3.png",toggleMarkUnmark))
           
           
        }
        else{
            break;
        }
    }
       
 }

function createIcon(id,path,fn){
    var img = document.createElement("img");
    img.src = path;
    img.className = "icon";
    img.setAttribute("item-id", id);
    
    img.addEventListener("click",fn);
    return img; 
}
function toggleMarkUnmark(event){
    var img = event.srcElement;
    
    var id = img.getAttribute("item-id");
    
    
    
    var li = img.parentNode;
    li.classList.toggle("red");
    
    

}


function getFinalResponse(){
    var homeTeam = getHomeTeam();
    var outsideTeam = getOutsideTeam();
    var team1 = document.querySelector(".team1");
    var team1li = team1.getElementsByTagName("li");
    var team1members = [];
    var team2 = document.querySelector(".team2");
    var team2li = team2.getElementsByTagName("li");
    var team2members = [];
    var tossTeam = document.querySelector("#tossTeam").value;
    console.log(tossTeam);
    var decision = document.querySelector("#decision").value;
    console.log(decision);
    
    for(let i = 0;i<=team1li.length;i++){
        if(i<=10){
            team1members.push(team1li[i].innerText);
            
        }
        else{
            break;
        }
    }
    for(let i = 0;i<=team2li.length;i++){
        if(i<=10){
            team2members.push(team2li[i].innerText);
            
        }
        else{
            break;
        }
    }
    var captain1 =  document.querySelector(".captain1")
    var captain1name = captain1.getElementsByTagName("li");
    var captainNameTeam1 = "";
    for(let i = 0; i<= captain1name.length;i++){
        if(captain1name[i].classList.contains('red')){
            captainNameTeam1 = captain1name[i].innerText;
            
            break;
        }
        
    }
    var captain2 =  document.querySelector(".captain2")
    var captain2name = captain2.getElementsByTagName("li");
    var captainNameTeam2 = "";
    for(let i = 0; i<= captain2name.length;i++){
        if(captain2name[i].classList.contains('red')){
            captainNameTeam2 = captain2name[i].innerText;
            
            break;
        }
        
    }
    postDetails(homeTeam,outsideTeam,team1members,team2members,captainNameTeam1,captainNameTeam2,tossTeam,decision);
   

}
function postDetails(homeTeam,outsideTeam,team1members,team2members,captainNameTeam1,captainNameTeam2,tossTeam,decision){
    var TeamDetails = {
        
        'team':[{
            'name':homeTeam,
            'member':team1members,
            'captainName':captainNameTeam1,
            

        },{
            'name':outsideTeam,
            'member':team2members,
            'captainName':captainNameTeam2

        },
        {
        'toss':tossTeam
        },
        {
        'inning':decision
        }]
   };
   
    
    fetch('https://cricquetz.herokuapp.com/result', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(TeamDetails)
    }).then(resp=>resp.json()).then(data=>success(data));
    
}
function success(data){
    var showDiv =  document.querySelector("#successMessage")
    showDiv.classList.add("show");
    var msg = document.querySelector(".successmsg");
    msg.innerHTML = data.winner;
    $("#main").append('<div>' + data.teams_chart + '</div><div>' + data.bats_chart + '</div><div>' + data.bowls_chart + '</div>');

}