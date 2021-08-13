from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class AccountManager(BaseUserManager):
	def create_user(self, first_name, last_name, email, phone, password):
		if not email:
			raise ValueError('Email can\'t be empty')
		if not first_name:
			raise ValueError('first name can\'t be empty')

		username = email.split('@')[0]

		user = self.model(
			first_name=first_name, last_name=last_name,
			username=username, email=email, phone=phone)

		if password is not None:
			user.set_password(password)
		else:
			raise ValueError('Password Cannot be None')

		user.save(using=self._db)
		return user

	def create_superuser(self, first_name, last_name, email, password=None):
		if not email:
			raise ValueError('Email can\'t be empty')
		if not first_name:
			raise ValueError('first name can\'t be empty')

		username = email.split('@')[0]

		user = self.model(
			first_name=first_name, last_name=last_name,
			username=username, email=email)
		if password is not None:
			user.set_password(password)
		user.is_active = True
		user.is_staff = True
		user.is_superuser = True
		user.is_admin = True

		user.save(using=self._db)

		return user


class Account(AbstractBaseUser):
	# Basic info
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50, unique=True)  # username field
	username = models.CharField(max_length=12, unique=True)
	phone = models.CharField(max_length=12, null=True)
	
	# Address
	apartment = models.CharField(max_length=100, null=True)
	street = models.CharField(max_length=100, null=True)
	pincode = models.CharField(max_length=6, null=True)
	city = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=100, null=True)
	country = models.CharField(max_length=100, null=True)

	# Required
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(auto_now_add=True)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False) 

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects = AccountManager()


	def full_name(self):
		return f'{self.first_name} {self.last_name}'

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def __str__(self):
		return self.email

	def has_module_perms(self, add_label):
		return True



