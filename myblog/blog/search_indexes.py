from haystack import indexes

from blog.models import Blog


# 注意格式
class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 给title,content设置索引
    title = indexes.NgramField(model_attr='title')
    abstract = indexes.NgramField(model_attr='abstract')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
