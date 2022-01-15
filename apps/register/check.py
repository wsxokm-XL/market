from django import forms


class RegisterCheck(forms.Form):
    username = forms.CharField(label='username', max_length=10, min_length=4, required=True,
                               error_messages={"max_length": "用户名最长为10", "min_length": "用户名最短为4"})
    password = forms.CharField(label='password',max_length=12, min_length=6, required=True,
                               error_messages={"max_length": "密码最长为12", "min_length": "密码最短为6"})

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
