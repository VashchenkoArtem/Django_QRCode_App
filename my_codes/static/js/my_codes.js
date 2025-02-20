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

const buttonsCode = document.querySelectorAll(".qr-code-title");

for (let countCodes = 0; countCodes < buttonsCode.length; countCodes++) {
    let buttonCode = buttonsCode[countCodes];
    buttonCode.addEventListener(
        "click",
        function (event) {
            document.cookie = `specificQrcodeID=${buttonCode.id}`;
        }
    );
}
