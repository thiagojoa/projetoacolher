from django.db import models


class Tenant(models.Model):
    """"""
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"name: {self.name} - subdomain-prefix: {self.subdomain_prefix}"



class TenantAwareModel(models.Model):
    """"""
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True