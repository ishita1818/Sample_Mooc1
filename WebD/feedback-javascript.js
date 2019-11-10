function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function isNumber(num){
    var regex= /^\d{10}$/;
    return regex.test(num);
}

function checkEmail(){
    var e = $('#email').val();
    if(!isEmail(e)){
        document.getElementById('email').value=" ";
        alert("Invalid Phone!!")
        
    }
}

function checkPhone(){
    var p = $('#phone').val();
    if(!isNumber(p)){
        document.getElementById('phone').value=" ";
        alert("Invalid Phone!!")
    }
}