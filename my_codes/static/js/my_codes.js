
const buttonsDelete = document.querySelectorAll(".button-delete");
for (let count = 0; count < buttonsDelete.length; count++) {
    let buttonDelete = buttonsDelete[count];
    buttonDelete.addEventListener("click", function (event) {
        document.cookie = `qrcode=${buttonDelete.id}`;
    });
}

const buttonsName = document.querySelectorAll(".qr-code-title");
for (let count = 0; count < buttonsName.length; count++) {
    let buttonName = buttonsName[count];
    buttonName.addEventListener("click", function (event) {
        document.cookie = `specificQrcodeID=${buttonName.id}`;
    });
}

const bgButton = document.querySelector(".bg");
const formButton = document.querySelector(".form-qr");

bgButton.addEventListener("click",
    function(event){
        bgButton.classList.toggle("close");
        formButton.classList.toggle("close");
    }
)

const closeButton = document.querySelector(".close-button");

closeButton.addEventListener(
    "click", 
    function(event){
        bgButton.classList.toggle("close");
        formButton.classList.toggle("close");
    }
)