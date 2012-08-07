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

from zope.component import adapts
from zope.component import provideAdapter
from sboard.profiles.nodes import ProfileView
from sboard.profiles.nodes import GroupView
from django.utils.translation import ugettext as _
from manoseimas.compat.models import PersonPosition

from .interfaces import IMPProfile
from .interfaces import IFraction


def search_lrs_url(query):
    pass


def format_position_percent(personposition):
    if personposition.position >= 0:
        return _(u'Palaiko %d%%') % personposition.position_percent()
    else:
        return _(u'Nepalaiko %d%%') % personposition.position_percent()


def prepare_position_list(node):
    """Returns list of positions of a person or fraction to be passed to a
    template."""
    positions = list(PersonPosition.objects.filter(profile=node))
    positions.sort(key=lambda pp: pp.node.ref.title)
    return [{
        'solution': pp.node,
        'position': pp.classify,
        'percent': format_position_percent(pp),
    } for pp in positions]


class MPProfileView(ProfileView):
    adapts(IMPProfile)
    template = 'mps/profile.html'

    def render(self, **overrides):
        context = {
            'positions': prepare_position_list(self.node),
        }
        context.update(overrides)
        return super(MPProfileView, self).render(**context)

provideAdapter(MPProfileView)


class FractionView(GroupView):
    adapts(IFraction)
    template = 'mps/fraction.html'

    def render(self, **overrides):
        context = {
            'positions': prepare_position_list(self.node),
        }
        context.update(overrides)
        return super(FractionView, self).render(**context)

provideAdapter(FractionView)
