function show()
{
        document.body.style.backgroundColor ="orange";
        alert('Form submitted !!')
}
//-------------//
let e1=document.getElementById("div1")
e1.style.color='red';
//-------------//
let items=document.getElementsByClassName("class1");
items[0].style.color='blue';
items[1].style.color='white'
//--------//
let elem=document.getElementsByTagName("p");
elem[1].style.color='white';
elem[1].style.fontFamily='arial';
elem[1].style.textAlign='center';