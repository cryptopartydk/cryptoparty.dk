from django import template

import CommonMark
from CommonMark import CommonMark

register = template.Library()


@register.filter
def markup(content):
    parser = CommonMark.DocParser()
    renderer = CommonMark.HTMLRenderer()
    ast = parser.parse(content)
    html = renderer.render(ast)
    return html