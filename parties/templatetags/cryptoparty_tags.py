from django import template

import CommonMark

register = template.Library()


@register.filter
def markup(input):
    parser = CommonMark.DocParser()
    renderer = CommonMark.HTMLRenderer()
    ast = parser.parse(input)
    return renderer.render(ast)
