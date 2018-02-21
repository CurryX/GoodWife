from django import forms
from pos.models import Member

text_widget = forms.TextInput(attrs={'class': 'form-control'})
number_widget = forms.NumberInput(attrs={'class': 'form-control'})


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'phone', 'balance', 'discount', 'comment')
        widgets = {
            'name': text_widget,
            'phone': text_widget,
            'balance': number_widget,
            'discount': number_widget,
            'comment': text_widget,
        }
        labels = {
            'name': '姓名',
            'phone': '电话',
            'balance': '卡余额',
            'discount': '折扣（%）',
            'comment': '备注',
        }
