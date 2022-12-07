let listElements= document.querySelectorAll(".list__button--click");

listElements.forEach(listElements => {
    listElements.addEventListener("click",()=>{
        
        listElements.classList.toggle("arrow");

        let height = 0;
        let menu = listElements.nextElementSibling;
        if(menu.clientHeight == "0"){
            height=menu.scrollHeight;
        }
        menu.style.height= height+"px";
    })
    
});

function validar(){
    var nombre, contrasena, confirmacion;
    nombre= document.getElementById("nombre").value;
    contrasena= document.getElementById("contrasena").value;
    confirmacion=document.getElementById("confirmacion").value;

    if(nombre==="" || contrasena==="" || confirmacion===""){
        alert("Todos los campos son obligatorios");
        return false;
    }
    else if (confirmacion != contrasena){
        alert("Contraseñas diferentes");
        return false;
    }
    else if(nombre.lenght<4){
        alert("Nombre Muy corto");
        return false;
    }
    else if(contrasena.lenght<5){
        alert("Contraseña Muy corta")
        return false;
    }
}

function access(){
    var usuario, contrasena;
    usuario = document.getElementById("usuario").value;
    contrasena= document.getElementById("contrasena").value;

    if (usuario===""){
        alert("Ingrese un nombre de usuario Valido");
        return false;
    }
    else if (contrasena===""){
        alert("Ingrese una contraseña Valida");
        return false;
    }
}

$(document).ready(function(){

    var Api_Key = "AIzaSyATH4GR2XLYOvF4CWA8rDi03cqztCa3_js";

    var video =''

    $("form").submit(function (evt){
        evt.preventDefault()

        var search = $("search").val()

        videosearch(Api_Key, search, 10)
    })

    function videosearch(key,search,maxresults){
        $.get("https://www.googleapis.com/youtube/v3/search?key=" + key + "&type=video&part=snippet&maxresults=" + maxresults+ "&q=" + search,function(data){
            console.log(data)

            data.items.forEach(item => {
                video = '<iframe width="420" height="135" src="http://www.youtube.com/embed/${item.id.videoId}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

                $("#videos").append(video)
            });
        } )

    }
})