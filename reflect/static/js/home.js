angular.module('MyApp',['ngMaterial','ngMessages','material.svgAssetsCache']).controller('formCtrl',function($scope,$mdDialog){

	$scope.user = {
		content:"",
		category:"",
		suggestions:""
	};

	$scope.$watch("user.category",
		function(newValue,oldValue){
			 console.log( "category changed" );
		}	
	); 

});	
setTimeout(function() {
	$('html, body').animate({
        scrollTop: $("#two").offset().top
    }, 1000);
 }, 2000);

// $('a[href*="#"]:not([href="#"])').click(function() {
//   if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
//     var target = $(this.hash);
//     console.log(target);
//     target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
//     if (target.length) {
//       $('html, body').animate({
//         scrollTop: target.offset().top
//       }, 1000);
//       return false;
//     }
//   }
// });