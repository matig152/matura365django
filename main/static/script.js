function mobilemenu(){
    const sideNav = document.querySelectorAll('.sidenav')[0];
    if(sideNav.offsetWidth > 0){hideSideNav();}
    else{showSideNav();}
}


async function showSideNav(){
    const sideNav = document.querySelectorAll('.sidenav')[0];
    const mask = document.querySelectorAll('.mask')[0];
    sideNav.style.width = '220px';
    //sideNav.style.padding = '10px';
    mask.style.display = 'block';
    await new Promise(r => setTimeout(r, 1));
    mask.style.opacity = 1;
}

async function hideSideNav(){
    const sideNav = document.querySelectorAll('.sidenav')[0];
    const mask = document.querySelectorAll('.mask')[0];
    sideNav.style.width = '0';
    //sideNav.style.padding = '0';
    mask.style.opacity = 0;
    await new Promise(r => setTimeout(r, 500));
    mask.style.display = 'none';
}

async function Odpowiedz(){
    przyciskodpowiedz = document.getElementById("przyciskodpowiedz")
    odpowiedz = document.getElementById("odpowiedz")
    if(przyciskodpowiedz.innerHTML == "POKAŻ ODPOWIEDZI"){
        odpowiedz.style.display = "block"
        await new Promise(r => setTimeout(r, 1));
        odpowiedz.style.opacity = "1"
        przyciskodpowiedz.innerHTML = "UKRYJ ODPOWIEDZI"
    }
    else{
        odpowiedz.style.opacity = "0"
        await new Promise(r => setTimeout(r, 400));
        odpowiedz.style.display = "none"
        przyciskodpowiedz.innerHTML = "POKAŻ ODPOWIEDZI"
    }
    
}

