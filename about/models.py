from django.db import models


class About(models.Model):
    """
    Stores information about the site owner for the About Me page.
    """
    title = models.CharField(max_length=200)
    profile_image = models.ImageField(
        upload_to='about/', blank=True, null=True
    )
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About"
