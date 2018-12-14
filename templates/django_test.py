# clean_password2被调用的原因
'''
def _clean_fields(self):
        for name, field in self.fields.items():
            # value_from_datadict() gets the data from the data dictionaries.
            # Each widget type knows how to retrieve its own data, because some
            # widgets split data over several HTML fields.
            if field.disabled:
                value = self.get_initial_for_field(field, name)
            else:
                value = field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))
            try:
                if isinstance(field, FileField):
                    initial = self.get_initial_for_field(field, name)
                    value = field.clean(value, initial)
                else:
                    value = field.clean(value)
                self.cleaned_data[name] = value
                if hasattr(self, 'clean_%s' % name):
                    value = getattr(self, 'clean_%s' % name)()
                    self.cleaned_data[name] = value
            except ValidationError as e:
                self.add_error(name, e)
'''

from django.core.exceptions import ValidationError
import re
  
def phone_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class test_form(forms.Form):
    username = forms.CharField(label='username', strip=False, widget=forms.TextInput)
    
    phone = forms.CharField(label='phone',max_length=11,
        validators=[phone_validate,],
        error_messages={'required': u'邮箱不能为空'},
        widget=forms.TextInput(attrs={'class': "form-control",
                             'placeholder': u'手机号码'}),)
    email = forms.EmailField(error_messages={'required': u'邮箱不能为空'},
        widget=forms.EmailInput,)
    password = forms.CharField(
        label='password',
        strip=False,
        widget=forms.PasswordInput,
    )

    confirmpassword = forms.CharField(
        label='confirmpassword',
        strip=False,
        widget=forms.PasswordInput,
    )
    