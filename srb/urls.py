from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path('painel', views.painel, name='painel'), 
    path('produtos', views.produtos, name='produtos'),
    path('produtos/cadastro_de_produto', views.cad_produto, name='cad_produto'),   
    path('produtos/editar_produto/<int:idProdut>', views.editar_produto, name='editar_produto'),
    path('produtos/deletar_produto/<int:idProdut>',views.deletar_produto, name='deletar_produto'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)