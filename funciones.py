def menu(opciones, titulo):
    print('\n*******{}*******'.format(titulo))
    for op in range(0, len(opciones)):
        print("{}) {}".format(op, opciones[op]))
    opc = input('Elija Opcion [0...{}]: '.format(len(opciones)-1))
    return opc