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
		// console.log(page);
		$('#global-nav li a').each(function(i, el) {
			// console.log(el);
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
		// var newSrc = string[0] +'2x'+ string[1];
		// do it up
		// img['src'] = newSrc;
		img['src'] = string[0]+'2x'+string[1];
	}

	return {
		highres: highres
	};
})()