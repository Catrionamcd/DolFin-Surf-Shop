"""
    Product Form
"""

from django import forms
from django.forms import Textarea
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductComment


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_names = [(c.id, c.get_category_name()) for c in categories]

        self.fields['category'].choices = category_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductCommentForm(forms.ModelForm):
    """ A form to attach a user comment to a product to a """

    class Meta:
        model = ProductComment
        fields = ('product_comment',)
        labels = {
            'product_comment': '<strong>Comment:</strong>'
        }

        widgets = {
            'product_comment': Textarea(attrs={'cols': 200, 'rows': 10})
        }
