from django.db import models

CARGO_DIRIGENTE = (
    ('DIR', 'Dirigente'),
    ('VOL', 'Voluntário'),
    ('FRE', 'Freelancer'),
)

CAUSAS = (
    ("Social", "Causas Sociais"),
)


class Tenant(models.Model):
    """Esta classe modela a multitenancy adicionando subdomínios como identificador
    """
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"name: {self.name} - subdomain-prefix: {self.subdomain_prefix}"


class TenantAwareModel(models.Model):
    """Esta classe modela a multitenancy
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Ong(TenantAwareModel):
    """Esta classe modela as Ong's
    """
    nome = models.CharField(max_length=200)
    resumo = models.TextField()
    imagem = models.ImageField()
    endereco = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    causas = models.CharField(max_length=10, choices=CAUSAS, default=None)
    numero_beneficiaros = models.IntegerField()
    cnpj = models.CharField(unique=True, max_length=16, blank=True, null=True)
    is_active = models.BooleanField(default=True, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField()
    facebook_ong = models.URLField()
    descricao = models.TextField()

    class Meta:
        verbose_name = "Ong"
        verbose_name_plural = "Ong's"

    def __str__(self):
        return self.nome


class Dirigente(TenantAwareModel):
    """Esta classe modela os dirigentes
    """
    cargo = models.CharField(max_length=3, choices=CARGO_DIRIGENTE, default=None)


class Fornecedor(TenantAwareModel):
    """Esta classe modela os fonercedores
    """
    pass