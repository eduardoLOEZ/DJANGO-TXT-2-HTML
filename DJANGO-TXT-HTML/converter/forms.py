from django.forms import ModelForm, CharField
from .models import Editor
from ckeditor.widgets import CKEditorWidget

class EditorForm(ModelForm):
    body =CharField(
        widget=CKEditorWidget(),
        label= "Enter ypur text here..."
    )
    
    class Meta:
        model= Editor
        fields= "__all__"