from abc import ABC, abstractmethod

class Diccionario(ABC):
    
    @abstractmethod
    def registrar_usuario(self, nombre: str, email: str, contraseña: str)->bool:
        pass
    
    @abstractmethod
    def verificar_usuario(self, email: str, contraseña: str, Rol: str)->bool:
        pass