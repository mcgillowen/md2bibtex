# -*- coding: utf-8 -*-

"""Main module."""

import re


def extract(link):
    match = re.search('\[([^\[\]]+)\]\(([^)]+)\)', link)
    return (match.group(1), match.group(2))
