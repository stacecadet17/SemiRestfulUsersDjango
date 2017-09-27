# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
NAME_REGEX = re.compile(r"^[-a-zA-Z]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


# Create your models here.
class BlogManage(models.Manager):
    def validator(self, postdata, valid):
        errors = {}
        if len(postdata["first_name"]) < 1:
            errors["first_name"] = "Must enter a first name!"
        elif not NAME_REGEX.match(postdata["first_name"]):
            errors["first_name"] = "First name is invalid!"
        if len(postdata["last_name"]) < 1:
            errors["last_name"] = "Must enter a last name!"
        elif not NAME_REGEX.match(postdata["last_name"]):
            errors["last_name"] = "last name is invalid!"
        if len(postdata["email"]) < 1:
            errors["email"] = "Must enter an email!"
        elif not EMAIL_REGEX.match(postdata["email"]):
            errors["email"] = "Email address not valid!"
        if valid == "create":
            if User.objects.filter(email=postdata["email"]):
                errors["email"] = "Email address is aready taken!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManage()
