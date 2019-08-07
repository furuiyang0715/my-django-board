from django.conf.urls import url
from django.contrib import admin

from boards import views
# 给 accounts 的 views 指定了别名，否则它会与boards 的views 模块发生冲突。
from accounts import views as accounts_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # 创建一个新的路由来实现用户的身份认证
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
