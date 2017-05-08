function deselect(e) {
  $('.pop').slideFadeToggle(function() {
    e.removeClass('selected');
  });    
}

$(function() {
  $('.in-cart').on('click', function() {
    var cart = document.getElementById('cart-img');
    if (cart) {
      cart.style.opacity = "0.5";
      cart.style.filter  = 'alpha(opacity=90)'; // IE fallback
    }

    if($(this).hasClass('selected')) {
      deselect($(this)); 
      console.log("deselect works")              
    } 
    else {
      $(this).addClass('selected');
      console.log("select works")
      //$('.pop').css({left:e.pageX,top:e.pageY}).slideFadeToggle();
      $('.pop').slideFadeToggle();
      $('body').scrollTop(0);
    }
    return false;
  });

  $('.close').on('click', function() {
    var cart = document.getElementById('cart-img');
    if (cart) {
      cart.style.opacity = "1.0";
      cart.style.filter  = 'alpha(opacity=90)'; // IE fallback
    }
    deselect($('.in-cart'));
    console.log("close works")
    return false;
  });
});

$.fn.slideFadeToggle = function(easing, callback) {
  return this.animate({ opacity: 'toggle', height: 'toggle' }, 'fast', easing, callback);
};

if (document.readyState === 'interactive') {
	document.getElementById("minishopcart_total").innerHTML = numCart;
}

///////////////////////////////////////////

function addToCart() {
	console.log("works")
	//numCart ++;
  //console.log("numCart works")
 	//document.getElementById("minishopcart_total").innerHTML = numCart;
 	//alert("Je hebt het speelgoed gevonden! Ga nu verder met de volgende opdracht");
 }