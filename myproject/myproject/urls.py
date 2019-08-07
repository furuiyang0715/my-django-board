from django.conf.urls import url
from django.contrib import admin

from boards import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^$', views.BoardListView.as_view(), name='home'),

    # 个人账户
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),

    # 用户注册
    url(r'^signup/$', accounts_views.signup, name='signup'),
    # 用户登录
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # 用户注销 这是一个Django的“基于类”的视图
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),

    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),

    # 查看回复与评论详情的路由
    # pk用于唯一标识版块（Board），topic_pk用于唯一标识该回复来自哪个主题
    # url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),

    # 回复主题
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),

    # 编辑回复
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),

    # 与重置密码相关的一系列视图均是内置的
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

]
