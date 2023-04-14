from django.contrib import admin
from .models import Home, Snabbfakta, Summary_om_oss, Intervju


class HomeAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class Summary_om_ossAdmin(admin.ModelAdmin):
    list_display = ("titel", "summary")


class SnabbfaktaAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "head_quote", "last_updated", "quote", "quote_sayer")


class IntervjuAdmin(admin.ModelAdmin):
    list_display = ("titel", "front", "auther")


admin.site.register(Home, HomeAdmin)
admin.site.register(Summary_om_oss, Summary_om_ossAdmin)
admin.site.register(Snabbfakta, SnabbfaktaAdmin)
admin.site.register(Intervju, IntervjuAdmin)
