import sys
import pymysql


class Conector:
    def __init__(self, server='localhost', usuario='root', password='daniel', basedato='nomina'):
        self.__server = server
        self.__usuario = usuario
        self.__password = password
        self.__basedato = basedato
        self.__conn = ''
        self.__conector = ''

    def conectar(self):
        try:
            self.__conn = pymysql.connect(
                host=self.__server, user=self.__usuario, passwd=self.__password, db=self.__basedato)
            self.__conector = self.__conn.cursor()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Error en la conexion", e)
            sys.exit(1)

    def cerrar(self):
        self.__conn.close()
        self.__conector.close()

    @property
    def conector(self):
        return self.__conector

    @property
    def conn(self):
        return self.__conn


"""    def consultar(self, buscar):
        result = False
        try:
            sql = "Select id cod, nombre nom, sueldo sueld From empleado where id like '%" + str(buscar) + "%' or nombre like '%" + str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
"""
con = Conector()
con.conectar()
con.cerrar()
print(con.conector)
""" empleados = con.consultar("")
print(empleados) 
for emp in empleados: print(emp[1])
 """
