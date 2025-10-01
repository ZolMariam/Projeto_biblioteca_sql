from django.db import models

# Create your models here.
    
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    biografia = models.TextField()
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria
    
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField(null=True,blank=True)
    autores = models.ManyToManyField(Autor, related_name="Livro")
    categorias = models.ManyToManyField(Categoria, related_name="Livro")
    
    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    numero_identificacao = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    data_devolucao_limite = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos", null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="emprestimos")
    
    def __str__(self):
        return f"{self.livro.titulo} → {self.usuario.nome} → {self.data_emprestimo}"
    
    