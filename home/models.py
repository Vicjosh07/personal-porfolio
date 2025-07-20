from django.db import models
from PIL import Image

# Create your models here.
class Intro(models.Model):
    headline = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='personal/', blank=False, null=False)
    about = models.TextField()
    resume = models.FileField(upload_to='personal/', blank=False, null=False)

    def __str__(self):
        return 'Intro Section'
    
    class Meta:
        verbose_name = "1. Intro"
        verbose_name_plural = "1. Intro"

    
class Expertise(models.Model):
    expertise = models.CharField(max_length=200)

    class Meta:
        verbose_name = "2. Expertise"
        verbose_name_plural = "2. Expertise"

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def date_range(self):
        if self.is_current:
            return f"{self.start_date.strftime('%b %Y')} - Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        return f"{self.start_date.strftime('%b %Y')} - Unknown"

    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        verbose_name = "3. Experience"
        verbose_name_plural = "3. Experience"

class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def date_range(self):
        if self.is_current:
            return f"{self.start_date.strftime('%b %Y')} - Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        return f"{self.start_date.strftime('%b %Y')} - Unknown"

    def __str__(self):
        return f"{self.degree} from {self.institution}"
    
    class Meta:
        verbose_name = "4. Education"
        verbose_name_plural = "4. Education"

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    link = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # project thumbnail models images with different sizes
    projectImg_small = models.ImageField(upload_to='projects/small_img/', blank=False, null=False)
    projectImg_big = models.ImageField(upload_to='projects/big_img/', blank=False, null=False)
    projectImg_relative = models.ImageField(upload_to='projects/relative_img/', blank=False, null=False)
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['created_at']
        verbose_name = "5. Project"
        verbose_name_plural = "5. Projects"
    
class Certificates(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    # about company
    company_name = models.CharField(max_length=100, blank=False, null = True)
    type = models.CharField(max_length=100, blank=False, null=True)
    company_logo = models.ImageField(upload_to='certificates/logo/', blank=False, null=True)
    #certificate thumbnail models images with different sizes
    certificateImg_big = models.ImageField(upload_to='certificates/big_img/', blank=False, null=True)

    certificate_url = models.URLField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.company_name}'
    
    class Meta:
        ordering = ['created_at']
        verbose_name = "6. Certificates"
        verbose_name_plural = "6. Certificates"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.certificateImg_big:
            img_path = self.certificateImg_big.path
            img = Image.open(img_path)

            max_width = 2200
            if img.width > max_width:
                # ratio = max_width / img.width
                new_size = (max_width, 1400)
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                img.save(img_path)