jQuery(function($) {

	"use strict";

		/**
		 * Bootstrap Tooltip
		 */	
		 
		$('[data-toggle="tooltip"]').tooltip();
		
		
		/**
		 * Sticky Header
		 */
				
		$(window).scroll(function(){

			if( $(window).scrollTop() > 10 ){

				$('.navbar').addClass('navbar-sticky')

			} else {
				$('.navbar').removeClass('navbar-sticky')
			}

		})
		
		/**
		 * Main Menu Slide Down Effect
		 */
		 
		var selected = $('#navbar li');
		// Mouse-enter dropdown
		selected.on("mouseenter", function() {
				$(this).find('ul').first().stop(true, true).delay(350).slideDown(500, 'easeInOutQuad');
		});

		// Mouse-leave dropdown
		selected.on("mouseleave", function() {
				$(this).find('ul').first().stop(true, true).delay(100).slideUp(150, 'easeInOutQuad');
		});
		
		
		
		/**
		 * Slicknav - a Mobile Menu
		 */
		var $slicknav_label;
		$('.responsive-menu').slicknav({
			duration: 500,
			easingOpen: 'easeInExpo',
			easingClose: 'easeOutExpo',
			closedSymbol: '<i class="fa fa-plus"></i>',
			openedSymbol: '<i class="fa fa-minus"></i>',
			prependTo: '#slicknav-mobile',
			allowParentLinks: true,
			label:"" 
		});

		var $slicknav_label;
		$('#responsive-menu').slicknav({
			duration: 500,
			easingOpen: 'easeInExpo',
			easingClose: 'easeOutExpo',
			closedSymbol: '<i class="fa fa-plus"></i>',
			openedSymbol: '<i class="fa fa-minus"></i>',
			prependTo: '#slicknav-mobile',
			allowParentLinks: true,
			label:"" 
		});
		
		
		
		/**
		 * Smooth scroll to anchor
		 */
		$('a.anchor[href*=#]:not([href=#])').on("click",function() {
			if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
				var target = $(this.hash);
				target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
				if (target.length) {
					$('html,body').animate({
						scrollTop: (target.offset().top - 70) // 70px offset for navbar menu
					}, 1000);
					return false;
				}
			}
		});
		
		
		
		/**
		 * Another Bootstrap Toggle
		 */
		$('.another-toggle').on("click",function() {
			if( $('h4',this).hasClass('active') ){
				$(this).find('.another-toggle-content').show();
			}
		});
		$('.another-toggle h4').on("click",function() {
			if( $(this).hasClass('active') ){
				$(this).removeClass('active');
				$(this).next('.another-toggle-content').slideUp();
			} else {
				$(this).addClass('active');
				$(this).next('.another-toggle-content').slideDown();
			}
		});
		
		

		/**
		 *  Arrow for Menu has sub-menu
		 */
		if ($(window).width() > 992) {
			$(".navbar-arrow ul ul > li").has("ul").children("a").append("<i class='arrow-indicator fa fa-angle-right'></i>");
		}
		
		
		
		/**
		 * Payment Option
		 */
		var selected2 = $("div.payment-option-form"); 
		selected2.hide();
		$("input[name$='payments']").on("click",function() {
				var test = $(this).val();
				selected2.hide();
				$("#" + test).show();
		});
		
		
		
		/**
		 * Icon Change on Collapse
		 */
		$('.collapse.in').prev('.panel-heading').addClass('active');
		$('.bootstrap-accordion, .bootstrap-toggle')
		.on('show.bs.collapse', function(a) {
			$(a.target).prev('.panel-heading').addClass('active');
		})
		.on('hide.bs.collapse', function(a) {
			$(a.target).prev('.panel-heading').removeClass('active');
		});
		
		
		
		/**
		 * Back To Top
		 */
		var selected3 = $("#back-to-top");

		$(window).scroll(function(){
			if($(window).scrollTop() > 500){
				selected3.fadeIn(200);
			} else{
				selected3.fadeOut(200);
			}
		});
		selected3.on("click",function() {
				$('html, body').animate({ scrollTop:0 }, '800');
				return false;
		});

		
		/**
		 * Placeholder
		 */
		$("input, textarea").placeholder();
		
		
		
		/**
		* Bootstrap rating
		*/

		var selected4 = $('.rating-label');

		selected4.rating();
			
		selected4.each(function () {
		$('<span class="label label-default"></span>')
			.text($(this).val() || ' ')
			.insertAfter(this);
		});
		selected4.on('change', function () {
		$(this).next('.label').text($(this).val());
		});

		
		
		/**
		 * Sign-in Modal
		 */
		var $formLogin = $('#login-form');
		var $formLost = $('#lost-form');
		var $formRegister = $('#register-form');
		var $divForms = $('#modal-login-form-wrapper');
		var $modalAnimateTime = 300;
		
		$('#login_register_btn').on("click", function () { modalAnimate($formLogin, $formRegister) });
		$('#register_login_btn').on("click", function () { modalAnimate($formRegister, $formLogin); });
		$('#login_lost_btn').on("click", function () { modalAnimate($formLogin, $formLost); });
		$('#lost_login_btn').on("click", function () { modalAnimate($formLost, $formLogin); });
		$('#lost_register_btn').on("click", function () { modalAnimate($formLost, $formRegister); });
		
		function modalAnimate ($oldForm, $newForm) {
			var $oldH = $oldForm.height();
			var $newH = $newForm.height();
			$divForms.css("height",$oldH);
			$oldForm.fadeToggle($modalAnimateTime, function(){
				$divForms.animate({height: $newH}, $modalAnimateTime, function(){
					$newForm.fadeToggle($modalAnimateTime);
				});
			});
		}
		
		
		/**
		 * Read more-less paragraph
		 */
		var showTotalChar = 130, showChar = "read more +", hideChar = "read less -";
		$('.read-more-less').each(function() {
			var content = $(this).text();
			if (content.length > showTotalChar) {
				var con = content.substr(0, showTotalChar);
				var hcon = content.substr(showTotalChar, content.length - showTotalChar);
				var txt= con +  '<span class="dots">...</span><span class="morectnt"><span>' + hcon + '</span>&nbsp;&nbsp;<a href="" class="showmoretxt">' + showChar + '</a></span>';
			$(this).html(txt);
			}
		});
		$(".showmoretxt").on("click",function() {
			if ($(this).hasClass("sample")) {
				$(this).removeClass("sample");
				$(this).text(showChar);
			} else {
				$(this).addClass("sample");
				$(this).text(hideChar);
			}
			$(this).parent().prev().toggle();
			$(this).prev().toggle();
			return false;
		});

		// SLICK SLIDER

		$('.responsive').slick({
		  dots: false,
		  infinite: true,
		  speed: 300,
		  slidesToShow: 4,
		  slidesToScroll: 1,
		  responsive: [
		    {
		      breakpoint: 1024,
		      settings: {
		        slidesToShow: 3,
		        slidesToScroll: 3,
		        infinite: true,
		        dots: false
		      }
		    },
		    {
		      breakpoint: 600,
		      settings: {
		        slidesToShow: 2,
		        slidesToScroll: 2
		      }
		    },
		    {
		      breakpoint: 480,
		      settings: {
		        slidesToShow: 1,
		        slidesToScroll: 1
		      }
		    }
		    // You can unslick at a given breakpoint now by adding:
		    // settings: "unslick"
		    // instead of a settings object
		  ]
		});


		// SLICK SLIDER STYLE TESTIMONIAL

		$('.testimonial1').slick({
		  dots: false,
		  infinite: true,
		  speed: 300,
		  slidesToShow: 2,
		  slidesToScroll: 1,
		  responsive: [
		    {
		      breakpoint: 1024,
		      settings: {
		        slidesToShow: 2,
		        infinite: true,
		        dots: false
		      }
		    },
		    {
		      breakpoint: 600,
		      settings: {
		        slidesToShow: 2
		      }
		    },
		    {
		      breakpoint: 480,
		      settings: {
		        slidesToShow: 1
		      }
		    }
		    // You can unslick at a given breakpoint now by adding:
		    // settings: "unslick"
		    // instead of a settings object
		  ]
		});

		// SLICK SLIDER STYLE TESTIMONIAL

		$('.testimonial2').slick({
		  dots: false,
		  infinite: true,
		  speed: 300,
		  slidesToShow: 1,
		  slidesToScroll: 1,
		  responsive: [
		    {
		      breakpoint: 1024,
		      settings: {
		        slidesToShow: 3,
		        infinite: true,
		        dots: false
		      }
		    },
		    {
		      breakpoint: 600,
		      settings: {
		        slidesToShow: 2,
		      }
		    },
		    {
		      breakpoint: 480,
		      settings: {
		        slidesToShow: 1,
		        slidesToScroll: 1
		      }
		    }
		    // You can unslick at a given breakpoint now by adding:
		    // settings: "unslick"
		    // instead of a settings object
		  ]
		});

		$('.tour-cats').slick({
			  dots: false,
			  infinite: true,
			  speed: 300,
			  slidesToShow: 6,
			  slidesToScroll: 1,
			  responsive: [
			    {
			      breakpoint: 1024,
			      settings: {
			        slidesToShow: 3,
			        infinite: true,
			        dots: false
			      }
			    },
			    {
			      breakpoint: 600,
			      settings: {
			        slidesToShow: 2
			      }
			    },
			    {
			      breakpoint: 480,
			      settings: {
			        slidesToShow: 1

			      }
			    }
			    // You can unslick at a given breakpoint now by adding:
			    // settings: "unslick"
			    // instead of a settings object
			  ]
			});

	

		$('.main-banner').slick();

		// FADE SLIDER
		$('.sidefd').slick({
		  dots: false,
		  infinite: true,
		  speed: 200,
		  slide: true,
		  autoplay :true,
		  cssEase: 'linear'
		});

		$(document).on('click','.itenerary_tab',function(){

			var tab_class = $(this).next().find('.tab-gallery').attr('data-tab');
			var selector = "." + tab_class;

			$( selector ).slick({
			  dots: false,
			  infinite: false,
			  arrows: true,
			  speed: 300,
			  slidesToShow: 5,
			  slidesToScroll: 1,
			  responsive: [
			    {
			      breakpoint: 1024,
			      settings: {
			        slidesToShow: 3,
			        slidesToScroll: 3,
			        infinite: true,
			      }
			    },
			    {
			      breakpoint: 600,
			      settings: {
			        slidesToShow: 2,
			        slidesToScroll: 2
			      }
			    },
			    {
			      breakpoint: 480,
			      settings: {
			        slidesToShow: 1,
			        slidesToScroll: 1
			      }
			    }
			    // You can unslick at a given breakpoint now by adding:
			    // settings: "unslick"
			    // instead of a settings object
			  ]
			});

		});

		$('.fading').slick({
		  dots: false,
		  infinite: true,
		  speed: 300,
		  fade: true,
		  arrows: true,
		  autoplay: true,
		  cssEase: 'linear'
		});


		$('.video_play_pause').on('click',function(){
			
			var video = $(this).prev();

			if( video.get(0).paused ){
				video.get(0).play();
				$(this).find('i').removeClass('fa-play').addClass('fa-pause');
			} else {
				video.get(0).pause();	
				$(this).find('i').removeClass('fa-pause').addClass('fa-play');
			}
			
		});



		$('#hero-video').YTPlayer({
		    fitToBackground: true,
		    videoId: '4NtfDBY_DVQ'
		});
		

		/*====================================
					Clock Countdown
		======================================*/

		$('#clock-countdown').countdown('2018/9/20 12:00:00').on('update.countdown', function(event) {
			var $this = $(this).html(event.strftime(''
				+ '<div class="counter-container"><div class="counter-box first"><div class="number">%-D</div><span>Day%!d</span></div>'
				+ '<div class="counter-box"><div class="number">%H</div><span>Hours</span></div>'
				+ '<div class="counter-box"><div class="number">%M</div><span>Minutes</span></div>'
				+ '<div class="counter-box last"><div class="number">%S</div><span>Seconds</span></div></div>'
			));
		});
		

});

;