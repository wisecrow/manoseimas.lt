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

"""
manoseimas - social project for Lithuanian parliament.

This project is based on Django web framework and has these apps:

mps
    Members of Parliament.

    This app mainly extends ``sboard.profiles`` functionality.

solutions
    Solutions are main object of this project and describes a solution to a
    problem or to a set of problems.

compat
    Compatibility checking app. This app helps to check if opinion on
    particular solutions or solution groups are compatible between different
    users and user groups.

scrapy
    Scrapy scripts for crawling data from various sources. Main source of data
    currently is lrs.lt - web site of Lithuanian parliament.

votings
    MPs votings, automatically crawled from lrs.lt.

"""
