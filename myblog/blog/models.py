from django.db import models


# Create your models here.

class BlogManage(models.Manager):
    """自定义博客模型管理类"""

    def blog_click_num(self):
        """获得点击量前四的博客"""
        # 获取以点击数倒序排列并获得前四条
        blog_click = Blog.objects.all().order_by('-click_nums')
        blog_click4 = blog_click[:5]
        return blog_click4



class TagManage(models.Manager):
    """自定义博客标签管理类"""

    def tag_blogs(self, tag_num):
        """获取一个标签下的所有博客信息"""
        blogs = Blog.objects.filter(tag__id=tag_num)
        return blogs


class CategoryManage(models.Manager):
    """自定义文章分类管理器"""

    def cat_blogs(self, cat_num):
        """获得标签下的所有博客"""
        blogs = Blog.objects.filter(category__id=cat_num)

        return blogs


class Category(models.Model):
    """文章分类"""
    name = models.CharField(verbose_name='文章分类', max_length=100, unique=True)

    objects = CategoryManage()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """文章分类"""
    name = models.CharField(verbose_name='文章标签', max_length=50, unique=True)

    objects = TagManage()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_tag'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    """博客类"""
    title = models.CharField(verbose_name='标题', max_length=100, unique=True)
    abstract = models.CharField(verbose_name='摘要', max_length=300, null=True, default='', blank=True)
    img = models.ImageField(upload_to='images/', default='', null=True, blank=True)
    content = models.TextField(verbose_name='正文', default='')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='修改时间')
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, verbose_name='博客分类')
    tag = models.ManyToManyField(Tag, verbose_name='博客标签')

    objects = BlogManage()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_blog'
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name
