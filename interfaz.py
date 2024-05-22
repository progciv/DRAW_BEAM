import flet as ft 
from viga_base import Style
from viga_base import Viga

#Colores para la interfaz
red = '#000030'
black = '#000000'
white ='white'
azul = '#7B241C'
verde = '#A7C414'
naranja = '#E5812B'
nuevo = '#581845'

#Clase para los titulos y subtitulos de la interfaz
class Title(ft.Text):
    def __init__(self,title ,color = azul,size = 14):
        super().__init__()
        self.value = title
        self.font_family = "Verdana"
        self.italic = False
        self.weight = "bold"
        self.size = size
        self.color = color

#Clase para los inputs de la interfaz
class TextF(ft.TextField):
    def __init__(self,label, width, height, suffix = None,
                 prefix = None, disabled = False):
        super().__init__()
        self.label = label
        self.width = width
        self.height = height
        self.suffix = suffix
        self.prefix = prefix
        self.value = None
        self.bgcolor = "white" 
        self.color = "black"
        self.selection_color = "blue"
        self.focused_color = "Red"
        self.focused_border_width= 3
        self.width = self.width
        self.height = self.height
        self.suffix_text = self.suffix
        self.prefix_text = self.prefix
        self.border_width = 2
        self.border_color = "black"
        self.text_align = ft.TextAlign.END
        self.disabled = disabled

#Clase para los desplegables de la interfaz
class Drop(ft.Dropdown):
    def __init__(self,label, width, height, prefix = None,
                 items=["3/8","1/2","5/8","3/4","1"], disabled = False):
        super().__init__()
        self.label = label
        self.prefix = prefix
        self.items = items
        self.value = None
        self.label = self.label
        self.prefix_text = self.prefix
        self.border_width = 2
        self.width = width
        self.height = height
        self.color = "black"
        self.border_color = "black"
        self.disabled = disabled
        self.option()
    def option(self):
        for i in range(len(self.items)):
            self.options.append(ft.dropdown.Option(self.items[i]))

class Bot(ft.FloatingActionButton):
    def __init__(self, label, width, radio, 
                 icon = "add_circle", mini = True, 
                 click = None, disabled = False,
                 color = verde,
                 text_color = white):
        
        super().__init__()
        self.content = ft.Row(
            [ft.Icon(icon),ft.Text(label, color = text_color)], 
             alignment = "center", spacing = 5
        )
        self.bgcolor = color
        self.shape = ft.RoundedRectangleBorder(radius = radio)
        self.width = width
        self.mini = mini
        self.on_click = click
        self.disabled = disabled

class Check(ft.Checkbox):
    def __init__(self, disabled = True, value = True, change = None):
        super().__init__()
        self.disabled = disabled
        self.value = value
        self.on_change = change
        
