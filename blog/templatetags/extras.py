from django import template
register=template.Library()
@register.filter(name='get_val') 
#get_val is the name of the filter that we will use to filter out the replies

def get_val(dict,key):
    return dict.get(key)