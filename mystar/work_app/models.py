from django.db import models
from django.contrib.auth.models import AbstractUser



class Skill(models.Model):
    skill_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.skill_name


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'client'),
        ('freelancer', 'freelancer'),
    )
    role = models.CharField(choices=ROLE_CHOICES, default='client', max_length=32)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='user_avatars', null=True, blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'



class SocialNetwork(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users')
    name = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return f'{self.name}, {self.url}'



class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Project(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    budget = models.PositiveIntegerField()
    deadline = models.DateField()
    STATUS_CHOICES = (
        ('open', 'open'),
        ('in_progress', 'in_progress'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    )
    status = models.CharField(choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    skills_required = models.ManyToManyField(Skill)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='clients')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Offer(models.Model):
    project= models.ForeignKey(Project, on_delete=models.CASCADE, related_name='offers')
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    proposed_budget = models.IntegerField()
    proposed_deadline = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project}, {self.freelancer}'


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_written')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_received')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.project}, {self.reviewer}, {self.target}, {self.rating}'



