from django.contrib import admin
from .models import Board

# 在后台管理系统中注册 Board
admin.site.register(Board)