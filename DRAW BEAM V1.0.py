import flet as ft 
from  viga_base import Style
from viga_base import Viga
from viga_base import Acero
class Title (ft.UserControl):
    def __init__(self,title):
        super().__init__()
        self.title = title

    def build(self):
        self.text= ft.Text(str(self.title))
        self.text.color="#7B241C"
        self.text.font_family="verdana"
        self.text.weight="bold"
        return self.text 
        
def main(page: ft.Page):
    page.title = "DRAW BEAM"
    red = '#111130'
    black = '#000000'
    white ='white'
    prueba= "#922B21"
    y = "USUARIO 1-1"
    x = f"BIENVENIDO {y}"
    
    page.theme_mode ='light'
    page.window_always_on_top = True
    page.add(
        ft.Card(
            ft.Container(
                content= ft.Row(
                    [ft.Text(value= x,
                    size = 20,
                    color=white, 
                    font_family="verdana",
                    weight="bold")], 
                    alignment = "center")
                        ),
            color="#34495E",
                    )
             )
    #DENOMINACIÓN
    text_viga =ft.TextField(label="VIGA",
                        width=210,
                        height=55,
                        bgcolor=white,
                        color=black,
                        focused_border_width=3,                        
                        focused_border_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        prefix_text="VIGA",
                        text_align=ft.TextAlign.END,
                        keyboard_type = "number"
                        )
    #GEOMETRÍA
    text_base= ft.TextField(label="BASE",
                        width=110,
                        height=55,
                        bgcolor=white,
                        color=black,
                        focused_border_width=3,                        
                        focused_border_color=black,
                        suffix_text="m",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END)
    
    text_altura = ft.TextField(label="ALTURA",
                        width=110,
                        height=55,
                        bgcolor=white,
                        color=black,
                        focused_border_width=3,                        
                        focused_border_color=black,
                        suffix_text="m",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        )	
    
    text_recubrimiento = ft.TextField(label="RECUBRI.",
                        width=110,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="m",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END
                         )
    
    text_estribo = ft.Dropdown(label = "ESTRIBO",
                        width=110,
                        height=55,
                        prefix_text= "Ø",
                        options=[ft.dropdown.Option("3/8"),
                        ft.dropdown.Option("1/2"),
                        ft.dropdown.Option("5/8"),
                        ft.dropdown.Option("3/4"),
                        ft.dropdown.Option("1"),
                                        ],
                        border_color=black,
                        color=black,
                        border_width=2,
                        )
    
    text_long_gancho = ft.TextField(label="L.Gancho",
                        width=110,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="m",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END
                         )
    
                  
    container_text_geometria = ft.Container(
        content=ft.Column([Title("DENOMINACIÓN"),
                        text_viga,
                        Title("GEOMETRÍA"),
                        text_base,
                        text_altura,
                        text_recubrimiento,          
                            ])
                        )
    
    s1_top =ft.TextField(label="S1",
                        width=75,
                        height=40,
                        bgcolor=white,
                        color=black,
                        focused_border_width=3,                        
                        focused_border_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        suffix_text="m",
                        text_align=ft.TextAlign.END,
                        keyboard_type = "number",
                        disabled= True
                        )
    
    s2_top =ft.TextField(label="S2",
                        width=75,
                        height=40,
                        bgcolor=white,
                        color=black,
                        focused_border_width=3,                        
                        focused_border_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        suffix_text="m",
                        text_align=ft.TextAlign.END,
                        keyboard_type = "number",
                        disabled= True
                        )

    s1_under =ft.TextField(label="S1",
                        width=75,
                        height=40,
                        bgcolor=white,
                        color=black,
                        focused_border_width=3,                        
                        focused_border_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        suffix_text="m",
                        text_align=ft.TextAlign.END,
                        keyboard_type = "number",
                        disabled= True
                        )
    
    s2_under =ft.TextField(label="S2",
                        width=75,
                        height=40,
                        bgcolor=white,
                        color=black,
                        focused_border_width=3,                        
                        focused_border_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        suffix_text="m",
                        text_align=ft.TextAlign.END,
                        keyboard_type = "number",
                        disabled= True
                        ) 

    def style(e):
        style_cad = Style()
        text_estilo_cota.options.clear()
        text_estilo_text.options.clear()
        for i in style_cad.selection_style_cotas():
            text_estilo_cota.options.append(ft.dropdown.Option(i))
        for i in style_cad.selection_style_texto():
            text_estilo_text.options.append(ft.dropdown.Option(i))
        page.update()
    
    lista_aceros_row1_top = []
    lista_aceros_row2_top = []
    lista_aceros_row3_top = []
    lista_aceros_row1_under = []
    lista_aceros_row2_under = []
    lista_aceros_row3_under = []
    
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
    
    def clear_list_row3_top(e):   
        lista_aceros_row3_top.clear()
        cantidad_row3_top.value = None
        cantidad_parcial_row3_top.value  = None
        aceros_disponibles_row3_top.value = None
           
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
                lista_aceros_row1_top.append(aceros_disponibles_row1_top.value)
        print(f"lista 1 top {lista_aceros_row1_top}")

    def creador_lista_row2_top(e):
        if int(cantidad_row2_top.value)> len(lista_aceros_row2_top):
            for i in range(int(cantidad_parcial_row2_top.value)):
                lista_aceros_row2_top.append(aceros_disponibles_row2_top.value)    
        print(f"lista 2 top {lista_aceros_row2_top}")
        
    def creador_lista_row3_top(e):
        if int(cantidad_row3_top.value)> len(lista_aceros_row3_top):
            for i in range(int(cantidad_parcial_row3_top.value)):
                lista_aceros_row3_top.append(aceros_disponibles_row3_top.value)    
        print(f"lista 3 top {lista_aceros_row3_top}")
        
    def creador_lista_row1_under(e):
        if int(cantidad_row1_under.value)> len(lista_aceros_row1_under):
            for i in range(int(cantidad_parcial_row1_under.value)):
                lista_aceros_row1_under.append(aceros_disponibles_row1_under.value)
        print(f"lista 1 under {lista_aceros_row1_under}")

    def creador_lista_row2_under(e):
        if int(cantidad_row2_under.value)> len(lista_aceros_row2_under):
            for i in range(int(cantidad_parcial_row2_under.value)):
                lista_aceros_row2_under.append(aceros_disponibles_row2_under.value)
        print(f"lista 2 under {lista_aceros_row2_under}")
        
    def creador_lista_row3_under(e):
        if int(cantidad_row3_under.value)> len(lista_aceros_row3_under):
            for i in range(int(cantidad_parcial_row3_under.value)):
                lista_aceros_row3_under.append(aceros_disponibles_row3_under.value)
        print(f"lista 3 under {lista_aceros_row3_under}")
    
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
            boton_bucle_row2_top.bgcolor = "#A7C414"
            boton_remove_row2_top.disabled = False
            boton_remove_row2_top.bgcolor = "#A7C414"
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
                boton_bucle_row3_top.bgcolor= "#A7C414"
                boton_remove_row3_top.disabled = False  
                boton_remove_row3_top.bgcolor = "#A7C414"
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
            boton_bucle_row2_under.bgcolor = "#A7C414"
            boton_remove_row2_under.disabled = False
            boton_remove_row2_under.bgcolor = "#A7C414"
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
                boton_bucle_row3_under.bgcolor= "#A7C414"
                boton_remove_row3_under.disabled = False  
                boton_remove_row3_under.bgcolor = "#A7C414"
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
        lista1 = []
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

    text_estilo_text = ft.Dropdown(label = "E. TEXTO",
                        width=210,
                        height=55,
                        border_color=black,
                        color=prueba,
                        border_width=2)
    
    text_estilo_cota = ft.Dropdown(label = "E. COTA",
                        width=210,
                        height=55, 
                        border_color=black,
                        color=prueba,
                        border_width=2) 

    check_row1_top = ft.Checkbox(
                    disabled = True,
                    value= True
                    )
    
    check_row2_top = ft.Checkbox(
                    on_change=activador_desactivador_row2_top
                    )
    
    check_row3_top = ft.Checkbox(
                    disabled = True,
                    on_change=activador_desactivador_row3_top
                    )
    
    check_row1_under = ft.Checkbox(
                    disabled = True,
                    value= True
                    )
    
    check_row2_under = ft.Checkbox(
                    on_change=activador_desactivador_row2_under        
                    )
    
    check_row3_under = ft.Checkbox(
                disabled = True,
                on_change= activador_desactivador_row3_under
        
                    )
    
    cantidad_row1_top = ft.TextField(label="N°Barras",
                        width=100,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="Barras",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        
                         )
    
    cantidad_row2_top = ft.TextField(label="N°Barras",
                        width=100,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="Barras",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )
    
    cantidad_row3_top = ft.TextField(label="N°Barras",
                        width=100,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="Barras",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )
    
    cantidad_row1_under = ft.TextField(label="N°Barras",
                        width=100,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="Barras",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                         )
    
    cantidad_row2_under = ft.TextField(label="N°Barras",
                        width=100,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="Barras",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )

    cantidad_row3_under = ft.TextField(label="N°Barras",
                        width=100,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        suffix_text="Barras",
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )
    
    cantidad_parcial_row1_top = ft.TextField(label="",
                        width=60,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END
                         )
    
    cantidad_parcial_row2_top = ft.TextField(label="",
                        width=60,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )
    
    cantidad_parcial_row3_top = ft.TextField(label="",
                        width=60,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )
    
    cantidad_parcial_row1_under = ft.TextField(label="",
                        width=60,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END
                         )
    
    cantidad_parcial_row2_under = ft.TextField(label="",
                        width=60,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )
    
    cantidad_parcial_row3_under = ft.TextField(label="",
                        width=60,
                        height=55,
                        bgcolor=white,
                        color = black,
                        focused_bgcolor=white,
                        focused_border_color=black,
                        focused_border_width=3,
                        focused_color=black,
                        selection_color="red",
                        border_color="black",
                        border_width=2,
                        text_align=ft.TextAlign.END,
                        disabled=True
                         )
    
    aceros_disponibles_row1_top = ft.Dropdown(
                        width=80,
                        height=55,
                        prefix_text= "Ø",
                        options=[ft.dropdown.Option("3/8"),
                        ft.dropdown.Option("1/2"),
                        ft.dropdown.Option("5/8"),
                        ft.dropdown.Option("3/4"),
                        ft.dropdown.Option("1"),
                                        ],
                        border_color=black,
                        color=black,
                        border_width=2)
    
    aceros_disponibles_row2_top = ft.Dropdown(
                        width=80,
                        height=55,
                        prefix_text= "Ø",
                        options=[ft.dropdown.Option("3/8"),
                        ft.dropdown.Option("1/2"),
                        ft.dropdown.Option("5/8"),
                        ft.dropdown.Option("3/4"),
                        ft.dropdown.Option("1"),
                                        ],
                        border_color=black,
                        color=black,
                        opacity=0.15,
                        border_width=2,
                        disabled=True)

    aceros_disponibles_row3_top = ft.Dropdown(
                        width=80,
                        height=55,
                        prefix_text= "Ø",
                        options=[ft.dropdown.Option("3/8"),
                        ft.dropdown.Option("1/2"),
                        ft.dropdown.Option("5/8"),
                        ft.dropdown.Option("3/4"),
                        ft.dropdown.Option("1"),
                                        ],
                        border_color=black,
                        color=black,
                        opacity=0.15,
                        border_width=2,
                        disabled=True)
    
    aceros_disponibles_row1_under = ft.Dropdown(
                        width=80,
                        height=55,
                        prefix_text= "Ø",
                        options=[ft.dropdown.Option("3/8"),
                        ft.dropdown.Option("1/2"),
                        ft.dropdown.Option("5/8"),
                        ft.dropdown.Option("3/4"),
                        ft.dropdown.Option("1"),
                                        ],
                        border_color=black,
                        color=black,
                        border_width=2)

    aceros_disponibles_row2_under = ft.Dropdown(
                        width=80,
                        height=55,
                        prefix_text= "Ø",
                        options=[ft.dropdown.Option("3/8"),
                        ft.dropdown.Option("1/2"),
                        ft.dropdown.Option("5/8"),
                        ft.dropdown.Option("3/4"),
                        ft.dropdown.Option("1"),
                                        ],
                        border_color=black,
                        color=black,
                        border_width=2,
                        opacity=0.15,
                        disabled=True)
    
    aceros_disponibles_row3_under = ft.Dropdown(
                        width=80,
                        height=55,
                        prefix_text= "Ø",
                        options=[ft.dropdown.Option("3/8"),
                        ft.dropdown.Option("1/2"),
                        ft.dropdown.Option("5/8"),
                        ft.dropdown.Option("3/4"),
                        ft.dropdown.Option("1"),
                                        ],
                        border_color=black,
                        color=black,
                        border_width=2,
                        opacity=0.15,
                        disabled=True)
    
    boton_bucle_row1_top = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD_CIRCLE), ft.Text("Add")], alignment="center", spacing=5
        ),
        bgcolor='#A7C414',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=70,
        mini=True,
        on_click= creador_lista_row1_top)

    boton_bucle_row2_top = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD_CIRCLE), ft.Text("Add")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=70,
        mini=True,
        on_click= creador_lista_row2_top,
        disabled=True)

    boton_bucle_row3_top = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD_CIRCLE), ft.Text("Add")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=70,
        mini=True,
        on_click= creador_lista_row3_top,
        disabled=True)

    boton_remove_row1_top = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.REMOVE_CIRCLE), ft.Text("Remove")], alignment="center", spacing=5
        ),
        bgcolor='#A7C414',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=90,
        mini=True,
        on_click= clear_list_row1_top)
    
    boton_remove_row2_top = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.REMOVE_CIRCLE), ft.Text("Remove")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=90,
        mini=True,
        on_click= clear_list_row2_top,
        disabled=True)
    
    boton_remove_row3_top = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.REMOVE_CIRCLE), ft.Text("Remove")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=90,
        mini=True,
        on_click= clear_list_row3_top,
        disabled=True)
    
    boton_bucle_row1_under = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD_CIRCLE), ft.Text("Add")], alignment="center", spacing=5
        ),
        bgcolor='#A7C414',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=70,
        mini=True,
        on_click= creador_lista_row1_under)
    
    boton_bucle_row2_under = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD_CIRCLE), ft.Text("Add")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=70,
        mini=True,
        on_click= creador_lista_row2_under,
        disabled=True)
    
    boton_bucle_row3_under = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD_CIRCLE), ft.Text("Add")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=70,
        mini=True,
        on_click= creador_lista_row3_under,
        disabled=True)
    
    boton_remove_row1_under = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.REMOVE_CIRCLE), ft.Text("Remove")], alignment="center", spacing=5
        ),
        bgcolor='#A7C414',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=90,
        mini=True,
        on_click= clear_list_row1_under)

    boton_remove_row2_under = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.REMOVE_CIRCLE), ft.Text("Remove")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=90,
        mini=True,
        on_click= clear_list_row2_under,
        disabled=True)
    
    boton_remove_row3_under = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.REMOVE_CIRCLE), ft.Text("Remove")], alignment="center", spacing=5
        ),
        bgcolor='white',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=90,
        mini=True,
        on_click= clear_list_row3_under,
        disabled=True)
    
    boton = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.DRAW), ft.Text("DIBUJAR")], alignment="center", spacing=5
        ),
        bgcolor='#E5812B',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=210,
        mini=True,on_click= value_geometria)
    boton_style = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.LINE_STYLE), ft.Text("CARGAS ESTILOS")], alignment="center", spacing=5
        ),
        bgcolor='#E5812B',
        shape=ft.RoundedRectangleBorder(radius=5),
        width=210,
        mini=True,
        on_click= style)
    
    page.add(ft.Row([Title("DENOMINACIÓN Y ESTILOS")],alignment="center",spacing=25))
    page.add(ft.Row([text_viga,text_estilo_text,text_estilo_cota],alignment="center",spacing=20))
    page.add(ft.Row([Title("GOEMETRÍA Y ESTRIBO")],alignment="center"))
    page.add(ft.Row([text_base,text_altura,text_recubrimiento, text_estribo, text_long_gancho],alignment="center",spacing=20))
    page.add(ft.Row([Title("ACEROS")],alignment="center",spacing=65))
    
    x_top = ft.Row([Title("FILA 1"),check_row1_top,cantidad_row1_top,cantidad_parcial_row1_top,aceros_disponibles_row1_top,boton_bucle_row1_top,boton_remove_row1_top],alignment="center",spacing=15)
    y_top = ft.Row([Title("FILA 2"),check_row2_top,cantidad_row2_top,cantidad_parcial_row2_top,aceros_disponibles_row2_top,boton_bucle_row2_top,boton_remove_row2_top,s1_top],alignment="center",spacing=15)
    z_top = ft.Row([Title("FILA 3"),check_row3_top,cantidad_row3_top,cantidad_parcial_row3_top,aceros_disponibles_row3_top,boton_bucle_row3_top,boton_remove_row3_top,s2_top],alignment="center",spacing=15)
    
    x_under = ft.Row([Title("FILA 1"),check_row1_under,cantidad_row1_under,cantidad_parcial_row1_under,aceros_disponibles_row1_under,boton_bucle_row1_under,boton_remove_row1_under],alignment="center",spacing=15)
    y_under = ft.Row([Title("FILA 2"),check_row2_under,cantidad_row2_under,cantidad_parcial_row2_under,aceros_disponibles_row2_under,boton_bucle_row2_under,boton_remove_row2_under,s1_under],alignment="center",spacing=15)
    z_under = ft.Row([Title("FILA 3"),check_row3_under,cantidad_row3_under,cantidad_parcial_row3_under,aceros_disponibles_row3_under,boton_bucle_row3_under,boton_remove_row3_under,s2_under],alignment="center",spacing=15)
    
    a = ft.Column([Title("SUPERIOR"),x_top,y_top,z_top, Title("INFERIOR"),x_under,y_under,z_under],alignment="center",spacing=10)
    '''b = ft.Column([Title("INFERIOR"),x,y,z],alignment="center",spacing=10)'''
    page.add(ft.Row([a],alignment="center",spacing=120))
    
    #page.add(ft.Row([container_text_geometria,container_estilo], alignment="center",spacing=10))
    page.add(ft.Row([boton_style, boton], alignment="center"))
    return (text_viga, text_base, text_altura,
            )
ft.app(target=main)



