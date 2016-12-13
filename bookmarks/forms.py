from django import forms
from django.contrib.auth.models import User
from .models import Category, Page, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), help_text="Category")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ['name']


class PageForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), help_text="Title")
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'input'}), help_text="URL")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ['category']


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    website = forms.CharField(widget=forms.URLInput(attrs={'class': 'input'}))

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

