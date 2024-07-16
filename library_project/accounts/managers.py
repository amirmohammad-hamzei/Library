from django.contrib.auth.models import BaseUserManager
import re


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password, username):
        regex_pattren = r'^09\d{9}$'
        match = re.match(regex_pattren, phone_number)
        if not phone_number or not match:
            raise ValueError("Enter Your Phone Number Correctly")

        user = self.model(phone_number=phone_number, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
