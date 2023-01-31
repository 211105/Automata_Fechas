import PyPDF2
from  tkinter import *
from tkinter import filedialog
trancisiones = [#ES,EL,ES
                [1,["0"],2],
                [1,["1"],18],
                [1,["2"],38],
                [1,["3"],45],
                [2,["1","2","3","4","5","6","7","8","9"],3],
                [3,["-"],4],
                [3,["/"],11],
                [4,["2"],5],
                [4,["3"],7],
                [4,["0"],9],
                [5,["0","1","2","3","4","5","6","7","8","9"],6],
                [6,["-"],52],
                [7,["0","1"],8],
                [8,["-"],52],
                [9,["1","2","3","4","5","6","7","8","9"],10],
                [10,["-"],52],
                [11,["2"],12],
                [11,["3"],14],
                [11,["0"],16],
                [12,["0","1","2","3","4","5","6","7","8","9"],13],
                [13,["/"],52],
                [14,["0","1"],15],
                [15,["/"],52],
                [16,["1","2","3","4","5","6","7","8","9"],17],
                [17,["/"],52],
                [18,["1","2"],19],
                [18,["3","4","5","6","7","8","9"],39],
                [19,["-"],20],
                [19,["/"],29],
                [20,["2"],21],
                [20,["3"],23],
                [20,["0"],25],
                [20,["1"],27],
                [21,["0","1","2","3","4","5","6","7","8","9"],22],
                [22,["-"],52],
                [23,["0","1"],24],
                [24,["-"],52],
                [25,["1","2","3","4","5","6","7","8","9"],26],
                [26,["-"],52],
                [27,["0","1","2"],28],
                [27,["3","4","5","6","7","8","9"],22],
                [28,["-"],52],
                [29,["0"],30],
                [29,["1"],32],
                [29,["2"],34],
                [29,["3"],36],
                [30,["1","2","3","4","5","6","7","8","9"],31],
                [31,["/"],52],
                [32,["0","1","2"],33],
                [32,["3","4","5","6","7","8","9"],35],
                [33,["/"],52],
                [34,["0","1","2","3","4","5","6","7","8","9"],35],
                [35,["/"],52],
                [36,["0","1"],37],
                [37,["/"],52],
                [38,["0","1","2","3","4","5","6","7","8","9"],39],
                [39,["-"],40],
                [39,["/"],47],
                [40,["0"],41],
                [40,["1"],43],
                [41,["1","2","3","4","5","6","7","8","9"],42],
                [42,["-"],52],
                [43,["0","1","2"],44],
                [44,["-"],52],
                [45,["0","1"],46],
                [46,["-"],40],
                [46,["/"],47],
                [47,["0"],48],
                [47,["1"],50],
                [48,["1","2","3","4","5","6","7","8","9"],49],
                [49,["/"],52],
                [50,["0","1","2"],51],
                [51,["/"],52],
                [52,["1","2","3","4","5","6","7","8","9"],53],
                [52,["0"],57],
                [53,["0","1","2","3","4","5","6","7","8","9"],54],
                [54,["0","1","2","3","4","5","6","7","8","9"],55],
                [55,["0","1","2","3","4","5","6","7","8","9"],56],
                [57,["1","2","3","4","5","6","7","8","9"],58],
                ] 
alfabeto = ["0","1","2","3","4","5","6","7","8","9","-","/"]
estados_finales = [54,58,56]
datos2 = []
raiz = Tk()



#la funcion lee cual es el camino que tomo para llegar al resultado 
def leer_trancisiones():
    global estado_actual
    global auxiliar_str
    global cadenas_recopiladas
    global bandera 
    bandera = 0
    cadenas_recopiladas = []
    guardar_o_no_guardar = True 
    auxiliar_str = ""
    estado_actual = 1
    print("estado actual: ", estado_actual)

    #bandera se incrementa asta el numero total de palabras que hay
    for bandera in range(numero_palabras):

        # elemento es el caracter de la palabra almacenada en datos[bandera2]
        for elemento in datos2[bandera]:

            #valida si el caracter leido existe en el alfabeto si no cancela todo el for e inica con la siguiente palabra
            if (elemento in alfabeto):    

                #valida si desde el estado actual sale una transicion en el caso de que no 
                if validar_estado_trancision():

                    #iteracion con el numero de trancisiones
                    for i in range(78):

                            #si encuentra el estado actual 
                            if estado_actual == trancisiones[i][0]:

                                #busca en cual transiciones tomara con base al elemento
                                if elemento in trancisiones[i][1]:

                                    #ya que lo encontro el estado actual pasa a ser el estado final despues del elemento
                                    estado_actual = trancisiones[i][2]
                                    auxiliar_str = auxiliar_str +  elemento
                                    print(len(auxiliar_str), "::", len(datos2[bandera]))
                                    print(auxiliar_str, "::", datos2[bandera])
                                    
                                    
                                    if guardar_o_no_guardar == True and estado_actual in estados_finales and len(auxiliar_str) == len(datos2[bandera]):
                                   
                                        cadenas_recopiladas.append(auxiliar_str)
                                        estado_actual = 1
                                        auxiliar_str = ""

                                    break

                #si validar_Estado_trancision es false la cadena no es valida           
                else:
                    print("cadena no valida ")
                    estado_actual = 1
                    auxiliar_str = ""
                    guardar_o_no_guardar = False
                    
            # si el elemento no esta en el alfabeto termina la balabra completa       
            else:
                estado_actual = 1
                auxiliar_str = ""
                break


        estado_actual = 1
        auxiliar_str = ""
                    


def validar_estado_trancision():
     for i in  range(78):
        if estado_actual == trancisiones[i][0]:
            print ("estado actual: ", estado_actual, "transicion: ", trancisiones[i][0] )
            return True



def txt_palabras():
    global numero_palabras
    with open('texto-pdf.txt', 'r', encoding="utf-8") as file:
        contents = file.read()
        datos2.extend(contents.split())
    numero_palabras = len(datos2)
    



def leer_archivo(archivo):
    pdf_file_obj = open(archivo, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    f = open ('texto-pdf.txt','w', encoding="utf-8")
    for page in range(pdf_reader.getNumPages()):
        page_obj = pdf_reader.getPage(page)
        text = page_obj.extract_text()
        f.write(text.strip())
    f.close()



def abrirArchivo():
    global archivo
    archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=(("Archivos de Texto",".txt"), ("Archivos pdf", ".pdf")))
    leer_archivo(archivo)
    txt_palabras()
    leer_trancisiones()
    print(cadenas_recopiladas)
    text.insert(INSERT, cadenas_recopiladas, "\n")
   

   
def main(): 
    global text   
    text = Text(raiz)
    raiz.title("Automata detector de fechas")
    text.insert(INSERT, "los patrones validos son \n")
    text.insert(INSERT, "mm/dd/aaaa\n")
    text.insert(INSERT, "mm-dd-aaaa\n")
    text.insert(INSERT, "mm/dd/aa\n")
    text.insert(INSERT, "mm-dd-aa\n")
    text.insert(INSERT, "dd/mm/aaaa\n")
    text.insert(INSERT, "dd-mm-aaaa\n")
    text.insert(INSERT, "dd/mm/aa\n")
    text.insert(INSERT, "dd-mm-aa\n")
   

    text.pack()

    raiz.geometry("520x480") #Configurar tamaño
    Button(raiz, text="Abrir Archivo", command=abrirArchivo).pack()
    raiz.mainloop()
   

main()
