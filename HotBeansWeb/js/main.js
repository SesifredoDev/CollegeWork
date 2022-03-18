var navBar = document.getElementById("nav");
window.onscroll = function(e){
    if (window.scrollY > 200){
        navBar.style.background = 'linear-gradient(90deg, rgba(54,36,255,1) 0%, rgba(10,4,84,1) 50%, rgba(143,0,255,1) 100%)';

    }else{
        navBar.style.background = 'rgb(68, 68, 68)';
    };;
}
function scrollToElement(id){
    document.getElementById(id).scrollIntoView()
}