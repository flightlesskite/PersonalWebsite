from django import template
from calvin.models import Category, Page

register = template.Library()

@register.inclusion_tag('calvin/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
            'act_cat':cat}
