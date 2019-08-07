from django.conf.urls import url
from django.contrib import admin

from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # 用户注册
    url(r'^signup/$', accounts_views.signup, name='signup'),
    # 用户注销 这是一个Django的“基于类”的视图
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
