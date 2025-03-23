const bgButton = document.querySelector(".form-qr");
if (bgButton != null){
    bgButton.addEventListener("click",
        function(){
            bgButton.classList.toggle("disabled");
        }
    )
}