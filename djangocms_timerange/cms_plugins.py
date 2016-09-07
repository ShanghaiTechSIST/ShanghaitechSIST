#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: eastpiger
# @Date:   2015-12-22 19:11:55
# @Last Modified by:   eastpiger
# @Last Modified time: 2015-12-22 19:22:35
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import TimeRange

class TimeRangePlugin(CMSPluginBase):
    model = TimeRange
    name = _("Time Range Plugin")
    render_template = "cms/plugins/timerange_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(TimeRangePlugin)
