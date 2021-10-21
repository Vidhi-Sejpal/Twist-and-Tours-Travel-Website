(function($) {
    "use strict";
	
	
	/* ..............................................
    Gallery
    ................................................. */
	
	$('#slides').superslides({
		inherit_width_from: '.cover-slides',
		inherit_height_from: '.cover-slides',
		play: 20000,
		animation: 'fade',
	});
	
	$( ".cover-slides ul li" ).append( "<div class='overlay-background'></div>" );

	// Preloader
	$(window).on('load', function() {
		if ($('#preloader').length) {
		  $('#preloader').delay(100).fadeOut('slow', function() {
			$(this).remove();
		  });
		}
	  });
	
  
	// Smooth scroll for the navigation menu and links with .scrollto classes
	var scrolltoOffset = $('#header').outerHeight() - 1;
	$(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function(e) {
	  if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
		e.preventDefault();
		var target = $(this.hash);
		if (target.length) {
  
		  var scrollto = target.offset().top - scrolltoOffset;
  
		  if ($(this).attr("href") == '#header') {
			scrollto = 0;
		  }
  
		  $('html, body').animate({
			scrollTop: scrollto
		  }, 1500, 'easeInOutExpo');
  
		  if ($(this).parents('.nav-menu, .mobile-nav').length) {
			$('.nav-menu .active, .mobile-nav .active').removeClass('active');
			$(this).closest('li').addClass('active');
		  }
  
		  if ($('body').hasClass('mobile-nav-active')) {
			$('body').removeClass('mobile-nav-active');
			$('.mobile-nav-toggle i').toggleClass('fa fa-bars fas fa-times');
			$('.mobile-nav-overly').fadeOut();
		  }
		  return false;
		}
	  }
	});
  
	// Activate smooth scroll on page load with hash links in the url
	$(document).ready(function() {
	  if (window.location.hash) {
		var initial_nav = window.location.hash;
		if ($(initial_nav).length) {
		  var scrollto = $(initial_nav).offset().top - scrolltoOffset;
		  $('html, body').animate({
			scrollTop: scrollto
		  }, 1500, 'easeInOutExpo');
		}
	  }
	});
  
	// Mobile Navigation
	if ($('.nav-menu').length) {
	  var $mobile_nav = $('.nav-menu').clone().prop({
		class: 'mobile-nav d-lg-none'
	  });
	  $('body').append($mobile_nav);
	  $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="fa fa-bars"></i></button>');
	  $('body').append('<div class="mobile-nav-overly"></div>');
  
	  $(document).on('click', '.mobile-nav-toggle', function(e) {
		$('body').toggleClass('mobile-nav-active');
		$('.mobile-nav-toggle i').toggleClass('fa fa-bars fas fa-times');
		$('.mobile-nav-overly').toggle();
	  });
  
	  $(document).on('click', '.mobile-nav .drop-down > a', function(e) {
		e.preventDefault();
		$(this).next().slideToggle(300);
		$(this).parent().toggleClass('active');
	  });
  
	  $(document).click(function(e) {
		var container = $(".mobile-nav, .mobile-nav-toggle");
		if (!container.is(e.target) && container.has(e.target).length === 0) {
		  if ($('body').hasClass('mobile-nav-active')) {
			$('body').removeClass('mobile-nav-active');
			$('.mobile-nav-toggle i').toggleClass('fa fa-bars fas fa-times');
			$('.mobile-nav-overly').fadeOut();
		  }
		}
	  });
	} else if ($(".mobile-nav, .mobile-nav-toggle").length) {
	  $(".mobile-nav, .mobile-nav-toggle").hide();
	}
  
	// Toggle .header-scrolled class to #header when page is scrolled
	$(window).scroll(function() {
	  if ($(this).scrollTop() > 100) {
		$('#header').addClass('header-scrolled');
	  } else {
		$('#header').removeClass('header-scrolled');
	  }
	});
  
	if ($(window).scrollTop() > 100) {
	  $('#header').addClass('header-scrolled')
	}

	// Init AOS
	function aos_init() {
		AOS.init({
		  duration: 1000,
		  easing: "ease-in-out",
		  once: true,
		  mirror: false
		});
	  }
	  $(window).on('load', function() {
		aos_init();
	  });
	

	// Initiate venobox (lightbox feature used in portofilo)
	$(document).ready(function() {
		$('.venobox').venobox();
	  });

	$(document).ready(function() {
		$('select').niceSelect();
	});
	

})(jQuery);

$("#carousel").owlCarousel({
	autoplay: true,
	lazyLoad: true,
	loop: true,
	margin: 20,
	width:100,
	 /*
	animateOut: 'fadeOut',
	animateIn: 'fadeIn',
	*/
	responsiveClass: true,
	autoHeight: true,
	autoplayTimeout:5000,
	smartSpeed: 500,
	nav: true,
	responsive: {
	  0: {
		items: 1
	  },
	  600: {
		items: 2
	  },
  
	  800: {
		items: 3
	  },
  
	  1024: {
		items: 3
	  },
	}
  });

// Testimonials carousel (uses the Owl Carousel library)
$(".testimonials-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    responsive: {
      0: {
        items: 1
      },
      768: {
        items: 2
      },
      900: {
        items: 2
      }
    }
  });

// number count for stats, using jQuery animate

$(".counting").each(function () {
	var $this = $(this),
	  countTo = $this.attr("data-count");
  
	$({ countNum: $this.text() }).animate(
	  {
		countNum: countTo,
	  },
	  {
		duration: 20000,
		easing: "linear",
		step: function () {
		  $this.text(Math.floor(this.countNum));
		},
		complete: function () {
		  $this.text(this.countNum);
		  //alert('finished');
		},
	  }
	);
  });



var btn = $('#scroll-up');

$(window).scroll(function() {
	if ($(window).scrollTop() > 300) {
	btn.addClass('show');
	} else {
	btn.removeClass('show');
	}
});

btn.on('click', function(e) {
	e.preventDefault();
	$('html, body').animate({scrollTop:0}, '300');
});
