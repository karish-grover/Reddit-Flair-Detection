from django import forms

class RedditForm(forms.Form):
	url= forms.URLField(label="Please enter the Reddit URL ", widget=forms.URLInput(attrs={'size': '40'}))



