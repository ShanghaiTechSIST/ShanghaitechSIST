$(function(){
	$(".clickbox").click(function(){
		location.href = $(this).attr("href")
	})
	$("#top-menu-btn,#top-menu-mask").click(function(){
		$("body").toggleClass("mobile-menu-enabled");
	})
})
