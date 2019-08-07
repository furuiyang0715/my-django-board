from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        # 可以测试Django是否在请求的URL的时候返回了正确的视图函数。这也是一个有用的测试，因为随着开发的进展，
        # 您会发现urls.py模块可能变得非常庞大而复杂。URL conf 全部是关于解析正则表达式的。
        # 有些情况下有一个非常宽容的URL（译注：本来不应该匹配的，却因为正则表达式写的过于宽泛而错误的匹配了），
        # 所以Django最终可能返回错误的视图函数。
        # resolve函数。Django使用它来将浏览器发起请求的URL与urls.py模块中列出的URL进行匹配。
        # 该测试用于确定URL / 返回 home 视图
        view = resolve('/')
        self.assertEquals(view.func, home)
