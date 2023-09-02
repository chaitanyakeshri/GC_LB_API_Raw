from django.urls import path 
from.import views

urlpatterns = [
path('', views.apiOverview,  name = "Api - Overview"), 
path('get/', views.getData,  name = "Article - Get"),
path('add/',views.addArticle,name = "Article - Add"),
path('update/<str:pk>/',views.UpdateArticle ,  name = "Article - Update"),
path('delete/<str:pk>/',views.DeleteArticle ,  name = "Article - Delete"),

##########################################################################
path('types', views.Types_Of_GCs ,  name = "Types Of GC"),
path('cult', views.Cult_GC ,  name = "Cult GC"),
path('tech', views.Tech_GC ,  name = "Tech GC"),
path('sports', views.Sports_GC ,  name = "Sports GC"),
path('subgclb/<str:gc_ID>/', views.Sub_GC_LB),

path('typegclb/<str:type>/', views.Type_GC_LB),
path('gclb/', views.GC_LB),
path('post_GC/', views.add_GC),
path('update_score/', views.update_Points),

]