from django.urls import path, include
from . import views  # --- (1)

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista de inicio
    path('create', views.create, name='create'),  # Ruta para la vista de creación
    path('detail/<int:article_id>', views.detail, name='detail'),  # Ruta para la vista de detalles con un parámetro dinámico 'article_id'
    path('edit/<int:article_id>/', views.edit, name='edit'),  # Agregado el '/' al final
    path('delete/<int:article_id>', views.delete, name='delete'),
    path('__debug__/', include('debug_toolbar.urls')),
]