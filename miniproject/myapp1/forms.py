from django.forms import ModelForm, Textarea, CharField
from myapp1.models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('ActivityName','ActivityType','ActivityDate','ActivityDesc')
        widgets = {
            'ActivityDesc': Textarea(attrs={'cols': 80, 'rows': 10,'class':'myclass'})
        }

#class PhoneNoForm(ModelForm):
#    class Meta:
#        model = PhoneNo
