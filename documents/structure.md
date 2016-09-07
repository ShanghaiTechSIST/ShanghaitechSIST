# Chapter 1 基本结构

##结构说明

###后端框架

整体站点构建在Python Django 1.8.6的Python 3版本上，使用django的基本框架、Django_CMS框架以及部分Django_CMS官方插件，尽可能使用开源组件，减少自主开发部分。

###前端框架

前端主要使用的框架是Jquery 2.1.4、Bootstrap 3.3.5、glyphicons图标字库。

##安装

安装Python3(ubuntu)

```
apt-get install python3 python3-pip
```

安装Django

```
pip3 install 'django==1.8.6'
```

安装Django_CMS

```
pip install django-cms
```

安装插件

```
pip3 install djangocms-text-ckeditor
pip3 install djangocms-picture
pip3 install djangocms-file
```

安装数据库支持

数据库连接使用Django官方的连接模块，可以任意选择Django支持的数据库postgresql、mysql、sqlite3、oracle等，可能需要对特定的服务器安装特定的组件，具体查阅Django官方文档。

源代码默认状态使用sqlite3。

##配置

核心配置文件位于shanghaitech_SIST/settings.py，内部内容说明参见注释，Django官方文档及Django_CMS官方文档。

##数据库

数据库结构由Django内置的抽象层处理。

数据库连接使用Django官方的连接模块，可以任意选择Django支持的数据库postgresql、mysql、sqlite3、oracle等，可能需要对特定的服务器安装特定的组件，具体查阅Django官方文档。

数据库使用方法详见Django官方文档。以下仅给出示例。

```
python3 manage.py makemigrations
python3 manage.py migrate
```

##静态数据

静态数据，包括上传数据，由Django接管。详见Django官方文档。

目录位置可在Django管理内修改，前端模板渲染均使用了Django staticfile标签管理。

静态文件开发在static_dev目录下，由以下指令遍历收集所有静态文件后放置在static目录。

```
python3 manage.py collectstatic
```

##服务器

不需要特定的服务器配置，仅需按照Django的官方服务器连接即可。推荐使用Nginx+Gunicorm搭配。

开发环境使用如下内置开发服务器

```
python3 manage.py server 127.0.0.1:8000
```

##目录结构说明

注：
__init__.py文件为Python模块标志文件，无内容，不可删除。

__pycache__目录为Python执行缓存目录，可删除。

migrations目录为Django数据库结构分析目录，可删除

*.pyc文件为Python执行临时文件，可删除。


* README.md 文档说明首页
* SUMMARY.md 文档目录
* _doc GitBook文档输出目录
* db.sqlite3 开发数据库（可随时替换）
* djangocms_plaintext 扩展插件plaintext，参见Chapter3
	* __init__.py
	* admin.py
	* cms_plugins.py
	* models.py
	* templates
		* cms
			* plugins
				* plaintext_plugin.html
	* tests.py
	* views.py
* djangocms_timerange 扩展插件timerange，参见Chapter3
	* __init__.py
	* admin.py
	* cms_plugins.py
	* migrations
	* models.py
	* templates
		* cms
			* plugins
				* djangocms_timerange.html
	* tests.py
	* views.py
	*
* documents 文档内容
* manage.py Django服务器接口模块
* media 上传目录位置，可在配置内修改
* shanghaitech_SIST 核心APP模块
	* __init__.py
	* settings.py 核心配置文件
	* templatetags Tag扩展，参见Chapter4
		* __init__.py
		* sist_tags.py
	* urls.py URL路由定义
	* wsgi.py WSGI连接模块
* static 静态文件输出模块，此目录内容由collectstaticfile生成
* static_dev 静态文件开发模块
	* admin 优先级覆盖Django_CMS，参见Chapter2
		* js
			* urlify.js
			* urlify_zh
				* pinyin.js
	* cms 优先级覆盖Django_CMS，参见Chapter2
		* js
			* dist
				* bundle.admin.changeform.min.js
	* css CSS样式表定义
		* article.css
		* bootstrap-theme.css
		* bootstrap-theme.css.map
		* bootstrap-theme.min.css
		* bootstrap.css
		* bootstrap.css.map
		* bootstrap.min.css
		* common.css
		* home.css
		* list.css
		* seminars.css
	* fonts glyphicons相关图标字体
		* glyphicons-halflings-regular.eot
		* glyphicons-halflings-regular.svg
		* glyphicons-halflings-regular.ttf
		* glyphicons-halflings-regular.woff
		* glyphicons-halflings-regular.woff2
	* image 图片
		* LOGO.png
		* LOGO_shanghaitech.png
		* bg.jpg
		* bg_mark.jpg
		* bg_up.png
		* people_none.jpg
	* js js文件
		* bootstrap.js
		* bootstrap.min.js
		* common.js
		* jquery-2.1.4.min.js
		* npm.js
* templates 前端渲染模板
	* root.html 根页面模板，参见Chapter5
	* root_with_right_menu.html
	* home.html 主页页面模板，参见Chapter5
左右分栏页面模板，参见Chapter5
	* article.html 文章页面模板，参见Chapter5
	* list.html 列表根页面模板，参见Chapter5
	* list_news.html 新闻列表页面模板，参见Chapter5
	* list_overview.html 总览列表页面模板，参见Chapter5
	* list_seminars.html 讲座页面列表模板，参见Chapter5
	* people.html 人员页面模板，参见Chapter5
	* seminars.html 讲座页面模板，参见Chapter5
	* menu 菜单模板，参见Chapter6
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
