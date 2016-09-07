from cms.models.pluginmodel import CMSPlugin

from django.db import models

class TimeRange(CMSPlugin):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
