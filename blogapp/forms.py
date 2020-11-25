from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ['title', 'pub_date', 'body']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'pub_date': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '작성 날자'}
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }