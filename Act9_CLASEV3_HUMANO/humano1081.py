print("Act 9 clase Humano")
print("Luis Molinar Mat: 22308051281081")
# zona de class
class Humano1081:
    # zona de atributos
    edad=0
    estatura=0
    peso=0
    genero=" "
    colorpelo=" "
    fechanacimiento=" "
    # zona funciones dentro de la clase
    def correr1081(self,n):
        print(f"{n} esta corriendo ")

    def caminar1081(self,n2):
        print(f"{n2} esta caminando ")

    def hablar1081(self,n3):
        print(f"{n3} esta hablando en clase ")

    def escuchar1081(self,n4):
        print(f"{n4} esta escuchando musica mientras el profe esta ablando y no pone atencion")

    def comer1081(self,n5):
        print(f"{n5} esta comiendo en clase ")

# zona de creacion de objetos
luis=Humano1081()
luisa=Humano1081()
# zona de usando objetos
print("")
print("Resultados para Luis")
luis.edad=17
luis.estatura=1.70
luis.peso=78
luis.genero="Hombre"
luis.colorpelo="Negro"
luis.fechanacimiento="18/junio/2007"
print(f"Edad: {luis.edad}")
print(f"Estatura: {luis.estatura}")
print(f"Peso: {luis.peso}")
print(f"Genero: {luis.genero}")
print(f"Color de pelo: {luis.colorpelo}")
print(f"Fecha de ncimiento: {luis.fechanacimiento}")

luis.correr1081("Luis")
luis.caminar1081("Luis")
luis.hablar1081("Luis")
luis.escuchar1081("Luis")
luis.comer1081("Luis")

print("")
print("Resultados para Luisa")
luisa.edad=16
luisa.estatura=1.65
luisa.peso=60
luisa.genero="Mujer"
luisa.colorpelo="Negro"
luisa.fechanacimiento="12/julio/2008"
print(f"Edad: {luisa.edad}")
print(f"Estatura: {luisa.estatura}")
print(f"Peso: {luisa.peso}")
print(f"Genero: {luisa.genero}")
print(f"Color de pelo: {luisa.colorpelo}")
print(f"Fecha de ncimiento: {luisa.fechanacimiento}")

luisa.correr1081("Luisa")
luisa.caminar1081("Luisa")
luisa.hablar1081("Luisa")
luisa.escuchar1081("Luisa")
luisa.comer1081("Luisa")