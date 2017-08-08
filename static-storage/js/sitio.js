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