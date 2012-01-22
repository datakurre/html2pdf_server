# -*- coding: utf-8 -*-
"""Render a given template as PDF"""

from pyramid.response import Response
from pyramid.renderers import get_renderer

from StringIO import StringIO
from xhtml2pdf import pisa


def render(request):
    template = get_renderer('templates/default.pt')
    html = template({'project': 'Hello World'}, request)
    pdf = StringIO()
    pisa.CreatePDF(html, pdf)
    pdf.seek(0)
    return Response(pdf.read(),
                    content_type='application/pdf',
                    content_disposition='attachment; filename="output.pdf"')
