from .forms import PropiedadesForm

class propiedadBuilder:
    def __init__(self):
        self.__propiedad = None
        
    def set_propiedad(self, data, usuario, instance=None):
        form = PropiedadesForm(data, instance=instance)
        if form.is_valid():
            self.__propiedad = form.save(commit=False)
            self.__propiedad.dueño = usuario
        return self
    
    def build(self):
        if self.__propiedad:
            self.__propiedad.save()
        return self.__propiedad
    
