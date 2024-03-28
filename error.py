class DimensionError(Exception):
    """ Clase de Excepción personalizada para manejar errores de dimensiones inválidas.

    Args:
        Exception (class): Clase de la que se heredan Metodos.
    """
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None):
        """ Metodo que iniciliza la instancia de DimensionError.

        Args:
            mensaje (str): Cadena de texto de la descripción del error.
            dimension (int, optional): Valor de la dimensión que causó el error. Defaults to None.
            maximo (int, optional): Valor máximo permitido para la dimensión. Defaults to None.
        """
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        """ Metodo que retorna la representación en cadena de texto de la excepción.

        Returns:
            str: Mensaje a retornar.
        """
        # Validacion
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            ret = self.mensaje
            # Agrega información de la dimensión si está disponible
            if self.dimension:
                ret += f" Se ingresó dimensión {self.dimension}."
            if self.maximo:
                # Agrega información del valor máximo permitido si está disponible
                ret += f" El valor máximo permitido es {self.maximo}."
            return f"Dimension recibida: {self.dimension}, Máximo permitido: {self.maximo}"
