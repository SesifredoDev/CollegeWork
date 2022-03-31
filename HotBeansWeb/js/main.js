var navBar = document.getElementById("nav");
window.onscroll = function(e){
    if (window.scrollY > 200){
        navBar.style.background = 'linear-gradient(45deg, rgba(0,0,0,1) 0%, rgba(10,14,10,1) 48%, rgba(29,171,0,1) 100%)';

    }else{
        navBar.style.background = 'rgb(68, 68, 68)';
    };
}
function scrollToElement(id){
    document.getElementById(id).scrollIntoView();
};