from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

def index(request):
    articles = Article.objects.all()  # --- 2
    params = {  # --- 3
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)  # --- 4

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content)
        article.save()
        messages.success(request,"Blog creado con éxito.")  # añadir
        return redirect('index')
    else:
        params = {
            'form': ArticleForm(),
        }
        return render(request, 'blog/create.html', params)

def detail(request, article_id):  # --- 1
    article = Article.objects.get(id=article_id)  # --- 2
    params = {
        'article': article,  # Pasamos el artículo al contexto para la plantilla
    }
    return render(request, 'blog/detail.html', params)  # Renderizamos la plantilla 'detail.html'

def edit(request, article_id):
    # Obtener el artículo por su id
    article = Article.objects.get(id=article_id)
    
    # Verificar si el método de la solicitud es POST (cuando se envían datos)
    if request.method == 'POST':
        # Actualizar los campos del artículo con los datos enviados en el formulario
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()  # Guardar los cambios
        return redirect('detail', article_id)  # Redirigir a la vista de detalle del artículo editado
    
    else:
        # Si no es POST, se muestra el formulario con los datos actuales del artículo
        form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
        })
        params = {
            'article': article,  # Pasar el artículo a la plantilla
            'form': form,  # Pasar el formulario con los datos iniciales
        }
        return render(request, 'blog/edit.html', params)  # Renderizar la plantilla para editar

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    else:
        params = {
            'article': article,
        }
        return render(request, 'blog/delete.html', params)