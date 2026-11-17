class empleado:
    #Atributos
    #Constructor de la clase
    def __init__(self, nombre: str, salario_base: float):
        self.__nombre = nombre
        self.__salario_base = salario_base
    #Getter
    @property
    def nombre(self) -> str:
        return self.__nombre
    @property
    def salario_base(self) -> float:
        return self.__salario_base
    #Setter
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    @salario_base.setter
    def nombre(self, nuevo_salario: float):
        self.__salario_base = nuevo_salario
    def calcular_salario(irpf: int) -> float:
        salario_irpf = self.__salario_base * (1 - irpf/100)
        return salario_irpf
    #Para hacer un to string es necesario pasar por parametro la instancia del objeto
    def __str__(self) -> str:
        #"f" nos permite "concatenar" con los atributos que queremos llevar al to string
        to_string = f"Nombre: {self.__nombre} - Salario base: {self.__salario_base}"
        #Otra manera de concatenar: "Nombre: {} - Salario base: {}.format(self.__nombre , self.__salario_base)
        return to_string
class vendedor(empleado):
    #Ejemplo de lista
    #ventas: list[float]
    #Meterle empleado en el parentesis crea herencia
    def __init__(self, nombre: str, salario_base: float, ventas: list[float]):
        #Para meter una lista parametrizada se hace como se ve en ventas
        super().__init(nombre, salario_base)
        #super.()__init llama al constructor del padre
        self.__ventas = ventas
    @property
    def ventas(self) -> list[float]:
        return self.__ventas
    #Para sobreescribir el metodo de un padre se usa override
    @override
    def calcular_salario(irpf: int) -> float:
        salario_irpf = self.__salario_base * (1 - irpf/100)
        salario_irpf_mas_ventas = salario_irpf + sum(self.__ventas) * 0.10
        return salario_irpf_mas_ventas