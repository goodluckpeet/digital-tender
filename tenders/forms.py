from django import forms
from users.models import Bid, Tender


class TenderCreationForm(forms.ModelForm):

    class Meta:
        model=Tender
        fields = ['title','description','documents', 'closing_date',]

class TenderUpdateForm(forms.ModelForm):

    class Meta:
        model = Tender
        fields = ['closing_date', 'status']

class BidCreateForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ['documents','company','tender']

class BidUpdateForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ['awarded']
