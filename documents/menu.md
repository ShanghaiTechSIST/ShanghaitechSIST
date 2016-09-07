# Chapter 6 前端菜单模板

前端菜单页面模板主要依照的是Django对于Template的定义，由Django-CMS的menu模块负责处理。详细内容参考DJango和Django-CMS官方文档。

##主要前端约定

菜单模板提供一个基本的children对象，对象内为menu的具体内容。对每一个children对象的子对象，提供对象的基本参数，部分函数接口，可以结合page_lookup和id属性取得页面对象，继而使用tag扩展访问页面对象内容。

##涉及代码

* templates
	* menu
		* home_news_menu.html
		* home_seminars_menu.html
		* language_chooser.html
		* list_menu.html
		* list_news_menu.html
		* list_overview_inner_menu.html
		* list_overview_menu.html
		* list_seminars_menu.html
		* root_menu.html
		* root_with_right_menu_menu.html
