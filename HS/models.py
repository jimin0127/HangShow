from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from HangShow import settings

# assignment model
class Assignment(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateField()
    endline = models.DateField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return '{}:{}'.format(self.title, self.author)

class class_2_1(models.Model):
    ban = "2-1"
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateField()
    endline = models.DateField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return '{}:{}'.format(self.title, self.author)

class class_2_2(models.Model):
    ban = "2-2"
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateField()
    endline = models.DateField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return '{}:{}'.format(self.title, self.author)


class class_2_3(models.Model):
    ban = "2-3"
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateField()
    endline = models.DateField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return '{}:{}'.format(self.title, self.author)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, student_id, email, password):
        if not email and name and student_id:
            raise ValueError('must have user email')
        user = self.model(
            name=name,
            student_id=student_id,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, name, student_id, email, password):
        user = self.create_user(
            name=name,
            student_id=student_id,
            email=self.normalize_email(email),
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    id = models.CharField(
        verbose_name=_('id'),
        max_length=20,
        null=False,
        primary_key=True
    )

    name = models.CharField(
        verbose_name=_('name'),
        max_length=5,
        null=False,
        unique=True
    )

    student_id = models.CharField(
        verbose_name=_('student_id'),
        max_length=4,
        null=False,
        unique=True
    )

    email = models.EmailField(
        verbose_name=_('email'),
        max_length=255,
        unique=True,

    )
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['student_id', 'email']

    def __str__(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.id

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_user_email(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser