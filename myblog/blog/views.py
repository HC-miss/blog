from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from blog.models import Blog, Tag, Category


# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.all().order_by('-id')  # 获取对象并倒序排列
        num = request.GET.get('num', 1)  # 获取页码并默认为一
        num = int(num)
        # 封装分页器
        paginator = Paginator(blog, 4)
        try:
            t_pre_page = paginator.page(num)  # 获取当前页码的记录
        except PageNotAnInteger:  # 如果用户输入的页码不是整数时,显示第1页的内容
            t_pre_page = paginator.page(1)
        except EmptyPage:  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
            t_pre_page = paginator.page(paginator.num_pages)
        # 传回热门点击数据
        blog_click_nums = Blog.objects.blog_click_num()
        # 获取全部的标签
        tags = Tag.objects.all()

        return render(request, 'blog/index.html', {
            't_pre_page': t_pre_page,
            'blog_click_nums': blog_click_nums,
            'tags': tags,
        })


def showtags(request, tag_num):
    """展示所有标签下的博客"""

    # 获取一个标签下的全部的博客集合
    tag_blogs = Tag.objects.tag_blogs(tag_num)

    return render(request, 'blog/showtags.html', {'t_pre_page': tag_blogs,

                                                  })


def showcats(request, cat_num):
    """展示分类下的博客"""

    # 获得一个分类下的所有博客标签
    cat_blogs = Category.objects.cat_blogs(cat_num)

    return render(request, 'blog/showcats.html', {'t_pre_page': cat_blogs,
                                                  })


def view(request, post_num):
    # 获取前端参数并获取数据库响应对象
    post = Blog.objects.get(id=post_num)
    # 获取这个id的上一条数据，比这个ID大的上一条数据
    on_post = Blog.objects.filter(id__lt=post_num).order_by('id').last()
    # 获取这个id的下一条数据，比这个ID小的的第一条数据
    in_post = Blog.objects.filter(id__gt=post_num).order_by('id').first()
    # 每请求一次数据库中点击数增加一
    post.click_nums += 1
    post.save()

    return render(request, 'blog/view.html', {'post': post,
                                              'on_post': on_post,
                                              'in_post': in_post,
                                              })


def search(request):
    """处理搜索数据"""
    from haystack.query import SearchQuerySet
    from haystack.query import SQ
    # 获取搜索框的数据
    search_words = request.GET.get('s', '')
    # 搜索匹配文章名和内容
    search_blogs = SearchQuerySet().filter(SQ(title=search_words) | SQ(content=search_words))
    sea_blogs = []
    for s_b in search_blogs:
        sea_blogs.append(s_b.object)

    return render(request, 'blog/search.html', {'t_pre_page': sea_blogs})


def archive(request):
    """归档详情页"""
    # 获得参数
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    print(year, month)
    # 查询并返回查询集
    arc_blog = Blog.objects.filter(modify_time__year=year, modify_time__month=month).order_by('-modify_time')

    return render(request, 'blog/showarchive.html', {'arc_blog': arc_blog})
