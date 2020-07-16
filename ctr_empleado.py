from dao_empleado import DaoEmpleado
from mod_empleado import ModEmpleado
class CtrEmpleado:
    def __init__(self, emp=None):
        self.empleado = emp

    def consulta(self, buscar):
        objDao = DaoEmpleado()
        return objDao.consultar(buscar)

    def ingresar(self, emp):
        objDao = DaoEmpleado()
        return objDao.ingresar(emp)

    def modificar(self, emp):
        objDao = DaoEmpleado()
        return objDao.modificar(emp)

    def eliminar(self, emp):
        objDao = DaoEmpleado()
        return objDao.eliminar(emp)

""" emp = ModEmpleado()
emp.id=3
emp.nombre='Yadira B'
emp.sueldo=800
ctr = CtrEmpleado()
#ctr.ingresar(emp)
#ctr.modificar(emp)
ctr.eliminar(emp)
empleados=ctr.consulta("")
print(empleados) 
for emp in empleados: print(emp[0],emp[1])
 """