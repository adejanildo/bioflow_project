from django.db import models
from django.conf import settings

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponível'),
        ('in_use', 'Em Uso'),
        ('maintenance', 'Em Manutenção'),
        ('broken', 'Com Defeito'),
        ('inactive', 'Inativo'),
    ]
    name = models.CharField('Nome', max_length=200)
    model = models.CharField('Modelo', max_length=200)
    serial_number = models.CharField('Número de Série', max_length=100, unique=True)
    manufacturer = models.CharField('Fabricante', max_length=200)
    location = models.CharField('Localização', max_length=200)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='available')
    acquisition_date = models.DateField('Data de Aquisição', null=True, blank=True)
    maintenance_date = models.DateField('Próxima Manutenção', null=True, blank=True)
    description = models.TextField('Descrição', blank=True)
    manual = models.FileField('Manual', upload_to='manuals/', null=True, blank=True)
    image = models.ImageField('Foto', upload_to='equipments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} — {self.model}"

class EquipmentFailure(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='failures', verbose_name='Equipamento')
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Reportado por')
    description = models.TextField('Descrição da Falha')
    reported_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField('Resolvido', default=False)
    resolved_at = models.DateTimeField('Resolvido em', null=True, blank=True)

    class Meta:
        verbose_name = 'Falha de Equipamento'
        ordering = ['-reported_at']

    def __str__(self):
        return f"Falha: {self.equipment.name} em {self.reported_at.strftime('%d/%m/%Y')}"
