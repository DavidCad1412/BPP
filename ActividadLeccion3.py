class calculadora:
    """
    Calculadora.
    Atributos
    ---------
    numero 1:
        este es el primer operando que se utilizara en las operaciones de calculadora.
    numero 2:
        este es el segundo operando que se utilizara en las operaciones de calculadora.

    Metodos
    -------
    Suma:
        Esta funcion suma los operandos numero1 y numero2.
    Resta:
        Esta funcion resta los operandos numero1 y numero2.
    Multiplicaciones:
        Esta funcion multiplica los operandos numero1 y numero2.
    Division:
        Esta funcion divide los operandos numero1 y numero2.

    Ejemplos
    --------
    >>> import calculadora
    >>> Calc = calculadora(6,7)
    >>> res_suma = Calc.sumar()
    >>> res_resta = Calc.restar()
    >>> res_multiplicar = Calc.multiplicar()
    >>> res_dividir = Calc.dividir()
    """
    def __init__(self, numero1, numero2):
        self.numero1 = float(numero1)
        self.numero2 = float(numero2)

    def sumar(self):
        """
        Metodo suma. Aplica la operacion suma sobre los datos de numero1 y numero2.
        Inputs
        ------
            self.numero1
            self.numero2
        Outputs
        -------
            suma: resultado de sumar numero1 y numero2
        """
        suma = self.numero1 + self.numero2
        return suma

    def restar(self):
        """
        Metodo resta. Aplica la operacion resta sobre los datos de numero1 y numero2.
        Inputs
        ------
            self.numero1
            self.numero2
        Outputs
        -------
            resta: resultado de restar numero1 y numero2
        """
        resta = self.numero1 - self.numero2
        return resta

    def multiplicar(self):
        """
        Metodo multiplica. Aplica la operacion multiplica sobre los datos de numero1 y numero2.
        Inputs
        ------
            self.numero1
            self.numero2
        Outputs
        -------
            multiplicacion: resultado de multiplicar numero1 y numero2
        """
        multiplicacion = self.numero1 * self.numero2
        return multiplicacion

    def dividir(self):
        """
        Metodo dividir. Aplica la operacion dividir sobre los datos de numero1 y numero2.
        Inputs
        ------
            self.numero1
            self.numero2
        Outputs
        -------
            division: resultado de dividir numero1 y numero2
        """
        division = self.numero1 / self.numero2
        return division
