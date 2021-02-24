from django.test import TestCase
from .models import Post
# Create your tests here.
class PostTest(TestCase):

    def setUp(self):

        instance = Post.objects.create(title='django', description='....')
        instance.save()

        instance = Post.objects.create(title='Angular', description='....')
        instance.save()

    def test_for_post(self):
        print(Post.objects.all())
        print(Post.objects.filter(title='django'))
        print(Post.objects.filter(title__icontains='Django'))
        #print('hola')
        #print(Post.objects.filter(created_at__range=['2021-01-01', '2021-02-01']))
        instance = Post.objects.get(pk=1)
        instance.title = 'Django REST'
        instance.save()

        print(Post.objects.all())
        instance.delete()
        print(Post.objects.all())
