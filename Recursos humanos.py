
#Empleados = {}
class Persona:
    def _init_(self, Codigo, nombre, departamento, años):
        self.Codigo = Codigo
        self.nombre = nombre
        self.departamento = departamento
        self.años = años
        self.Empleados = {}

    def Diccionario(self):
        return {
            "Codigo": self.Codigo,
            "nombre": self.nombre,
            "departamento": self.departamento,
            "Años": self.años
        }

Empleados = {}
def Agregar_Empleado():
    Codigo = int(input("Ingrese el Codigo de Empleado: "))
    nombre = input("Ingrese el nombre del Empleado: ")
    Departamento = input("Ingrese el departamento del Empleado: ")
    años = int(input("Ingrese los años de antiguedad:"))
    trabajador = Persona(Codigo, nombre, Departamento, años)
    Empleados[Codigo] = trabajador
    print("Empleado agregado exitosamente")
    #def Informacion(self):
def menu():
    while True:
        print("\n Bienvenido al Recurso de Empleados")
        print("1. Regitro de Empleados: ")
        print("2. salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            Agregar_Empleado()
        elif opcion == "3":
            print("👋 Programa finalizado.")
            break
        else:
            print("❌ Opción inválida.\n")
menu()
