from django import forms

class ChallengeLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    signed_challenge = forms.CharField(label='Challenge',widget=forms.Textarea)
