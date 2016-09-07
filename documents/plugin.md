# Chapter 3 plugin扩展

Plain概念与运作机制，详见Django-CMS官方文档。

##PlainText原始文本插件

###涉及代码

* djangocms_plaintext
	* __init__.py Python模块标记文件
	* admin.py Admin注册文件（未使用）
	* cms_plugins.py 插件逻辑代码
	* models.py 数据库模型定义
	* templates 插件模板
		* cms
			* plugins
				* plaintext_plugin.html
	* tests.py 测试文件（未使用）
	* views.py 视图文件（未使用）

###程序逻辑
注册一个PlainText的数据类，提供不包含任何特定输出处理的原始文字串插件。

##TimeRange

###涉及代码

* djangocms_timerange
	* __init__.py Python模块标记文件
	* admin.py Admin注册文件（未使用）
	* cms_plugins.py 插件逻辑代码
	* migrations 数据库模型定义
	* models.py 插件模板
	* templates
		* cms
			* plugins
				* djangocms_timerange.html
	* tests.py 测试文件（未使用）
	* views.py 视图文件（未使用）

###程序逻辑
注册一个TimeRange的数据类，记录两个时间点，渲染为```Wed Dec. 30th, 2015, 3:00 p.m. ~ Wed Dec. 30th, 2015, 3:00 p.m.<var class="hide">Dec 30th</var>```

```
{{ instance.starttime | date:'D N jS, Y, g:i a' }} ~ {{ instance.endtime | date:'D N jS, Y, g:i a' }}
<var class="hide">{{ instance.starttime | date:'M jS' }}</var>
```

```<var class="hide">```一段封装为便于上级调取不同语言的样式。

