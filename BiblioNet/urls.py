from django.urls import path
from .models import Autor, Livro, Categoria, Usuario, Emprestimo

urlpatterns = [
    path('Autor/', Autor),
    path('Livro/', Livro),
    path('Categoria/', Categoria),
    path('Usuario/', Usuario),
    path('Emprestimo/', Emprestimo)
]