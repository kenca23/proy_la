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


    $("#id_email").change(function () {
      var email = $(this).val();
      console.log( $(this).val() );
      
      $.ajax({
        url: '{% url "subscribers:validar_email" %}',
        data: {
          'email': email
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
              $("#id_email").val('');
              $.magnificPopup.open({
                  items: {
                    src: '<div id="small-dialog" class="zoom-anim-dialog"><h1>Usuario Existente</h1><p>' + data.error_message + '.</p></div>', // can be a HTML string, jQuery object, or CSS selector
                    type: 'inline',
                    fixedContentPos: false,
            		fixedBgPos: true,
            
            		overflowY: 'auto',
            
            		closeBtnInside: true,
            		preloader: false,
            		
            		midClick: true,
            		removalDelay: 300,
            		mainClass: 'my-mfp-slide-bottom'
                  }
                });
          }
        }
      });
      
    });
    
    $('#har_form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    function create_post() {
        console.log("create post is working!") // sanity check
        var formData = $("#har_form").serializeArray()
        
    $.ajax({
        url : "{% url 'subscribers:nuevo' %}", // the endpoint
        type : "POST", // http method
        
        data : formData,/*{ 
            name : $('#id_nombre').val(),
            email : $('#id_email').val(),
            pais : $('#id_pais').val(),
            ciudad : $('#id_ciudad').val(),
            'csrfmiddlewaretoken': csrftoken,
        },*/ // data sent with the post request
        // handle a successful response
        success : function(json) {
            $.magnificPopup.open({
                          items: {
                            src: '<div id="small-dialog" class="zoom-anim-dialog"><p>' + json.result + '.</p></div>', // can be a HTML string, jQuery object, or CSS selector
                            type: 'inline',
                            fixedContentPos: false,
                    		fixedBgPos: true,
                    
                    		overflowY: 'auto',
                    
                    		closeBtnInside: true,
                    		preloader: false,
                    		
                    		midClick: true,
                    		removalDelay: 300,
                    		mainClass: 'my-mfp-slide-bottom'
                          }
                        });
            
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $.magnificPopup.open({
                          items: {
                            src: '<div id="small-dialog" class="zoom-anim-dialog"><p>' + errmsg + '.</p></div>', // can be a HTML string, jQuery object, or CSS selector
                            type: 'inline',
                            fixedContentPos: false,
                    		fixedBgPos: true,
                    
                    		overflowY: 'auto',
                    
                    		closeBtnInside: true,
                    		preloader: false,
                    		
                    		midClick: true,
                    		removalDelay: 300,
                    		mainClass: 'my-mfp-slide-bottom'
                          }
                        });
        }
    });
    };
    
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
    
    
