from django.contrib import admin
from .models import Executor, Authoring, Order, Ordering, Tag, Review, Ticket, Message, Service, Customer

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Executor)
admin.site.register(Authoring)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Ticket)
admin.site.register(Ordering)
admin.site.register(Message)
admin.site.register(Service)

