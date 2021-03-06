from django import template
from classytags.arguments import (Argument, MultiValueArgument,
                                  MultiKeywordArgument)
from classytags.core import Options, Tag
from classytags.helpers import AsTag, InclusionTag
from cms.templatetags.cms_tags import _show_placeholder_by_id
from django.core.exceptions import ImproperlyConfigured
import math

register = template.Library()

class ShowPlaceholderByIdwithAS(InclusionTag):
    template = 'cms/content.html'
    name = 'show_placeholder_by_id'
    options = Options(
        Argument('placeholder_name'),
        Argument('reverse_id'),
        Argument('lang', required=False, default=None),
        Argument('site', required=False, default=None),
        'as',
        Argument('varname', required=False, resolve=False),
    )

    def __init__(self, parser, tokens, **kwargs):
        super().__init__(parser, tokens)
        if len(self.options.breakpoints) < 1:
            raise ImproperlyConfigured(
                "AsTag subclasses require at least one breakpoint."
            )
        last_breakpoint = self.options.options[self.options.breakpoints[-1]]
        optscount = len(last_breakpoint)
        if optscount != 1:
            raise ImproperlyConfigured(
                "The last breakpoint of AsTag subclasses require exactly one "
                "argument, got %s instead." % optscount
            )
        self.varname_name = last_breakpoint[-1].name

    def get_context(self, *args, **kwargs):
        try:
            return {'content': _show_placeholder_by_id(**self.get_kwargs(*args, **kwargs))}
        except:
            return {'content': ''}

    def get_kwargs(self, context, placeholder_name, reverse_id, lang, site, varname):
        cache_result = True
        if 'preview' in context['request'].GET:
            cache_result = False
        return {
            'context': context,
            'placeholder_name': placeholder_name,
            'reverse_id': reverse_id,
            'lang': lang,
            'site': site,
        }

    def render_tag(self, context, **kwargs):
        """
        INTERNAL!

        Gets the context and data to render.
        """
        value = super().render_tag(context, **kwargs)
        try:
            value = super().render_tag(context, **kwargs)
            varname = kwargs.pop(self.varname_name)
            if varname:
                context[varname] = value
                return ''
            else:
                return value
        except:
            return ''

register.tag('show_placeholder_as', ShowPlaceholderByIdwithAS)

class Paginate(AsTag):
    name = 'Paginate'
    options = Options(
        Argument('request'),
        Argument('container'),
        'maxitem',
        Argument('maxitem', resolve=False, required=False, default=30),
        'maxmenuitem',
        Argument('maxmenuitem', resolve=False, required=False, default=10),
        'page',
        Argument('page', resolve=False, required=False, default=0),
        'key',
        Argument('key', resolve=False, required=False, default='paginate_id'),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def __init__(self, parser, tokens, **kwargs):
        super().__init__(parser, tokens)

    def get_value(self, context, request, container, maxitem, maxmenuitem, page, key):
        maxitem, maxmenuitem, page = int(maxitem), int(maxmenuitem), int(page)
        length = len(container)
        maxpage = math.ceil(length / maxitem)

        if not page:
            try:
                page = int(request.GET[key])
            except:
                page = 1;

        if page > maxpage : page = maxpage
        if page < 1: page = 1

        response_page = []

        if maxpage < maxmenuitem:
            for i in range(1, maxpage + 1):
                response_page.append({
                    'id': i,
                    'currectpage': i == page,
                })
        elif page - (maxpage - 1) // 2 < 1:
            for i in range(1, maxmenuitem + 1):
                response_page.append({
                    'id': i,
                    'currectpage': i == page,
                })
        elif page + (maxpage - 1) // 2 > maxpage:
            for i in range(maxpage - maxmenuitem, maxpage + 1):
                response_page.append({
                    'id': i,
                    'currectpage': i == page,
                })
        else:
            for i in range(page - (maxpage - 1) // 2, page + (maxpage - 1) // 2 + 1):
                response_page.append({
                    'id': i,
                    'currectpage': i == page,
                })

        response = {
            'container': container,
            'containerP': container[maxitem * (page - 1): maxitem * page],
            'attr':{
                'currectpage': page,
                'maxpage': maxpage,
                'start': min(maxitem * (page - 1) + 1, length),
                'end': min(maxitem * page, length),
                'length': length,
                'page': response_page,
                'previous': page != 1,
                'next': page != maxpage,
                'key': key,
            }
        }

        return response

register.tag(Paginate)

class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value
        return u""

def set_var(parser, token):
    """
        {% set <var_name>  = <var_value> %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
    return SetVarNode(parts[1], parts[3])

register.tag('set', set_var)
