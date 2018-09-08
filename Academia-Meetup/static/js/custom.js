/*

	Template Name: Eventor - Conference & Event HTML Template
	Author: Themewinter
	Author URI: https://themeforest.net/user/themewinter
	Description: Eventor - Conference & Event HTML Template
	Version: 1.0

	1. Mobile Menu
	2. Main Slideshow
	3. Gallery popup
	4. Counter
	5. Contact form
	6. Back to top
  
*/


jQuery(function($) {
  "use strict";


	/* ----------------------------------------------------------- */
	/*  Mobile Menu
	/* ----------------------------------------------------------- */

	jQuery(".nav.navbar-nav li a").on("click", function() { 
		jQuery(this).parent("li").find(".dropdown-menu").slideToggle();
		jQuery(this).find("i").toggleClass("fa-angle-down fa-angle-up");
	});


	/* ----------------------------------------------------------- */
	/*  Event counter 
	/* -----------------------------------------------------------*/

	if ( $( '.countdown' ).length > 0 ) {
		$(".countdown").jCounter({
		  	date: '11 November 2017 09:00:00',
		  	fallback: function() { console.log("count finished!") }
		});
	}


	/* ----------------------------------------------------------- */
	/*  Main slideshow
	/* ----------------------------------------------------------- */

		$('#main-slide').carousel({
			pause: true,
			interval: 100000,
		});


	/* ----------------------------------------------------------- */
	/*  Gallery popup
	/* ----------------------------------------------------------- */

	  $(document).ready(function(){

			$(".gallery-popup").colorbox({rel:'gallery-popup', transition:"fade", innerHeight:"700"});

			$(".popup").colorbox({iframe:true, innerWidth:650, innerHeight:450});

			$('#success-box').hide();
	  });



	/* ----------------------------------------------------------- */
	/*  Counter
	/* ----------------------------------------------------------- */

		$('.counterUp').counterUp({
		 delay: 10,
		 time: 1000
		});


	
	/* ----------------------------------------------------------- */
	/*  Contact form
	/* ----------------------------------------------------------- */

	$('form#register-form').submit(function(e){
		var $form = $(this);
		var action = 'http://35.198.219.143:8080/subscriber';
		var $name = $form.find('.form-control-name'),
			$email = $form.find('.form-control-email'),
			$github = $form.find('.form-control-github'),
			$mobile = $form.find('.form-control-mobile'),
			$gender = $form.find('.form-control-gender'),
			$location = $form.find('.form-control-location'),
			$track = $form.find('.form-control-track'),
			$type = $form.find('.form-control-type');

		$.post(action, {
			name: $name.val(),
			email: $email.val(),
			github: $github.val(),
			mobile: $mobile.val(),
			state: $location.val(),
			gender: $gender.val(),
			track: $track.val(),
			type: $type.val()
		},
		function (data) {
			$('#success-box').show();
		});

		return false;
	});


	/* ----------------------------------------------------------- */
	/*  Back to top
	/* ----------------------------------------------------------- */

		$(window).scroll(function () {
			if ($(this).scrollTop() > 50) {
				 $('#back-to-top').fadeIn();
			} else {
				 $('#back-to-top').fadeOut();
			}
		});

		// scroll body to 0px on click
		$('#back-to-top').on('click', function () {
			 $('#back-to-top').tooltip('hide');
			 $('body,html').animate({
				  scrollTop: 0
			 }, 800);
			 return false;
		});
		
		$('#back-to-top').tooltip('hide');


});