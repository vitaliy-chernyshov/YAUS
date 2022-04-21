from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    field.field.widget.attrs["class"] = css
    return field


@register.filter
def placeholder(field, placeholder=None):
    if placeholder is not None:
        field.field.widget.attrs["placeholder"] = placeholder
    else:
        field.field.widget.attrs["placeholder"] = field.field.help_text
    return field
