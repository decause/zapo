var zapo = {}; //global var

//wait until main document is loaded
window.addEventListener('load',function(){
  zapo.main.init();
}); //end addEventListener

zapo.main = (function() {
	var init = function() {
		nav();
		jpgs();
		$('#zapo').addClass('highres');
		// highres should really be added only if 
		// there is a strong connection speed
	}

	var nav = function() {
		var page = $('#zapo').attr('data-page');

		// page specfic things
		if (page === 'index') {
			$html = $('html');
			$html.addClass('full-height');
			if ($html.height() <= 480) $html.removeClass('full-height');
		}
		
		if (page === 'work') {
			// new swipe slider is created with name:
			// swipe-[index]. ex. swipe-0, swipe-1, swipe-2
			$('.swipe').each(function(i, el) {
				$el = $(el);

				var newSwipe = 'swipe-'+i;
				window[newSwipe] = $el.Swipe({
					auto: Math.floor((Math.random()*5000)+3000)
				}).data('Swipe'); // auto swipe each at random intervals

				// set next and prev controls
				$el.find('.prev').on('click', function(e) {
					window[newSwipe].prev();
				});

				$el.find('.next').on('click', function(e) {
					window[newSwipe].next();
				});
			});
		}

		// updating nav
		$('#global-nav li a').each(function(i, el) {
			if (el.innerHTML === page) {
				$(el).addClass('current');
			}
		});
	}

	var jpgs = function() {
		// find all imgs with class "jpg". replace src attr with 2x
		$('.jpg').each(function(i, el) {
			zapo.images.highres(el);
		});
	}

	return {
		init: init
	};
})();


zapo.images = (function() {
	var highres = function(img) {
		var src = img['src'];
		string = src.split('1x');
		img['src'] = string[0]+'2x'+string[1];
	}

	return {
		highres: highres
	};
})()