from django import template

from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def circle_page(curr_page, loop_page):
    """自定义标签过滤器"""
    offset = abs(curr_page - loop_page)
    # 无论有多少个页数，只显示三个
    if offset < 2:
        if curr_page == loop_page:
            page_ele = '<a style="color: #6FA5DB" href="/index/?num=%d">%s</a>' % (int(loop_page), loop_page)
        else:
            page_ele = '<a  href="/index/?num=%d">%s</a>' % (int(loop_page), loop_page)
        return format_html(page_ele)
    return ''

