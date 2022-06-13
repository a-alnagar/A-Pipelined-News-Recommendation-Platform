

document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('form').onsubmit = function(){
        
        document.querySelector('submit').disabled = true;
        const task = document.querySelector('#task').value;
        const li = document.createElement('li');
        
        li.innerHTML= task;
        document.querySelector('#task').onkeyup = () =>{
            if(document.querySelector('#task').value > 0){
                document.querySelector('submit').disabled = false;
            }
            else{document.querySelector('submit').disabled = true;}
        }
        document.querySelector('#tasks').append(li);
        document.querySelector('#task').value = ''
        //Returning false prevents from sending the submitted info to the web
        //perform in the browser context
        return false
    }
});