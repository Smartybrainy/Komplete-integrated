from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

HOME_STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class IndexDesign(models.Model):
    title = models.CharField(max_length=30)
    content = RichTextField()
    home_video_url = EmbedVideoField(blank=True, null=True)
    image = models.ImageField(upload_to='home_media', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=HOME_STATUS, default=0)
    timestamp = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Index Design Content'

    ordering = ['-timestamp']