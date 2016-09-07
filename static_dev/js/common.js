$(function(){
	$(".clickbox").click(function(){
		location.href = $(this).attr("href")
	})
	$("#top-menu-btn").click(function(){
		$("body").toggleClass("mobile-menu-enabled");
	})
})
