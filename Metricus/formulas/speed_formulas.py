# Classe base para Velocidade
class Speed:
    def __init__(self, num: float, with_unit: bool) -> None:
        """
        Inicializa um objeto Speed.

        :param num: Valor da velocidade.
        :type num: float
        :param with_unit: Flag para determinar se a unidade deve ser incluída na saída.
        :type with_unit: bool
        """
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        """
        Formata o resultado da conversão adicionando a unidade, se necessário.

        :param result: Resultado da conversão.
        :type result: float
        :param unit: Unidade a ser adicionada ao resultado.
        :type unit: str
        :return: Resultado formatado com ou sem unidade.
        :rtype: Union[float, str]
        """
        return f"{result} {unit}" if self.with_unit else result


# Metros por segundo (m/s)
class MetersPerSecond(Speed):
    """
    Classe para converter velocidades em metros por segundo (m/s) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
        """
        Converte a velocidade de metros por segundo (m/s) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'km/h', 'mph' ou 'kn'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhecida.
        """
        if unit == 'km/h':
            result = self.num * 3.6
        elif unit == 'mph':
            result = self.num * 2.23694
        elif unit == 'kn':
            result = self.num * 1.94384
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)


# Quilômetros por hora (km/h)
class KilometersPerHour(Speed):
    """
    Classe para converter velocidades em quilômetros por hora (km/h) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
        """
        Converte a velocidade de quilômetros por hora (km/h) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'm/s', 'mph' ou 'kn'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhecida.
        """
        if unit == 'm/s':
            result = self.num / 3.6
        elif unit == 'mph':
            result = self.num / 1.60934
        elif unit == 'kn':
            result = self.num / 1.852
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)


# Milhas por hora (mph)
class MilesPerHour(Speed):
    """
    Classe para converter velocidades em milhas por hora (mph) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
        """
        Converte a velocidade de milhas por hora (mph) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'm/s', 'km/h' ou 'kn'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhecida.
        """
        if unit == 'm/s':
            result = self.num / 2.23694
        elif unit == 'km/h':
            result = self.num * 1.60934
        elif unit == 'kn':
            result = self.num / 1.15078
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)


# Nós (kn)
class Knots(Speed):
    """
    Classe para converter velocidades em nós (kn) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
       """
        Converte a velocidade de nós (kn) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'm/s', 'km/h' ou 'mph'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhe """



from typing import Union

# Classe base para Velocidade


class Speed:
    def __init__(self, num: float, with_unit: bool) -> None:
        """
        Inicializa um objeto Speed.

        :param num: Valor da velocidade.
        :type num: float
        :param with_unit: Flag para determinar se a unidade deve ser incluída na saída.
        :type with_unit: bool
        """
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        """
        Formata o resultado da conversão adicionando a unidade, se necessário.

        :param result: Resultado da conversão.
        :type result: float
        :param unit: Unidade a ser adicionada ao resultado.
        :type unit: str
        :return: Resultado formatado com ou sem unidade.
        :rtype: Union[float, str]
        """
        return f"{result} {unit}" if self.with_unit else result


# Metros por segundo (m/s)


class MetersPerSecond(Speed):
    """
    Classe para converter velocidades em metros por segundo (m/s) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
        """
        Converte a velocidade de metros por segundo (m/s) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'km/h', 'mph' ou 'kn'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhecida.
        """
        if unit == 'km/h':
            result = self.num * 3.6
        elif unit == 'mph':
            result = self.num * 2.23694
        elif unit == 'kn':
            result = self.num * 1.94384
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)


# Quilômetros por hora (km/h)


class KilometersPerHour(Speed):
    """
    Classe para converter velocidades em quilômetros por hora (km/h) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
        """
        Converte a velocidade de quilômetros por hora (km/h) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'm/s', 'mph' ou 'kn'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhecida.
        """
        if unit == 'm/s':
            result = self.num / 3.6
        elif unit == 'mph':
            result = self.num / 1.60934
        elif unit == 'kn':
            result = self.num / 1.852
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)


# Milhas por hora (mph)


class MilesPerHour(Speed):
    """
    Classe para converter velocidades em milhas por hora (mph) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
        """
        Converte a velocidade de milhas por hora (mph) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'm/s', 'km/h' ou 'kn'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhecida.
        """
        if unit == 'm/s':
            result = self.num / 2.23694
        elif unit == 'km/h':
            result = self.num * 1.60934
        elif unit == 'kn':
            result = self.num / 1.15078
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)


# Nós (kn)


class Knots(Speed):
    """
    Classe para converter velocidades em nós (kn) para outras unidades de velocidade.

    Herda da classe base Speed.
    """
    
    def to(self, unit: str) -> Union[float, str]:
        """
        Converte a velocidade de nós (kn) para a unidade especificada.

        :param unit: Unidade para a qual a velocidade será convertida. Pode ser 'm/s', 'km/h' ou 'mph'.
        :type unit: str
        :return: Valor convertido na unidade especificada. Se `with_unit` for True, retorna uma string com o valor e a unidade; caso contrário, retorna um float.
        :rtype: Union[float, str]
        :raises ValueError: Se a unidade especificada não for reconhecida.
        """
        if unit == 'm/s':
            result = self.num / 1.94384
        elif unit == 'km/h':
            result = self.num * 1.852
        elif unit == 'mph':
            result = self.num * 1.15078
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)
