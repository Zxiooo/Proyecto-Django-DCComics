from django.urls import path, re_path
from django.contrib import admin
from moduloPeliculas import views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from moduloPeliculas.views import atencion_al_cliente
from online.views import Index,Inicio,RegisterView,LoginView,ViewRespuestas, catalogoPeliculas, logout_view
from administracion.views import IndexAdmin,BorrarPregunta,GestionUsuarios,EliminarUsuario,ModificarPregunta
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.PeliculaListView, name='pelicula-list'),
    path('agregarpelicula/', views.agregar_pelicula, name='agregarpelicula'),
    path('<int:id>/', views.pelicula_detail, name='pelicula-detail'),
    path('editar/<int:id>/', views.editar_pelicula, name='editar-pelicula'),
    path('eliminar/<int:id>/', views.eliminar_pelicula, name='eliminar-pelicula'),
    path('gestionpeliculas/', views.PeliculaListCrud, name='gestion_peliculas'),
    path('atencion-al-cliente/', atencion_al_cliente, name='atencion-al-cliente'),
    
    path('Callcenter/', Index, name='AtencionCliente'),
    path('Administracion/', IndexAdmin),
    path('Login/', LoginView.as_view(), name='Login'),
    path('Register/', RegisterView.as_view(), name='Register'),
    path('Inicio/<int:id>', Inicio),
    path('Logout/', logout_view, name='Logout'),
    path('Respuesta/<int:idUser>/<int:idPregunta>', ViewRespuestas),
    path('BorrarPregunta/<int:idUser>/<int:idPregunta>', BorrarPregunta),
    path('GestionUsuarios/', GestionUsuarios),
    path('EliminarUsuario/<int:idUser>', EliminarUsuario),
    path('ModificarPregunta/<int:idPregunta>', ModificarPregunta),
    path('Catalogo/', catalogoPeliculas, name='catalogoPeliculas'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


