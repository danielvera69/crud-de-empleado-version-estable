import sys
from conexion import Conector

class DaoEmpleado(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select id cod, nombre nom, sueldo sueld From empleado where nombre like '%" + str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta del empleado",e)
            self.conn.rollback()
        finally: self.cerrar()
        return result

    def ingresar(self, emp):
        correcto = True
        try:
            sql = "insert into empleado (nombre, sueldo) values (%s, %s)"
            self.conectar()
            self.conector.execute(sql, (emp.nombre, emp.sueldo))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar empleado",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def modificar(self, emp):
        correcto = True
        try:
            sql = 'Update empleado set nombre  = %s, sueldo = %s where id = %s'
            self.conectar()
            self.conector.execute(sql, (emp.nombre, emp.sueldo ,emp.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar empleado",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def eliminar(self, emp):
        correcto = True
        try:
            sql = 'delete from empleado where id = %s'
            self.conectar()
            self.conector.execute(sql, (emp.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar empleado",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

""" con = DaoEmpleado()
empleados = con.consultar("")
print(empleados) 
for emp in empleados: print(emp[1]) """
