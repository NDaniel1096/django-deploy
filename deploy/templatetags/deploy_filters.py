#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import importlib

from django import template

register = template.library()

@register.filter(name='reverse')
def reverse(value):
    """ Apache does not handle backslashes like Windows does,
        therefore, we convert them to forward slashes
    """
    return value.replace("\\", "/")

@register.simple_tag
def module_path(module_name):
    assert(module_name)
    module=importlib.import_module(module_name)
    return os.path.dirname(module.__file__)

@register.filter(name='directory')
def directory(filename):
    assert(filename)
    return os.path.dirname(filename)