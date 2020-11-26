from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager) :
    use_in_migrations = True

    def create_user(self, id, name, student_id, email, password):
        if not email or name or student_id :
            raise ValueError('must have user email')
        user = self.model(
            id=id,
            name=name,
            student_id=student_id,
            email=self.normalize_email(email)
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, name, email, password):
        # user = self.create_user(
        #     name=name,
        #     student_id=student_id,
        #     email=self.normalize_email(email)
        # )
        user = self.model(
            id=id,
            name=name,
            student_id=student_id,
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
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

    @property
    def is_staff(self):
        return self.is_superuser


