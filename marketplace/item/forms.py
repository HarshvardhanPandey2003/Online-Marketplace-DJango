from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
# Here we use form.x or forms.y because with the help of it we can perform data validation
# And also it generates automatic form fields for HTML 
class BaseItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES})
        }

class NewItemForm(BaseItemForm):
    class Meta(BaseItemForm.Meta):
        fields = BaseItemForm.Meta.fields + ('category',)
        widgets = {**BaseItemForm.Meta.widgets,
                   'category': forms.Select(attrs={'class': INPUT_CLASSES})}

class EditItemForm(BaseItemForm):
    class Meta(BaseItemForm.Meta):
        fields = BaseItemForm.Meta.fields + ('is_sold',)