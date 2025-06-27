from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["descricao"]
        indexes = [
            models.Index(fields=["descricao"]),
        ]