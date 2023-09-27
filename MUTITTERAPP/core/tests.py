from django.test import TestCase
from .models import Tag,Kling
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your tests here.

class TagTestCase(TestCase):
    def setUp(self) -> None:
        self.first_tag =Tag.objects.create(name= "Standard")
    
    
    def test_tag_str(self):
        self.assertEqual(str(self.first_tag),self.first_tag.name)
        
    
    def test_tag_name(self):
        self.assertEqual("Standard",self.first_tag.name)
    
    def tearDown(self) -> None:
        del self.first_tag
    
class KlingTestCase(TestCase):  
    def setUp(self) -> None:
        self.user=User.objects.create(username ="varsik72",email ="varsikharutyunyan72gmail.com",pasword="usmasvar11")
        self.first_kling =Kling.objects.create( title = "Test1",
                                                text= "text1",
                                                kling_type="1",
                                                user=self.user)
        
    # def test_kling_str(self):
    #     pass   
        
    # def test_kling_name(self):
    #     pass
        
    def tearDown(self) -> None:
        del self.user
        del self.first_kling
    