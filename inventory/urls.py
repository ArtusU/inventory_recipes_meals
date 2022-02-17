from django.contrib import admin
from django.urls import path, include

from accounts.views import (
    login_view,
    logout_view,
    register_view
)

from articles.views import (
    article_search_view,
    article_create_view,
    article_detail_view
)

from .views import home_view

urlpatterns = [
    path('', home_view),
    
    path('admin/', admin.site.urls),
    
    path('pantry/recipes/', include('recipes.urls')),
    
    path('articles/', include('articles.urls')),
    
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    
]
