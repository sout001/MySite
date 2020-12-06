from django.contrib import admin
from study.models import BaseModel, User


class BaseAdmin(admin.ModelAdmin):
    exclude = ['create_time', 'update_time', 'delete_time']
    list_per_page = 10


@admin.register(User)
class UserAdmin(BaseAdmin):
    verbose_name = "用户"
    list_display = ['id', 'user_id', 'user_name', 'user_pwd', 'user_phone', 'user_email', 'real_name', 'user_sex']


admin.site.site_header = "案例管理后台"
admin.site.site_title = '案例管理后台'
admin.site.index_title = '案例管理后台'
