from django import forms
from .models import Notice
from django_summernote.widgets import SummernoteWidget

class NoticeForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    class Meta:
        model = Notice
        fields = ('text', 'is_public',)