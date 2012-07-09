# coding: utf-8
# Copyright (C) 2012  Mantas Zimnickas <sirexas@gmail.com>
#
# This file is part of manoseimas.lt project.
#
# manoseimas.lt is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# manoseimas.lt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with manoseimas.lt.  If not, see <http://www.gnu.org/licenses/>.

from django import template
from django.forms.fields import CheckboxInput
from django.utils.translation import ugettext as _

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(value):
    return isinstance(value, CheckboxInput)

@register.filter(name='age_plural')
def age_plural(age):
    if age % 10 == 0 or 10 < age < 20:
        return _(u'metų')
    else:
        return _(u'metai')
