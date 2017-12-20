from django.conf.urls import url
from core.views import controle


urlpatterns = [
    url(r'^$', controle.inicio, name="inicio"),
    url(r'^delete/(?P<pk>\d+)/$', controle.delete_conta, name= 'delete'),
    url(r'atualizar_conta/(?P<pk>\d+)/$', controle.atualizar_conta, name='atualizar_conta'),
    url(r'conta_atualizada/$', controle.conta_atualizada, name='conta_atualizada'),
    url(r'^nova_conta/$', controle.nova_conta, name="nova_conta"),
    url(r'^conta_criada/$', controle.conta_criada, name="conta_criada"),
    url(r'^lista_categoria$',controle.lista_categoria, name="lista_categoria"),
    url(r'^nova_categoria/$', controle.novaCategoria, name="nova_categoria"),
    url(r'^categoria_criada/$', controle.categoria_criada, name="categoria_criada"),
    url(r'^editar_categoria/(?P<pk>\d+)$', controle.editar_categoria, name="editar_categoria"),
    url(r'^categoria_editada/(?P<pk>\d+)$', controle.categoria_editada, name="categoria_editada"),
    url(r'^deletar_categoria/(?P<pk>\d+)$', controle.deletar_categoria, name="deletar_categoria"),

]