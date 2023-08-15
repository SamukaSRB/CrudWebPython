from django.db import models

# Create your models here.

class Produtos(models.Model):
    idProdut = models.AutoField(primary_key=True)
    eanProdut = models.CharField(max_length=100, verbose_name="Ean")
    nomProdut = models.CharField(max_length=100, verbose_name="Nome")
    desProdut = models.CharField(max_length=100, verbose_name="Descricão")
    preProdut = models.FloatField( verbose_name="Preco")
  
    imgProdut = models.ImageField(upload_to='images/',verbose_name="Imagem",null=True)
    
    def __str__(self):
        fila = "Ean: " + self.eanProdut + " - " + "Nome: " + self.nomProdut + " - " + "Descricao: " + self.desProdut + " - " + "Preco: " +str(self.preProdut) 
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imgProdut.storage.delete(self.imgProdut.name)
        super().delete()
    
