# -*- coding: utf-8 -*-
"""Render a given template and data into PDF"""

from pyramid.response import Response
from pyramid.renderers import get_renderer

from datetime import datetime
from StringIO import StringIO
from xhtml2pdf import pisa


def render(request):
    # Get url dispatch and request data
    name = request.matchdict.get('template', 'default')
    data = request.GET['data'] or {}

    # Get template and render it into HTML
    template = get_renderer('templates/%s.pt' % name)
    html = template(data, request)

    # Create PDF from HTML
    pdf = StringIO()
    pisa.CreatePDF(html, pdf)
    pdf.seek(0)

    # Generate filename for content-disposition=attachment
    filename = '%s_%s.pdf' % (name.capitalize(),
                              datetime.now().strftime('%d-%m-%Y'))

    # Create PDF-response
    return Response(pdf.read(),
                    content_type='application/pdf',
                    content_disposition='attachment; filename="%s"' % filename)
