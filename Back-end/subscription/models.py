from django.db.models import *
from django.utils.timezone import now
from os import path

# Create your models here.

class Category(Model):
    title = CharField(max_length=255)
    is_adult = BooleanField()
    created_at = DateTimeField("Create Date", auto_now_add=True)
    description = TextField(blank=True)

    def __str__(self):
        return self.title
    

class Tag(Model):
    title = CharField(max_length=255)
    created_at = DateTimeField("Create Date", auto_now_add=True)
    discription = TextField(blank=True)

    def __str__(self):
        return self.title


class UserStatus(Model):
    status = CharField(unique=True, max_length=255)
    created_at = DateTimeField("Create Date", auto_now_add=True)
    discription = TextField(blank=True)

    def __str__(self):
        return self.status
    

class User(Model):
    tag = ManyToManyField(Tag, through='UserTagMap')
    user_status = OneToOneField(UserStatus, on_delete=SET(0))
    username = CharField(unique=True, max_length=255)
    password = CharField(max_length=255)
    email = EmailField(max_length=255)
    wallet_address = CharField("Wallet Address", max_length=255)
    created_at = DateTimeField("Create Date", auto_now_add=True)
    last_login = DateTimeField("Last Login", default=now)
    like = PositiveBigIntegerField()
    view = PositiveBigIntegerField()

    def update_last_login(self):
        self.last_login = now()
        self.save()

    def __str__(self):
        return f'{self.username} {self.user_status} {self.email} {self.like} {self.view}'

    class Meta:
        unique_together = ('email', 'wallet_address')


class Content(Model):
    category = ManyToManyField(Category, through='ContentCategoryMap')
    tag = ManyToManyField(Tag, through='ContentTagMap')
    user = ForeignKey(User, on_delete=SET(0), related_name='contents')
    title = CharField(max_length=255)
    discription = TextField(blank=True)
    created_at = DateTimeField("Create Date", auto_now_add=True)
    updated_at = DateTimeField("Update Date", auto_now=True)
    like = PositiveBigIntegerField()
    view = PositiveBigIntegerField()

    def __str__(self):
        return f'{self.title} {self.like} {self.view}'


class Repository(Model):
    content = ForeignKey(Content, on_delete=CASCADE, related_name='repositories')
    file_format = CharField("File Format", max_length=7)
    is_video = BooleanField()
    is_document = BooleanField()
    created_at = DateTimeField("Upload Date", auto_now_add=True)
    description = TextField(blank=True)
    
    def file_path_and_extention(instance, filename):
        file_extension = path.splitext(filename)[1][1:].upper()
        instance.file_format = file_extension
        return f'uploads/{instance.content.user_id}/{filename}'

    def __str__(self):
        return f'{self.file} {self.is_video} {self.is_document}'
    
    file = FileField(upload_to=file_path_and_extention)


class Subscribe(Model):
    subscriber = ForeignKey(User, on_delete=CASCADE, related_name='subscribers')
    subscription = ForeignKey(User, on_delete=CASCADE, related_name='subscriptions')
    created_at = DateTimeField("Subscribe Date", auto_now_add=True)

    def __str__(self):
        return f'{self.subscriber} {self.subscription}'

    class Meta:
        unique_together = ('subscriber', 'subscription')


class CommentStatus(Model):
    status = CharField(unique=True, max_length=255)
    created_at = DateTimeField("Create Date", auto_now_add=True)
    description = TextField(blank=True)

    def __str__(self):
        return self.status


class Comment(Model):
    user = ForeignKey(User, on_delete=SET(0), related_name='comments')
    content = ForeignKey(Content, on_delete=CASCADE, related_name='comments')
    comment_status = OneToOneField(CommentStatus, on_delete=SET(0), related_name='comments')
    title = CharField(max_length=255)
    body = TextField()
    created_at = DateTimeField("Create Date", auto_now_add=True)
    like = PositiveBigIntegerField()

    def __str__(self):
        return f'{self.title} {self.user} {self.comment_status} {self.like}'


class ContentCategoryMap(Model):
    content = ForeignKey(Content, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)
    created_at = DateTimeField("Create Date", auto_now_add=True)


class ContentTagMap(Model):
    content = ForeignKey(Content, on_delete=CASCADE)
    tag = ForeignKey(Tag, on_delete=CASCADE)
    created_at = DateTimeField("Create Date", auto_now_add=True)


class UserTagMap(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    tag = ForeignKey(Tag, on_delete=CASCADE)
    created_at = DateTimeField("Create Date", auto_now_add=True)
