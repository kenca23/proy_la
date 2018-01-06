/*---------------------
Inicio WOW
---------------------*/
new WOW().init();

/*---------------------
Inicio Smooth Scroll
---------------------*/
smoothScroll.init({
    speed: 1000, // Integer. How fast to complete the scroll in milliseconds
    offset: 100, // Integer. How far to offset the scrolling anchor location in pixels
});
/*---------------------------------
    OCULTAR Y MOSTRAR BOTON IR ARRIBA
 ----------------------------------*/

$(window).ready(function () {
    var resolucion = $(document).width();
    if (resolucion <= 992) {
        var src = $('#logo_menu').attr("src").match(/[^(2\.|\.)]+/) + "2.svg";
        $('#logo_menu').attr("src", src);
    } else {
        var src = $('#logo_menu').attr("src").replace("2.svg", ".svg");
        $('#logo_menu').attr("src", src);
    }
});

$(function () {
    $(window).resize(function () {
        var resolucion = $(document).width();
        if (resolucion <= 992) {
            var src = $('#logo_menu').attr("src").match(/[^(2\.|\.)]+/) + "2.svg";
            $('#logo_menu').attr("src", src);
        } else {
            var src = $('#logo_menu').attr("src").replace("2.svg", ".svg");
            $('#logo_menu').attr("src", src);
        }
    });
});

/*$(function () {
    $(window).scroll(function () {
        var scrolltop = $(this).scrollTop();

    });

});*/

/*---------------------------------
   CABECERA ANIMADA
 ----------------------------------*/
/*$(window).scroll(function () {

    var nav = $('.encabezado');
    var scroll = $(window).scrollTop();
    var resolucion = $(document).width();


    if (scroll >= 50) {
        $("#arriba").fadeIn('slow');
    } else {
        $("#arriba").fadeOut('slow');
    }

    if (scroll >= 100 && resolucion > 992) {

        //nav.addClass("fondo-menu");
        var src = $('#logo_menu').attr("src").match(/[^(2\.|\.)]+/) + "2.svg";
        $('#logo_menu').attr("src", src);

    } else if (scroll < 100 && resolucion > 992) {
        //nav.removeClass("fondo-menu");
        var src = $('#logo_menu').attr("src").replace("2.svg", ".svg");
        $('#logo_menu').attr("src", src);
    }
});
*/

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    
window.fbAsyncInit = function() {
        FB.init({
          appId      : '414955855568221',
          xfbml      : true,
          version    : 'v2.10'
        });
        FB.AppEvents.logPageView();
      };
    
      (function(d, s, id){
         var js, fjs = d.getElementsByTagName(s)[0];
         if (d.getElementById(id)) {return;}
         js = d.createElement(s); js.id = id;
         js.src = "//connect.facebook.net/en_US/sdk.js";
         fjs.parentNode.insertBefore(js, fjs);
       }(document, 'script', 'facebook-jssdk'));
       
       
       
     var c = $(".popup");
     c.on("click",function(a){
         a.preventDefault();
         var c=575,d=400,e=($(window).width()-c)/2,f=($(window).height()-d)/2,g="status=1"+",width="+c+",height="+d+",top="+f+",left="+e;
         window.open(this.href,"compartir",g)
         
     });