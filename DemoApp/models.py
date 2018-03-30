# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registration(models.Model):
	name = models.CharField(max_length = 60)
	email = models.CharField(max_length = 40)
	password = models.CharField(max_length = 40)
	def __unicode__(self):
		return self.name