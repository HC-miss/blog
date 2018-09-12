from django.contrib import admin

from blog.models import Category, Tag, Blog


# Register your models here.


class BlogManage(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )


admin.site.register(Blog, BlogManage)
admin.site.register(Tag)
admin.site.register(Category)
