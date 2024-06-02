const title= document.querySelector(".title");
const main_div=document.querySelector(".main-div");
const old_div = document.querySelector(".old-div");
//const lilist =document.querySelectorAll("ul.list > li")
const img = document.querySelector("img")
const btn= document.querySelector("button")
const list =document.querySelector(".list")

img.setAttribute("src", "e.png")
img.classList.add("img")
title.style.background="red"
document.body.removeChild(old_div)
let newDiv= document.createElement("div");
newDiv.innerText = "Ahora las putas me bailan"
document.body.appendChild(newDiv)
newDiv.style.background="yellow"
btn.addEventListener("click", function(){
    //alert("Holaa")
    //newDiv.style.background="black"
    //newDiv.innerText="Click"
    btn.style.background="white"
    btn.style.color="black"
})


const input= document.querySelector(".input")
const addButton= document.querySelector(".addButton")
const newList= document.querySelector(".newList")

addButton.addEventListener("click", function(){
    if(input.value.trim()!==""){
        let newItem = document.createElement("li");
        newItem.innerText=input.value;
        newList.appendChild(newItem)
        input.value=""
    }


}) 


const filter = document.querySelector(".filter")
filter.addEventListener("keyup", function(){
    const search = filter.value.toLowerCase();
    const items= list.getElementsByTagName("li")
    Array.from(items).forEach(function(item){
        if(item.textContent.toLowerCase().indexOf(search)!== -1){
            item.style.display="block"
        }else{
            item.style.display="none"
        }
    })
})

console.log(list)