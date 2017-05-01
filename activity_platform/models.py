from django.db import models
from django.utils import timezone


from django.db import models
from django.utils import timezone

class Post(models.Model):
    活動名稱 = models.CharField(default="建議最多十四字", max_length=15)
    副標題 = models.CharField(default="建議最多二十五字", blank=True, max_length=30)
    #圖片 = models.TextField(default=".jpg")
    圖片 = models.ImageField(default="back.png", upload_to='upload/')
    簡介 = models.TextField(default="簡介你的活動(建議最多三百二十五字)", max_length=1000)
    開始日期與時間 = models.DateTimeField(blank=True, null=True)
    結束日期與時間 = models.DateTimeField()
    地點 = models.CharField(blank=True, max_length=200)
    對象 = models.TextField(blank=True, max_length=200)
    費用 = models.CharField(blank=True, max_length=200)
    人數限制 = models.TextField(blank=True, max_length=200)
    報名死線 = models.DateTimeField(blank=True, null=True)
    聯絡資訊 = models.TextField(default="例如活動專頁等")
    類型 = models.CharField(max_length=200,blank=True)
    標籤 = models.CharField(max_length=200,blank=True)
    詳細地點 = models.TextField(max_length=200,blank=True)
    詳細費用 = models.TextField(max_length=200,blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.活動名稱
		
class Like(models.Model):
    user = models.CharField(max_length=20, blank=True)
    #user = models.ManyToManyField(User)
    post = models.ManyToManyField(Post)
    
    def __str__(self):
        return self.user