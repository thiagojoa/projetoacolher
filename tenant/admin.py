from django.contrib import admin
from .models import Tenant, Ong, Dirigente, Fornecedor


admin.site.register(Tenant)
admin.site.register(Ong)
admin.site.register(Dirigente)
admin.site.register(Fornecedor)