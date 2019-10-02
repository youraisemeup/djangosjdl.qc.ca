$(window).load(function(){
    $(".cycle-slideshow").cycle();
    resizeBtnImage();
    resizeHomeColsHeight();
});

$(function(){
    $(".collapsableitem h3").on("click",function(){
        $(".collapsableitem").removeClass("opened").find(".collapse").hide();
        $(this).parent().toggleClass("opened");
        $(this).parent().find(".collapse").toggle();
    });

    $(".navbar.navbar-default").on("click",".navbar-toggle",function(){
        //$(".navbar.navbar-default").toggleClass("opened");
        $("header").toggleClass("opened");
        $("body").toggleClass("menuopened");
    });

    $("#reglementsMunicipaux h3").on("click",function(){
        lastPos = $(window).scrollTop();
        location.hash = $(this).attr("id");
        $(window).scrollTop(lastPos);
    });

    if($(window).width() > 768){
        $(window).scroll(function(){
            if($(window).scrollTop() >= 153){
                $("header").addClass("fixed");
            }else{
                $("header").removeClass("fixed");
            }
        });
    }else{

        $(".navbar-toggle").on("click",function(){
            //reset positions
            $(".mainmenu").css({left:0});
            $(".submenu").hide();
            $(".navbar-header>a").html("Accueil").removeClass("prev");
        });
        $(".navbar-default .mainmenu").on("click",'.navbar-nav>li.dropdown>a',function(e){
            e.preventDefault();

            var sm = $(this).parent().children(".submenu").show();
            $(".mainmenu").animate({left:-5000});
            $(".navbar-header>a").addClass("prev").html("Précédent");

            return false;
        });

        $(".navbar-default").on("click","a.prev",function(e){
            e.preventDefault();

            $(this).html("Accueil").removeClass("prev");

            $(".mainmenu").animate({left:0});
            $(".submenu").hide();


            return false;
        });

        $(".sidemenu .menutoggle").on("click",function(){
            $(".sidemenu").toggleClass("opened");
            $(".sidebar .shadow").toggleClass("opened");
        });
    }

    $(".mainmenu .navbar-nav>li").hover(function(e){
        $(".mainmenu").toggleClass("hover");
    });

    /* Searchform animation */
    $(".searchform #searchsubmit").on("click",function(){
        var form = $(this).parent();
        var inputtext = form.find("#q");
        if(inputtext.hasClass("opened") && inputtext.val() == ""){
            inputtext.attr("placeholder","");
            inputtext.removeClass("opened");
        }else{
            inputtext.addClass("opened");
            inputtext.attr("placeholder","Rechercher");
            if(inputtext.val() != ""){
                form.submit();
            }
        }
        return false;
    });

    //Open links in blank if begins with http:// or if it's a pdf
    $("a").not("#prev").not("#next").on("click",function(e){
        e.preventDefault();
        var href = $(this).attr("href");

        if($(this).parent().parent().hasClass("navbar-nav")){
            return;
        }

        if($(this).hasClass("prev")){
            return;
        }

        if(href.match(/(^https?:\/\/.*)/) || href.match(/\.pdf$/)){
            window.open(href);
        }else{
            window.location = href;
        }
    });

    /* .btnimage responsiveness */
    //resizeBtnImage();
    //resizeHomeColsHeight();
    $(window).resize(function(){
        resizeBtnImage();
        resizeHomeColsHeight();
    });

});

function resizeBtnImage(){
    $("body#home .btnimage").each(function(i,e){
        var element = $(this);
        var imgheight = element.find("img").height();
        element.height(imgheight/2);
        $("body#home .threeblocks .bulletin").innerHeight(imgheight/2);
    });
}

function resizeHomeColsHeight(){
    if($(window).width() >= 768){

        var maxHeight = 0;
        $("body#home .actualites .shadow").each(function(){
            if($(this).outerHeight() > maxHeight){
                maxHeight = $(this).outerHeight();
            }
        });

        if($(window).width() >= 992){
            $("body#home .calendar .shadow").each(function(){
                if($(this).outerHeight() > maxHeight){
                    maxHeight = $(this).outerHeight();
                }
            });
            $("body#home .calendar .shadow, body#home .actualites .shadow").innerHeight(maxHeight);
        }else{
            $("body#home .calendar .shadow").innerHeight('auto');
        }

        $("body#home .actualites .shadow").innerHeight(maxHeight);
    }else{
        $("body#home .calendar .shadow, body#home .actualites .shadow").innerHeight('auto');
    }
}