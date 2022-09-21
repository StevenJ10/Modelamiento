
from .BotTelegram import getEClassifier, eClassifiers
from .BotTelegram import name, nsURI, nsPrefix, eClass
from .BotTelegram import App, Usuario, Paquete, Vuelo, Factura


from . import BotTelegram

__all__ = ['App', 'Usuario', 'Paquete', 'Vuelo', 'Factura']

eSubpackages = []
eSuperPackage = None
BotTelegram.eSubpackages = eSubpackages
BotTelegram.eSuperPackage = eSuperPackage

App.Users.eType = Usuario
Usuario.Aplicacion.eType = App
Usuario.Aplicacion.eOpposite = App.Users
Usuario.Packages.eType = Paquete
Paquete.Flight.eType = Vuelo
Paquete.User.eType = Usuario
Paquete.User.eOpposite = Usuario.Packages
Paquete.factura.eType = Factura
Vuelo.Package.eType = Paquete
Vuelo.Package.eOpposite = Paquete.Flight
Factura.Packs.eType = Paquete
Factura.Packs.eOpposite = Paquete.factura

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
