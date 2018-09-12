from django.db import connection

from blog.models import Blog


def viewInfo(request):
    # 仅仅获得侧边的条目
    gitblogs = Blog.objects.all()[:8]
    return {'gitblogs': gitblogs}


def archive(request):
    """博文的归档功能"""
    cursor = connection.cursor()
    cursor.execute(
        "SELECT modify_time,COUNT('*') AS COUNT FROM t_blog GROUP BY DATE_FORMAT(modify_time,'%Y-%m') ORDER BY COUNT DESC")
    arc_posts =cursor.fetchall()
    return {'arc_posts': arc_posts}