def main(page: ft.Page):
    page.window_width = 700
    page.window_height = 820
    page.title = "DRAW BEAM V1.0"
    page.theme_mode ='light'
    page.window_always_on_top = True

    #TITULO 
    text_title = Title(f"BIENVENIDO", white, 20 )

    #DENOMINACIÓN Y ESTILOS
    text_viga = TextF("VIGA", 197, 55, "", "VIGA")
    text_estilo_text = Drop("E. TEXTO", 197, 55, None, [])
    text_estilo_cota = Drop("E. COTA", 197, 55, None, [])
    
    #GEOMETRÍA Y ESTRIBO
    text_base= TextF("BASE", 110, 55, "m")
    text_altura = TextF("ALTURA", 110, 55, "m")
    text_recubrimiento = TextF("RECUBRI.", 110, 55, "m")
    text_estribo = Drop("ESTRIBO", 110, 55, "Ø ")
    text_long_gancho = TextF("L.Gancho", 110, 55, "m")

    #PARA LOS ESPACIADORES - ARRIBA
    s1_top =TextF("S1", 75, 40, "m")
    s1_top.disabled = True

    s2_top =TextF("S2", 75, 40, "m")
    s2_top.disabled = True

    #PARA LOS ESPACIADORES - ABAJO
    s1_under =TextF("S1", 75, 40, "m")
    s1_under.disabled = True

    s2_under =TextF("S1", 75, 40, "m")
    s2_under.disabled = True

    #LISTAS PARA ALMACENAR LA CANTIDAD DE ACERO 
    lista_aceros_row1_top = []
    lista_aceros_row2_top = []
    lista_aceros_row3_top = []
    lista_aceros_row1_under = []
    lista_aceros_row2_under = []
    lista_aceros_row3_under = []

    #FUNCIONES PARA ELIMINAR DATOS DE LA LISTA
    def clear_list_row1_top(e):
        lista_aceros_row1_top.clear()
        cantidad_row1_top.value = None
        cantidad_parcial_row1_top.value  = None
        aceros_disponibles_row1_top.value = None
        page.update()
    
    def clear_list_row2_top(e):
        lista_aceros_row2_top.clear()
        cantidad_row2_top.value = None
        cantidad_parcial_row2_top.value  = None
        aceros_disponibles_row2_top.value = None
        page.update()
        
    def clear_list_row3_top(e):   
        lista_aceros_row3_top.clear()
        cantidad_row3_top.value = None
        cantidad_parcial_row3_top.value  = None
        aceros_disponibles_row3_top.value = None
        page.update()
        
    def clear_list_row1_under(e):
        lista_aceros_row1_under.clear()
        cantidad_row1_under.value = None
        cantidad_parcial_row1_under.value  = None
        aceros_disponibles_row1_under.value = None
        page.update()
    
    def clear_list_row2_under(e):
        lista_aceros_row2_under.clear()
        cantidad_row2_under.value = None
        cantidad_parcial_row2_under.value  = None
        aceros_disponibles_row2_under.value = None
        page.update()
    
    def clear_list_row3_under(e):   
        lista_aceros_row3_under.clear()
        cantidad_row3_under.value = None
        cantidad_parcial_row3_under.value  = None
        aceros_disponibles_row3_under.value = None
        page.update()
      
    def creador_lista_row1_top(e):
        if int(cantidad_row1_top.value)> len(lista_aceros_row1_top):
            for i in range(int(cantidad_parcial_row1_top.value)):
                lista_aceros_row1_top.append(
                    aceros_disponibles_row1_top.value)

    def creador_lista_row2_top(e):
        if int(cantidad_row2_top.value)> len(lista_aceros_row2_top):
            for i in range(int(cantidad_parcial_row2_top.value)):
                lista_aceros_row2_top.append(
                    aceros_disponibles_row2_top.value)    
        
    def creador_lista_row3_top(e):
        if int(cantidad_row3_top.value)> len(lista_aceros_row3_top):
            for i in range(int(cantidad_parcial_row3_top.value)):
                lista_aceros_row3_top.append(
                    aceros_disponibles_row3_top.value)    
        
    def creador_lista_row1_under(e):
        if int(cantidad_row1_under.value)> len(lista_aceros_row1_under):
            for i in range(int(cantidad_parcial_row1_under.value)):
                lista_aceros_row1_under.append(
                    aceros_disponibles_row1_under.value)

    def creador_lista_row2_under(e):
        if int(cantidad_row2_under.value)> len(lista_aceros_row2_under):
            for i in range(int(cantidad_parcial_row2_under.value)):
                lista_aceros_row2_under.append(
                    aceros_disponibles_row2_under.value)
        
    def creador_lista_row3_under(e):
        if int(cantidad_row3_under.value)> len(lista_aceros_row3_under):
            for i in range(int(cantidad_parcial_row3_under.value)):
                lista_aceros_row3_under.append(
                    aceros_disponibles_row3_under.value)
    
    def row_activate_top():
        numero_filas_top = 1
        if check_row2_top.value == True and check_row3_top.value == False:
            numero_filas_top = 2
        elif check_row2_top.value == True and check_row3_top.value == True:
            numero_filas_top = 3
        return numero_filas_top
    
    def row_activate_under():
        numero_filas_under= 1
        if check_row2_under.value == True and check_row3_under.value == False:
            numero_filas_under = 2
        elif check_row2_under.value == True and check_row3_under.value == True:
            numero_filas_under = 3
        return numero_filas_under
    
    def activador_desactivador_row2_top(e):
        if check_row2_top.value == True:
            cantidad_row2_top.disabled = False
            cantidad_parcial_row2_top.disabled = False
            aceros_disponibles_row2_top.disabled = False
            aceros_disponibles_row2_top.opacity = None
            boton_bucle_row2_top.disabled = False
            boton_bucle_row2_top.bgcolor = verde
            boton_remove_row2_top.disabled = False
            boton_remove_row2_top.bgcolor = nuevo
            check_row3_top.disabled = False
            s1_top.disabled = False

        elif check_row2_top.value == False:
            lista_aceros_row2_top.clear()
            lista_aceros_row3_top.clear()
            cantidad_row2_top.disabled = True
            cantidad_parcial_row2_top.disabled = True
            aceros_disponibles_row2_top.disabled = True
            aceros_disponibles_row2_top.opacity = 0.15
            boton_bucle_row2_top.disabled = True
            boton_bucle_row2_top.bgcolor = "white"
            boton_remove_row2_top.disabled = True
            boton_remove_row2_top.bgcolor = "white"
            s1_top.disabled = True
            s1_top.value = ""
            
            cantidad_row2_top.value = None
            cantidad_parcial_row2_top.value = None
            aceros_disponibles_row2_top.value = None
            
            cantidad_row3_top.disabled = True
            cantidad_parcial_row3_top.disabled = True
            aceros_disponibles_row3_top.disabled = True
            aceros_disponibles_row3_top.opacity = 0.15
            boton_bucle_row3_top.disabled = True
            boton_bucle_row3_top.bgcolor = "White"
            boton_remove_row3_top.disabled = True
            boton_remove_row3_top.bgcolor = "White"
            check_row3_top.disabled = True
            check_row3_top.value = False
            s2_top.disabled = True
            s2_top.value = ""
            
            cantidad_row3_top.value = None
            cantidad_parcial_row3_top.value = None
            aceros_disponibles_row3_top.value = None
        page.update()
        
    def activador_desactivador_row3_top(e):
        if check_row2_top.value == True:
            if check_row3_top.value == True:
                cantidad_row3_top.disabled = False
                cantidad_parcial_row3_top.disabled = False
                aceros_disponibles_row3_top.disabled = False
                aceros_disponibles_row3_top.opacity = None
                boton_bucle_row3_top.disabled = False
                boton_bucle_row3_top.bgcolor= verde
                boton_remove_row3_top.disabled = False  
                boton_remove_row3_top.bgcolor = nuevo
                s2_top.disabled = False
                
        if check_row3_top.value == False:
            cantidad_row3_top.disabled = True
            cantidad_parcial_row3_top.disabled = True
            aceros_disponibles_row3_top.disabled = True
            aceros_disponibles_row3_top.opacity = 0.15
            boton_bucle_row3_top.disabled = True
            boton_bucle_row3_top.bgcolor= "white"
            boton_remove_row3_top.disabled = True 
            boton_remove_row3_top.bgcolor = "white"
            s2_top.disabled = True
            lista_aceros_row3_top.clear()
            cantidad_row3_top.value = None
            cantidad_parcial_row3_top.value = None
            aceros_disponibles_row3_top.value = None
            s2_top.value = ""
        page.update()
        
    def activador_desactivador_row2_under(e):
        if check_row2_under.value == True:
            cantidad_row2_under.disabled = False
            cantidad_parcial_row2_under.disabled = False
            aceros_disponibles_row2_under.disabled = False
            aceros_disponibles_row2_under.opacity = None
            boton_bucle_row2_under.disabled = False
            boton_bucle_row2_under.bgcolor = verde
            boton_remove_row2_under.disabled = False
            boton_remove_row2_under.bgcolor = nuevo
            check_row3_under.disabled = False
            s1_under.disabled = False
            
        elif check_row2_under.value == False:
            lista_aceros_row2_under.clear()
            lista_aceros_row3_under.clear()
            cantidad_row2_under.disabled = True
            cantidad_parcial_row2_under.disabled = True
            aceros_disponibles_row2_under.disabled = True
            aceros_disponibles_row2_under.opacity = 0.15
            boton_bucle_row2_under.disabled = True
            boton_bucle_row2_under.bgcolor = "white"
            boton_remove_row2_under.disabled = True
            boton_remove_row2_under.bgcolor = "white"
            s1_under.disabled = True
            s1_under.value = ""
            cantidad_row2_under.value = None
            cantidad_parcial_row2_under.value = None
            aceros_disponibles_row2_under.value = None
            
            cantidad_row3_under.disabled = True
            cantidad_parcial_row3_under.disabled = True
            aceros_disponibles_row3_under.disabled = True
            aceros_disponibles_row3_under.opacity = 0.15
            boton_bucle_row3_under.disabled = True
            boton_bucle_row3_under.bgcolor = "White"
            boton_remove_row3_under.disabled = True
            boton_remove_row3_under.bgcolor = "White"
            check_row3_under.disabled = True
            check_row3_under.value = False
            s2_under.disabled = True
            s2_under.value = ""
            cantidad_row3_under.value = None
            cantidad_parcial_row3_under.value = None
            aceros_disponibles_row3_under.value = None
        page.update()
        
    def activador_desactivador_row3_under(e):
        if check_row2_under.value == True:
            if check_row3_under.value == True:
                cantidad_row3_under.disabled = False
                cantidad_parcial_row3_under.disabled = False
                aceros_disponibles_row3_under.disabled = False
                aceros_disponibles_row3_under.opacity = None
                boton_bucle_row3_under.disabled = False
                boton_bucle_row3_under.bgcolor= verde
                boton_remove_row3_under.disabled = False  
                boton_remove_row3_under.bgcolor = nuevo
                s2_under.disabled = False
                
        if check_row3_under.value == False:
            cantidad_row3_under.disabled = True
            cantidad_parcial_row3_under.disabled = True
            aceros_disponibles_row3_under.disabled = True
            aceros_disponibles_row3_under.opacity = 0.15
            boton_bucle_row3_under.disabled = True
            boton_bucle_row3_under.bgcolor= "white"
            boton_remove_row3_under.disabled = True 
            boton_remove_row3_under.bgcolor = "white"
            s2_under.disabled = True
            lista_aceros_row3_top.clear()
            cantidad_row3_under.value = None
            cantidad_parcial_row3_under.value = None
            aceros_disponibles_row3_under.value = None
            s2_under.value = ""
        page.update()
    
    def value_geometria(e):
        style_cota_ingresado = text_estilo_cota.value
        style_text_ingresado = text_estilo_text.value
        b = float(text_base.value)
        h = float(text_altura.value)
        r = float(text_recubrimiento.value)
        l_g = float(text_long_gancho.value)
        viga = Viga(b,h,r)
        viga.get_interfaz(lista_aceros_row1_top[0],
                          lista_aceros_row1_under[0],
                            text_estribo.value,
                            row_activate_top(),
                            row_activate_under(),
                            len(lista_aceros_row1_top),
                            len(lista_aceros_row2_top),
                            len(lista_aceros_row3_top),
                            len(lista_aceros_row1_under),
                            len(lista_aceros_row2_under),
                            len(lista_aceros_row3_under),
                            s1_top.value,
                            s2_top.value,
                            s1_under.value,
                            s2_under.value,
                            l_g
                            )
        viga.get_lista_interfaz(lista_aceros_row1_top,
                                lista_aceros_row2_top,
                                lista_aceros_row3_top,
                                lista_aceros_row1_under,
                                lista_aceros_row2_under,
                                lista_aceros_row3_under,
                                text_viga.value
                                )
        viga.row_tops()
        viga.row_under()
        viga.points()
        viga.points_estribo_exterior()
        viga.points_bow()
        viga.points_estribo_interior()
        viga.points_gancho()
        viga.points_circle()
        viga.draw_gancho()
        viga.draw()
        viga.draw_line_e()
        viga.draw_bow()
        viga.draw_line_i()
        viga.draw_circle()
        viga.draw_circle_int_top()
        viga.draw_circle_int_under()
        viga.selection_style_cotas()
        viga.selection_style_texto()
        viga.get_style(style_text_ingresado, style_cota_ingresado)
        viga.draw_dimensions()
        viga.draw_diameters_under()
        viga.draw_diameters_top()

    #CHECK PARA ACTIVAR O DESACTIVAR LOS CAMPOS PARA INTRODUCIR TEXTO
    check_row1_top = Check()
    check_row2_top = Check(False, False, activador_desactivador_row2_top)
    check_row3_top = Check(True, False, activador_desactivador_row3_top)

    check_row1_under = Check()
    check_row2_under = Check(False, False, activador_desactivador_row2_under)
    check_row3_under = Check(True, False, activador_desactivador_row3_under)
   
    #PARA COLOCAR LA CANTIDAD DE ACEROS EN LA PARTE SUPERIOR
    cantidad_row1_top = TextF("N°Barras", 100, 55, "Barras")
    cantidad_parcial_row1_top = TextF("", 60, 55)
    aceros_disponibles_row1_top = Drop("Ø", 80, 55)
    
    cantidad_row2_top = TextF("N°Barras", 100, 55, "Barras",
                              disabled = True)
    cantidad_parcial_row2_top = TextF("", 60, 55, disabled = True)
    aceros_disponibles_row2_top = Drop("Ø", 80, 55, disabled = True)

    cantidad_row3_top = TextF("N°Barras", 100, 55, "Barras", 
                              disabled = True)
    cantidad_parcial_row3_top = TextF("", 60, 55, disabled = True)
    aceros_disponibles_row3_top = Drop("Ø", 80, 55, disabled = True)
    
    #PARA COLOCAR LA CANTIDAD DE ACEROS EN LA PARTE INFERIOR

    cantidad_row1_under = TextF("N°Barras", 100, 55, "Barras")
    cantidad_parcial_row1_under = TextF("", 60, 55)

    cantidad_row2_under = TextF("N°Barras", 100, 55, "Barras", 
                                disabled = True)
    cantidad_parcial_row2_under = TextF("", 60, 55, disabled = True)

    cantidad_row3_under = TextF("N°Barras", 100, 55, "Barras", 
                                disabled = True)
    cantidad_parcial_row3_under = TextF("", 60, 55, disabled = True)
    
    aceros_disponibles_row1_under = Drop("Ø", 80, 55)

    aceros_disponibles_row2_under = Drop("Ø", 80, 55, disabled = True)
    
    aceros_disponibles_row3_under = Drop("Ø", 80, 55, disabled = True)
    
    #PARA CREAR LOS BOTONES DE ADD PARA LOS ACEROS SUPERIORES

    boton_bucle_row1_top = Bot("Add", 70, 5, 
                               click = creador_lista_row1_top)
    boton_bucle_row2_top = Bot("Add", 70, 5, disabled = True,
                               click = creador_lista_row2_top,
                                color = white)
    boton_bucle_row3_top = Bot("Add", 70, 5, disabled = True,
                               click = creador_lista_row3_top,
                                color = white)
    
    #PARA CREAR LOS BOTONES DE REMOVE PARA LOS ACEROS SUPERIORES

    boton_remove_row1_top = Bot("Remove", 90, 5,
                                click = clear_list_row1_top,
                                icon = "remove_circle",
                                color = nuevo)
    
    boton_remove_row2_top = Bot("Remove", 90, 5, disabled = True,
                               click = clear_list_row2_top,
                                color = white, icon = "remove_circle")
    boton_remove_row3_top = Bot("Remove", 90, 5, disabled = True,
                               click = clear_list_row3_top,
                                color = white, icon = "remove_circle")
    
    #PARA CREAR LOS BOTONES DE ADD PARA LOS ACEROS INFERIORES
    
    boton_bucle_row1_under = Bot("Add", 70, 5, 
                               click = creador_lista_row1_under)
    boton_bucle_row2_under = Bot("Add", 70, 5, disabled = True,
                               click = creador_lista_row2_under,
                                color = white)
    boton_bucle_row3_under = Bot("Add", 70, 5, disabled = True,
                               click = creador_lista_row3_under,
                                color = white)
    
    #PARA CREAR LOS BOTONES DE REMOVE PARA LOS ACEROS INFERIORES

    boton_remove_row1_under = Bot("Remove", 90, 5,
                                click = clear_list_row1_under,
                                icon = "remove_circle",
                                color = nuevo)
    
    boton_remove_row2_under = Bot("Remove", 90, 5, disabled = True,
                               click = clear_list_row2_under,
                                color = white,icon = "remove_circle")
    boton_remove_row3_under = Bot("Remove", 90, 5, disabled = True,
                               click = clear_list_row3_under,
                                color = white, icon = "remove_circle")
    
    #FUNCIÓN PARA CARGAR LOS ESTILOS DE AUTOCAD EN EL DROP
    def style(e):
        style_cad = Style()
        text_estilo_cota.options.clear()
        text_estilo_text.options.clear()
        for i in style_cad.selection_style_cotas():
            text_estilo_cota.options.append(ft.dropdown.Option(i))
        for i in style_cad.selection_style_texto():
            text_estilo_text.options.append(ft.dropdown.Option(i))
        page.update()

    #BOTONES PARA CARGAR LOS ESTILOS DE AUTOCAD
    boton_draw = Bot("DIBUJAR", 210, 5, "draw", 
                     click = value_geometria,
                     color = naranja)
    boton_style = Bot("CARGAR ESTILOS", 210, 5, "line_style", 
                     click = style,
                     color = naranja)
    
    #ELEMENTOS A AÑADIR A LA VENTANA PRINCIPAL
    page.add(ft.Card(ft.Container(content= ft.Row([text_title], 
                                                  alignment = "center")),
                                                  color="#34495E"))
    page.add(ft.Row([Title("DENOMINACIÓN Y ESTILOS")],
                    alignment="center",spacing=25))
    page.add(ft.Row([text_viga,text_estilo_text,text_estilo_cota],
                    alignment="center",spacing=20))
    page.add(ft.Row([Title("GOEMETRÍA Y ESTRIBO")],
                    alignment="center"))
    page.add(ft.Row([text_base,text_altura,text_recubrimiento, 
                     text_estribo, text_long_gancho],
                    alignment="center",spacing=20))
    page.add(ft.Row([Title("ACEROS")],alignment="center",spacing=65))

    #CREAR FILAS PARA LOS ACEROS SUPERIORES
    x_top = ft.Row([Title("FILA 1"),check_row1_top,
                    cantidad_row1_top,cantidad_parcial_row1_top,
                    aceros_disponibles_row1_top,boton_bucle_row1_top,
                    boton_remove_row1_top],
                    alignment="center",spacing=15)
    y_top = ft.Row([Title("FILA 2"),check_row2_top,cantidad_row2_top,
                    cantidad_parcial_row2_top,
                    aceros_disponibles_row2_top,boton_bucle_row2_top,
                    boton_remove_row2_top,s1_top],
                    alignment="center",spacing=15)
    z_top = ft.Row([Title("FILA 3"),check_row3_top,cantidad_row3_top,
                    cantidad_parcial_row3_top,
                    aceros_disponibles_row3_top,boton_bucle_row3_top,
                    boton_remove_row3_top,s2_top],
                    alignment="center",spacing=15)
    
    #CREAR FILAS PARA LOS ACEROS INFERIORES
    x_under = ft.Row([Title("FILA 1"),check_row1_under,
                      cantidad_row1_under,cantidad_parcial_row1_under,
                      aceros_disponibles_row1_under,
                      boton_bucle_row1_under,boton_remove_row1_under],
                      alignment="center",spacing=15)
    y_under = ft.Row([Title("FILA 2"),check_row2_under,
                      cantidad_row2_under,cantidad_parcial_row2_under,
                      aceros_disponibles_row2_under,
                      boton_bucle_row2_under,boton_remove_row2_under,
                      s1_under],
                      alignment="center",spacing=15)
    z_under = ft.Row([Title("FILA 3"),check_row3_under,
                      cantidad_row3_under,cantidad_parcial_row3_under,
                      aceros_disponibles_row3_under,
                      boton_bucle_row3_under,boton_remove_row3_under,
                      s2_under],
                      alignment="center",spacing=15)
    
    #AÑADIR TITULOS Y FILAS DE ACEROS A LA VENTANA PRINCIPAL
    a = ft.Column([Title("SUPERIOR"),x_top, y_top, z_top, Title("INFERIOR"),
                   x_under,y_under,z_under],
                  alignment="center",spacing=10)
    page.add(ft.Row([a], alignment="center", spacing=120))

    #AÑADIR LOS BOTONES A LA VENTANA PRINCIPAL
    page.add(ft.Row([boton_style, boton_draw], alignment="center"))
    return (text_viga, text_base, text_altura)

ft.app(target=main, assets_dir="assets")