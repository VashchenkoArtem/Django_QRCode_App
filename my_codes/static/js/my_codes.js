const buttonsDelete = document.querySelectorAll(".button-delete");
for (let count = 0; count < buttonsDelete.length; count ++){
    let buttonDelete = buttonsDelete[count];
    buttonDelete.addEventListener(
        type = "click", 
        listener = function (event){
            document.cookie = `qrcode=${buttonDelete.id}`;
        }
    )
}
