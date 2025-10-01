from django.contrib import admin
from .models import Autor, Livro, Categoria, Usuario, Emprestimo
# Register your models here.

admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Emprestimo)
