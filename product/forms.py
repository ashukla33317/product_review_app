from django  import forms

class NewProductForm(forms.Form):
    product_name=forms.CharField(max_length=30)
    description=forms.CharField(widget=forms.Textarea())
    price=forms.IntegerField()


choices = [('1', '1'), ('2', '2'),('3','3'),('4','4'),('5','5')]
class NewReviewform(forms.Form):
    rating = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))