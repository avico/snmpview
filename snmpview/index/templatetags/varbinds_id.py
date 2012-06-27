from django import template

register = template.Library()

@register.filter
def varbinds_id(parent_loop, loop):
    """returns unique id for varbinds. Formula: [(num alarms(rows) per page)*forloop.parentloop.counter + forloop.counter]"""
    #number rows per page hardcoded = 1012. Please change this value if num of objects changed in paginator
    return 1012*int(parent_loop) + int(loop)
