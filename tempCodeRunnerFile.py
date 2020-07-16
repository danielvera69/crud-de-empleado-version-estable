from ctr_empleado import CtrEmpleado
from mod_empleado import ModEmpleado
from funciones import menu

ctr = CtrEmpleado()
def insertar(rango):
    for i in range(int(rango)):
        nombre = input('Ingrese nombre: ')
        sueldo = input('Ingrese sueldo: ')
        cli = ModEmpleado(nom=nombre, sueld=sueldo)
        if ctr.ingresar(cli):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar el Registro')

def modificar():
    codigo = input('Ingrese codigo: ')
    nombre = input('Ingrese nombre: ')
    sueldo = input('Ingrese sueldo: ')
    cli = ModEmpleado(cod=codigo,nom=nombre,sueld=sueldo)
    if ctr.modificar(cli):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar el Registro')

def eliminar():
    codigo = input('--Ingrese codigo: ')
    cli = ModEmpleado(cod=codigo)
    if ctr.eliminar(cli):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar el Registro')

def consultar():
    buscar = input('Ingrese nombre a buscar: ')
    cli = ctr.consulta(buscar)
    print('   Codigo  Nombre  Sueldo')
    for registro in cli:
        print('{:7} {:3} {:6}'.format(registro[0], registro[1], registro[2]))

def ejecutar_empleado():
    opc = ''
    while opc != '4':
        opc = str(menu(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Salir'],
            'Menu Empleado'))
        if opc == '0':
            print('\n<<<Insertar datos>>> ')
            valor = input('-Ingrese cantidad de datos a Ingresar')
            insertar(valor)
        elif opc == '1':
            print('\n<<<Modificar datos>>>')
            modificar()
        elif opc == '2':
            print('\n<<<Eliminar datos>>>')
            eliminar()
        elif opc == '3':
            print('\n<<<Consultar datos>>>')
            consultar()
        elif opc == '4':
            print('<<<Gracias por usar el Sistema>>>')
        elif opc != '4':
            print('Seleccione una opción correcta')
ejecutar_empleado()