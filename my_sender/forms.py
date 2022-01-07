from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='From')
    bcc = forms.CharField(required=False,widget = forms.Textarea)
    cc = forms.CharField(required=False,widget = forms.Textarea)
    reply_to = forms.CharField(required=False,widget = forms.Textarea)
    email_address = forms.CharField(widget = forms.Textarea)
    subject = forms.CharField(widget = forms.Textarea)
    extra_header = forms.CharField(widget = forms.Textarea,required=False)
    message = forms.CharField(widget = forms.Textarea)
    html_content = forms.CharField(widget = forms.Textarea,required=False)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)