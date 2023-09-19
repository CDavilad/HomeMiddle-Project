from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        
        
    class Meta:
        model = Review
        fields = {'content'}
        widgets = {'content': Textarea(attrs={'rows': 4})}