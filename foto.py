# Importacion de clase externa.
from error import DimensionError

class Foto:
    """
    Clase Que representa una imagen con dimensiones.
    """
    # Dimension máxima permitida para la foto.
    MAX = 2500 

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """ Metodo que inicializa una instancia de clase Foto.

        Args:
            ancho (int): Corresponde al ancho inicial de la foto.
            alto (int): Corresponde al alto inicial de la foto.
            ruta (str): Ruta del archivo de la foto.

        Raises:
            DimensionError: Error en caso de no respetarse los valores máximos.
        """
        # Validación del ancho y del alto.
        if not 1 <= ancho <= Foto.MAX or not 1 <= alto <= Foto.MAX:
            raise DimensionError("Las dimensiones de la foto son inválidas", ancho if ancho < 1 or ancho > Foto.MAX else alto, Foto.MAX)
        self.__ancho = ancho
        self.__alto = alto
        self.__ruta = ruta  

    @property
    def ancho(self) -> int:
        """ Metodo que retorna el ancho de la foto

        Returns:
            int: Ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho: int) -> None:
        """ Metodo que actualiza el ancho de la foto.

        Args:
            nuevo_ancho (int): Nuevo ancho de la foto.

        Raises:
            DimensionError: Error que retorna en caso de no cumplirse los limites.
        """
        if not 1 <= nuevo_ancho <= Foto.MAX:
            raise DimensionError("Ancho fuera de rango", ancho, Foto.MAX)
        self.__ancho = nuevo_anchoancho

    @property
    def alto(self) -> int:
        """ Metodo que retorna el altode la foto

        Returns:
            int: Alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto: int) -> None:
        """ Metodo que actualiza el alto de la foto.

        Args:
            nuevo_ancho (int): Nuevo alto de la foto.

        Raises:
            DimensionError: Error que retorna en caso de no cumplirse los limites.
        """
        if not 1 <= nuevo_altoalto <= Foto.MAX:
            raise DimensionError("Alto fuera de rango", nuevo_altoalto, Foto.MAX)
        self.__alto = _nuevo_alto
