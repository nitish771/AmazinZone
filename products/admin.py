from django.contrib import admin

from .models import Variation

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_type', 'variation_value', 'active')
    list_filter = ('active', 'variation_type', 'variation_value')
    list_editable = ('active',)

admin.site.register(Variation, VariationAdmin)