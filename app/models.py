from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cnpj = models.CharField(max_length=100, null=False)
    forma_med_part = models.FloatField(null=True)
    mass_esp_apar = models.FloatField(null=True)
    poros_apar = models.FloatField(null=True)
    resist_int = models.FloatField(null=True)
    resist_comp = models.FloatField(null=True)
    resist_choq = models.FloatField(null=True)
    teor_frag = models.FloatField(null=True)
    mat_pulv = models.FloatField(null=True)
    torr_arg = models.FloatField(null=True)
    limit_m_u = models.FloatField(null=True)
    resist_desg = models.FloatField(null=True)
    dist_635 = models.FloatField(null=True)
    dist_500 = models.FloatField(null=True)
    dist_380 = models.FloatField(null=True)
    dist_250 = models.FloatField(null=True)
    dist_190 = models.FloatField(null=True)
    dist_127 = models.FloatField(null=True)