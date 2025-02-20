const buttonFree = document.querySelector(".freeButton");
const buttonStandart = document.querySelector(".buttonStandart");
const buttonPro = document.querySelector(".proButton");

buttonFree.addEventListener("click", function() {
  document.cookie = "subscribeType=free;path=/";
});
buttonStandart.addEventListener("click", function() {
    document.cookie = "subscribeType=standart;path=/";
});
buttonPro.addEventListener("click", function() {
    document.cookie = "subscribeType=pro;path=/";
});