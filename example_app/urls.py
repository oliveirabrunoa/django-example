from django.conf.urls import url
from . import views

app_name = 'example_app'

urlpatterns = [
    url(r'^teste_requisicao$', views.teste_requisicao, name='teste_requisicao'),
]
