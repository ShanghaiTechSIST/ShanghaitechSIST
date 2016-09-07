# Chapter 2 框架修改

代码内部对使用的Django_CMS有一定的扩展和修改。具体记录如下：

##综述

修改点位置在页面后台管理-创建页面和编辑页面的slogan部分。修正原框架代码对中文无法解析的问题。中文页面title将会自动转换为拼音。同时增加时间戳（可选）。

代码修改使用的是在优先级更高的static_dev目录和templates重新定义框架代码，使得渲染时优先使用修改后的代码。

未修改原始框架代码。

##涉及代码
* static_dev
	* admin
		* js
			* urlify.js 增加拼音入口
			* urlify_zh
				* pinyin.js 拼音解析组件
	* cms
		* js
			* dist
				* bundle.admin.changeform.min.js 增加时间戳入口