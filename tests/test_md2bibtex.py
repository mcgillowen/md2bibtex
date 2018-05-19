#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `md2bibtex` package."""

import pytest

from click.testing import CliRunner

from md2bibtex import md2bibtex
from md2bibtex import cli


@pytest.mark.parametrize('md_link, link_tuple', [
    ('[Name of link](http://www.example.test)', (u'Name of link', u'http://www.example.test')),
])
def test_basic_extraction(md_link, link_tuple):
    """
    Test the basic extraction of information from markdown link

    The extraction should return (u'Name of link', u'http://www.example.test')
    from [Name of link](http://www.example.test)
    """
    assert md2bibtex.extract(md_link) == link_tuple


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'md2bibtex.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
