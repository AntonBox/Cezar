from django import forms


class check_NForm(forms.Form):
    rotate = forms.IntegerField()
    code = forms.CharField()

    def clean_rotate(self):
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        rotate = self.cleaned_data['rotate']
        if rotate not in range(0, len(alpha) + 1):
            raise forms.ValidationError('N is not in range(0-26)')

        return rotate
