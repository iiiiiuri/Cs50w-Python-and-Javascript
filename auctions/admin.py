from django import forms
from django.contrib import admin
from .models import User , AuctionListing , Bid , Comment

class UserAdminForm(forms.ModelForm):
    image_upload = forms.FileField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        exclude = ['image_upload'] 

class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm

    def save_model(self, request, obj, form, change):
        if 'image_upload' in request.FILES:
            obj.image_blob = request.FILES['image_upload'].read()
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)