from django.contrib import admin
from .models import ComputerVarity, ComputerReview, Store, ComputerCertificate

# Register your models here.
class ComputerReviewInline(admin.TabularInline):
    model = ComputerReview
    extra = 1 
    
class ComputerVarityAdmin(admin.ModelAdmin):
    inlines = [ComputerReviewInline]
    list_display = ('name', 'type', 'date_added')
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('computer_varieties',)
    
class ComputerCertificateAdmin(admin.ModelAdmin):
    list_display = ('computer', 'certificate_number', 'issue_date', 'valid_until')

admin.site.register(ComputerVarity, ComputerVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ComputerCertificate, ComputerCertificateAdmin)