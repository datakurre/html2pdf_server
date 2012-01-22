# -*- coding: utf-8 -*-
"""HTML to PDF -server"""

from pyramid.config import Configurator


def main(global_config, **settings):
    """Returns a Pyramid WSGI application"""
    config = Configurator(settings=settings)
    config.include('pyramid_zcml')
    config.load_zcml('configure.zcml')
    return config.make_wsgi_app()
