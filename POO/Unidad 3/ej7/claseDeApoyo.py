from clasePersonal import Personal

class DeApoyo(Personal):
    __categoria: int

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra ):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
        self.__categoria = int(categoria)

    def __str__(self):
        return f'cat = {self.__categoria}, {self.getCuil()}'

    @classmethod
    def getTipo(self):
        return 'Personal de apoyo'

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldoBasico = super().getSueldoBasico(),
                antiguedad = super().getAntiguedad(),
                categoria = self.__categoria,
                areaInvestigacion = '',
                tipoInvestigacion='',
                carrera='',
                cargo='',
                catedra=''
            )
        )
        return d

    def calcularSueldo(self):
        su = super().getSueldoBasico()
        su = (1 + super().getAntiguedad()/100) * super().getSueldoBasico()
        if self.__categoria <= 10:
            su += super().getSueldoBasico() * 0.1
        elif self.__categoria <= 20 and self.__categoria > 10:
            su += super().getSueldoBasico() * 0.2
        elif self.__categoria in [21, 22]:
            su += super().getSueldoBasico() * 0.3
        return su
