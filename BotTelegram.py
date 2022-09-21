"""Definition of meta model 'BotTelegram'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'BotTelegram'
nsURI = 'http://org.eclipse.example.BotTelegram'
nsPrefix = 'org.eclipse.example.BotTelegram'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class App(EObject, metaclass=MetaEClass):

    Name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    Users = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, Name=None, Users=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if Name is not None:
            self.Name = Name

        if Users:
            self.Users.extend(Users)


class Usuario(EObject, metaclass=MetaEClass):

    Nombre = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    Cedula = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    Telefono = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    Aplicacion = EReference(ordered=True, unique=True, containment=False, derived=False)
    Packages = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, Nombre=None, Cedula=None, Telefono=None, Aplicacion=None, Packages=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if Nombre is not None:
            self.Nombre = Nombre

        if Cedula is not None:
            self.Cedula = Cedula

        if Telefono is not None:
            self.Telefono = Telefono

        if Aplicacion is not None:
            self.Aplicacion = Aplicacion

        if Packages:
            self.Packages.extend(Packages)


class Paquete(EObject, metaclass=MetaEClass):

    IdPack = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    Ida = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    Vuelta = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    Aerolinea = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    NumAsientos = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    Precio = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    Flight = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    User = EReference(ordered=True, unique=True, containment=False, derived=False)
    factura = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, IdPack=None, Ida=None, Vuelta=None, Aerolinea=None, NumAsientos=None, Precio=None, Flight=None, User=None, factura=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if IdPack is not None:
            self.IdPack = IdPack

        if Ida is not None:
            self.Ida = Ida

        if Vuelta is not None:
            self.Vuelta = Vuelta

        if Aerolinea is not None:
            self.Aerolinea = Aerolinea

        if NumAsientos is not None:
            self.NumAsientos = NumAsientos

        if Precio is not None:
            self.Precio = Precio

        if Flight:
            self.Flight.extend(Flight)

        if User is not None:
            self.User = User

        if factura is not None:
            self.factura = factura


class Vuelo(EObject, metaclass=MetaEClass):

    Origen = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    Destino = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    DuracionMin = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    FechaIda = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    FechaVuelta = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    Package = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, Origen=None, Destino=None, DuracionMin=None, FechaIda=None, FechaVuelta=None, Package=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if Origen is not None:
            self.Origen = Origen

        if Destino is not None:
            self.Destino = Destino

        if DuracionMin is not None:
            self.DuracionMin = DuracionMin

        if FechaIda is not None:
            self.FechaIda = FechaIda

        if FechaVuelta is not None:
            self.FechaVuelta = FechaVuelta

        if Package is not None:
            self.Package = Package


class Factura(EObject, metaclass=MetaEClass):

    PrecioBase = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    ValorFinal = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    Packs = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, PrecioBase=None, ValorFinal=None, Packs=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if PrecioBase is not None:
            self.PrecioBase = PrecioBase

        if ValorFinal is not None:
            self.ValorFinal = ValorFinal

        if Packs is not None:
            self.Packs = Packs
