function submit(){
    nameInput = document.getElementById("name").value;
    phoneInput = document.getElementById("phone").value;
    alert("You entered " + nameInput + " and your number is " + phoneInput);
    const d = new Date()
    console.log(d)
    document.getElementById("enteredName").innerText = nameInput
    document.getElementById("currentDate").innerText = d.toLocaleDateString('en-GB')
}



