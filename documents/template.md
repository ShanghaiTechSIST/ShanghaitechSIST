# Chapter 5 前端页面模板

前端页面模板主要依照的是Django对于Template的定义，详细内容参考DJango官方文档。

##主要前端约定

###变量渲染

模板渲染是会有一些变量，在前端可以使用如下代码取得变量值。

```
{{ attr }}
{{ attr.attr }}字典属性查找/函数调用
```

###变量过滤器Filter

变量数据渲染的时候可以使用一些内置的filter，filter也可以带有一定的变量，允许自定义filter，参考官方文档。

```
{{ attr | filter:arg }}
{{ ship_date | date:"F j, Y" }} 格式化日期
{{ attr | lower | truncatewords:"30" }} 转为小写后截取前30个字
```

###逻辑块Tag

逻辑块可以理解为一些内置的语句。

```
{% cmd %}
```

####逻辑块 if

接受逻辑运算，接受==, !=, <, >, <=, >= and in 判断，逻辑运算中and优先于or。else可选。建议不做复杂判断。

```
{% if attr %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endif %}

{% if attr or attr2 %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endif %}

{% if not attr == 1 and attr2 > 2 %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endif %}
```

####逻辑块 ifequal & ifnotequal

字面意义，if的一种shortcut。


```
{% ifequal attr attr2 %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endifequal %}
```

####逻辑块 for


类Python循环，不接受计数器循环。empty可选，当被循环对象不存在或为空时触发。循环内存在forloop循环状态变量。

```
{% for item in list %}
    {{ item.name }}
{% endfor %}

{% for item in list %}
    {{ item.name }}
{% empty %}
    There is no item.
{% endfor %}

{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}

{% for item in list %}
    {{ item.name }}
    {% if not forloop.first %}、{% endif %}
{% endfor %}
```

##块定义与模板继承

允许通过```{% block name %}```的方式定义块或通过```{% block name %}something{% endblock %}```定义块及缺省内容。

在其他模板文件通过```{% extends "base.html" %}```标记继承上级模板，并在内部```{% block name %}something{% endblock %}```重载上级块定义。

允许通过```{% include "foo/bar.html" %}```标签导入其他模板页面的渲染结果。

前端模板大量使用了block和extends定义重用代码。

##Django-CMS官方前端页面模板的扩展约定

详细约定参阅Django-CMS官方文档

###定义Placeholder

定义Placeholder——及由Django-CMS控制的各页面不同的数据。由数据库渲染得到，运行状态后台可以修改。

```
{% placeholder 'article_content' %}
```

###获取页面参数

获取当前页面的部分状态数据，诸如页面的标题、当前语言等等。

```
{% page_attribute "page_title" %}
```

###更多

参考Django-CMS官方文档API部分关于Template Tag的定义。

##前端页面列表

前端页面均位于templates目录，下面列出的顺序为由继承定义的页面继承关系。

* root.html 根节点，定义了基本的页面样式，基本页面结构，公共header部分，渲染页面标题。
    * home.html 主页，重载root的root_body。
	* root_with_right_menu.html 分栏根节点，重载root的root_body，定义了左右分栏的页面结构，右分栏定义为一级节点的目录，左分栏定义为空。
    	* list.html 基本列表页面，重载root_with_right_menu的root_with_right_menu_body。
        	* list_news.html 新闻列表页面，重载list的list_body,修改列表项显示方式为新闻+新闻简介的样式。
        	* list_seminars.html 讲座列表页面，重载list的list_body,修改列表项显示方式为讲座+讲座时间的样式。
        	* list_overview.html 总览列表页面，重载list的list_body,修改列表项显示方式为一级加二级标题的样式。
    	* article.html 基本文章页面，重载root_with_right_menu的root_with_right_menu_body，可编辑文章内容。
        	* people.html 人员文章页面，重载article的article_content，可独立编辑个人信息。
        	* seminars.html 讲座文章页面，重载article的article_content，可独立编辑讲座信息。

##涉及代码

* templates
	* article.html
	* home.html
	* list.html
	* list_news.html
	* list_overview.html
	* list_seminars.html
	* people.html
	* root.html
	* root_with_right_menu.html
	* seminars.html
