class Mascota:
  def _init_(self, pIdMascota,pNombreDeLaMascota, pColorDeRaza, pRazaAnimal, pDiagnosticos, pFertilizado, pPeso):
    
    self.__nomMascota=pNombreDeLaMascota
    self.__colorRaza=pColorDeRaza
    self.__razaMascota=pRazaAnimal
    self.__codigoMascota=pIdMascota
    self.__diagnostico=pDiagnosticos
    self.__fertilizado=pFertilizado
    self.__pesoMascota=pPeso

  def setNombre(self, pNombreDeLaMascota):
    self.__nomMascota=pNombreDeLaMascota

  def setPeso(self, pPeso):
    self.__pesoMascota=pPeso

  def setCodigo(self, pIdMascota):
    self.__codigoMascota=pIdMascota
        
  def setRaza(self, pRaza):
    self.__raza=pRaza
    
  def setColor(self, pColorDeRaza):
        self.__color=pColorDeRaza
  
  def setFertilizacion(self, pFertilizado):
        self.__fertilizado=pFertilizado
  
  def setDiagnosticos(self, pDiagnosticos):
    self.__diagnosticos=pDiagnosticos
  def getNombre(self):
    return self.__nomMascota
    


class Persona():

  
  def _init_(self, pCodigoPersona, pNombre, pApellidos, pIdentificacion, pTelefono, pDireccion):

    self.__codigoPersona=pCodigoPersona
    self.__nombre=pNombre
    self.__apellidos=pApellidos
    self.__identificacion=pIdentificacion
    self.__telefono=pTelefono
    self.__direccion=pDireccion

  def setCodigoPersona(self, pCodigoPersona):
    self.__codigoPersona=pCodigoPersona

  def setNombre(self, pNombre):
    self.__nombre=pNombre

  def setApellidos(self, pApellidos):
    self.__apellidos=pApellidos

  def setIdentificacion(self,pIdentificacion):
    self.__identificacion=pIdentificacion

  def setTelefono(self, pTelefono):
    self.__telefono=pTelefono

  def setDireccion(self,pDireccion):
    self.__direccion=pDireccion


  def getCodigoPersona(self):
    return self.__codigoPersona
  def getNombre(self):
    return self.__nombre
  
  def getApellidos(self):
    return self.__apellidos
  
  def getIdentificacion(self):
    return self.__identificacion

  def getTelefono(self):
    return self.__telefono
    
  def getDireccion(self):
    return self.__direccion


class Medico(Persona):
  
  def _init_(self, pCodigoPersona, pNombre, pApellido,pIdentificacion,pTelefono,pDireccion, pEspecialidad):
    super()._init_(pCodigoPersona, pNombre, pApellido, pIdentificacion, pTelefono,pDireccion)              
    self.__especialidad=pEspecialidad
    
def setEspecialidad(self, pEspecialidad):
    self.__especializacion=pEspecialidad

def getEspecialidad(self):
    return self.__especialidad

class Cliente(Persona,Mascota):
  def _init_(self, pCodigoPersona, pNombre, pApellido,pIdentificacion, pTelefono, pDireccion,pCodigoMascota,pNombreMascota, pColor, pRaza, pDiagnosticos):

    Persona._init_(self, pCodigoPersona, pNombre, pApellido, pIdentificacion, pTelefono, pDireccion)
    
    Mascota._init_(self, pCodigoMascota,pNombreMascota, pColor, pRaza, pDiagnosticos,)