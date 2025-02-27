const buttonFree = document.querySelector(".freeButton");
const buttonStandart = document.querySelector(".buttonStandart");
const buttonPro = document.querySelector(".proButton");
const buttonDesktop = document.querySelector(".h1Desktop");

buttonFree.addEventListener("click", function() {
  document.cookie = "subscribeType=free;path=/";
});
buttonStandart.addEventListener("click", function() {
    document.cookie = "subscribeType=standart;path=/";
});
buttonPro.addEventListener("click", function() {
    document.cookie = "subscribeType=pro;path=/";
});
buttonDesktop.addEventListener(
  "click",
  function(){
    console.log("sadasdsa")
    document.cookie = "subscribeType=desktop;path=/";
  }
);