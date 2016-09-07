from cms.models.pluginmodel import CMSPlugin

from django.db import models

class PlainText(CMSPlugin):
    body = models.CharField(max_length=255)
