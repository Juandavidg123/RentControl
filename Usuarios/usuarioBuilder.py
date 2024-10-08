from django.contrib.auth.models import User

class usuarioBuilder:
    def __init__(self):
        self.__usuario = User()
    
    def set_username(self, username):
        self.__usuario.username = username
        return self
    
    def set_password(self, password):
        self.__usuario.password = password
        return self
    
    def build(self):
        return User.objects.create_user(username=self.__usuario.username, password=self.__usuario.password)