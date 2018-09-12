import markdown
from django import template

register = template.Library()


@register.filter
def markdownFilter(value):
    return markdown.markdown(value)
