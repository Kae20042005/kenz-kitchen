from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "category", "price", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_feelings(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)

    def clean_mood(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)

    def clean_feelings(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)