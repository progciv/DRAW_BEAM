from pyautocad import Autocad
from pyautocad import APoint as AP
from math import pi
from math import sin,cos
from fractions import Fraction
import comtypes

class Seccion():
    def __init__(self,b,h,r):
        self.acad = Autocad()
        self.doc = self.acad.doc
        self.base = b
        self.altura = h
        self.r = r
        a = self.acad.doc.Utility.GetPoint()
        self.puntox = a[0]
        self.puntoy = a[1]
        
    def points(self):
        self.point_insert= AP(self.puntox,self.puntoy,0)
        self.point_1 = AP(self.puntox, self.puntoy + self.altura, 0)
        self.point_2 = AP(self.puntox + self.base, self.puntoy + self.altura, 0)
        self.point_3 = AP(self.puntox + self.base, self.puntoy, 0)
        self.point_4 = AP(self.puntox, self.puntoy, 0)
        
    def draw(self):
        self.line_1 = self.acad.model.AddLine(self.point_insert, self.point_1)
        self.line_2 = self.acad.model.AddLine(self.point_1, self.point_2)
        self.line_3 = self.acad.model.AddLine(self.point_2, self.point_3)
        self.line_4 = self.acad.model.AddLine(self.point_3, self.point_4)
    
class Acero():

    diameter = {
        "3/8": 0.9525/100,
        "1/2": 1.27/100,
        "5/8": 1.5875/100,
        "3/4": 1.905/100,
        "1": 2.54/100,}
    
    diameter_list = ["3/8",
                     "1/2",
                     "5/8",
                     "3/4",
                     "1",]
    
    bar_area = {
        "3/8": 0.71,
        "1/2": 1.29,
        "5/8": 1.99,
        "3/4": 2.84,
        "1": 5.10,}

    def get_interfaz(self,acero_top, 
                     acero_under,
                     diametro_EST,
                     filas_superiores,
                     filas_inferiores,
                     barras_row1_top,
                     barras_row2_top,
                     barras_row3_top,
                     barras_row1_under,
                     barras_row2_under,
                     barras_row3_under,
                     s1_top,
                     s2_top,
                     s1_under,
                     s2_under,
                     long_gancho
                     ):
        
        self.acero_top = acero_top
        self.acero_under = acero_under
        self.diametro_EST = diametro_EST
        
        self.filas_superiores = filas_superiores
        self.filas_inferiores = filas_inferiores
        
        self.barras_row1_top = barras_row1_top
        self.barras_row2_top = barras_row2_top
        self.barras_row3_top = barras_row3_top
        
        self.barras_row1_under = barras_row1_under
        self.barras_row2_under = barras_row2_under
        self.barras_row3_under = barras_row3_under
        
        self.long_gancho = long_gancho
        
        if s1_top =="" and s2_top =="":
            self.top_e = 0
            self.top_e2 = 0
        elif s1_top =="":
            self.top_e = 0
            self.top_e2 = 0
        if s1_top !="":
            self.top_e = float(s1_top)
        if s2_top != "":
            self.top_e2 = float(s2_top)

        if s1_under == "" and s2_under == "":
            self.under_e = 0
            self.under_e2 = 0
        elif s1_under == "":
            self.under_e = 0
            self.under_e2 = 0
            
        if s1_under != "":
            self.under_e = float(s1_under)
        if s2_under != "":
            self.under_e2 = float(s2_under) 
            
    def get_lista_interfaz(self,lista_row1_top,
                           lista_row2_top,
                           lista_row3_top,
                           lista_row1_under,
                           lista_row2_under,
                           lista_row3_under,
                           nombre_viga):
        
        self.lista_row1_top = lista_row1_top
        self.lista_row2_top = lista_row2_top
        self.lista_row3_top = lista_row3_top
        
        self.lista_row1_under = lista_row1_under
        self.lista_row2_under = lista_row2_under
        self.lista_row3_under = lista_row3_under
        
        self.text_viga_name = nombre_viga
        
    def diameter_long_top(self):
        self.d_long_top = self.acero_top
        return self.diameter[self.d_long_top]
    
    def diameter_long_under(self):
        self.d_long_under = self.acero_under
        return self.diameter[self.d_long_under]
    
    def diameter_est(self):
        self.d_est = self.diametro_EST
        return self.diameter[self.d_est]
    
    def area(self, diameter):
        return self.bar_area[diameter]
    
    def row_tops(self):
        
        self.n_row_top = self.filas_superiores
        if  self.n_row_top == 1:
            self.n_bar_1_row1_top = self.barras_row1_top
            return self.n_bar_1_row1_top 
        
        elif self.n_row_top == 2:
            self.n_bar_1_row2_top = self.barras_row1_top
            self.n_bar_2_row2_top = self.barras_row2_top
            return self.n_bar_1_row2_top + self.n_bar_2_row2_top
            
        elif self.n_row_top == 3:
            self.n_bar_1_row3_top = self.barras_row1_top
            self.n_bar_2_row3_top = self.barras_row2_top
            self.n_bar_3_row3_top = self.barras_row3_top
            return self.n_bar_1_row3_top + self.n_bar_2_row3_top + self.n_bar_3_row3_top
        
    def row_under(self):
        self.n_row_under = self.filas_inferiores
        if self.n_row_under == 1:
            self.n_bar_1_row1_under = self.barras_row1_under
            return self.n_bar_1_row1_under
            
        elif self.n_row_under == 2:
            self.n_bar_1_row2_under = self.barras_row1_under
            self.n_bar_2_row2_under = self.barras_row2_under
            return self.n_bar_1_row2_under + self.n_bar_2_row2_under
            
        elif self.n_row_under == 3:
            self.n_bar_1_row3_under = self.barras_row1_under
            self.n_bar_2_row3_under = self.barras_row2_under
            self.n_bar_3_row3_under = self.barras_row3_under
            return self.n_bar_1_row3_under + self.n_bar_2_row3_under + self.n_bar_3_row3_under
                       
    def diameter_long_top_internal(self):
        diameter_list_internal_top = []
        self.diameter_internal_list_str_top = (self.lista_row1_top[1:-1]+
                                               self.lista_row2_top[:]+
                                               self.lista_row3_top[:])
        
        if self.n_row_top == 1:
            if self.n_bar_1_row1_top > 2 :
                self.bars_internal_top = self.n_bar_1_row1_top - 2
                for i in range(self.bars_internal_top):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_top[i]]
                    diameter_list_internal_top.append(diameter_internal)
                    
        elif self.n_row_top == 2:
            if self.n_bar_1_row2_top > 2 and self.n_bar_2_row2_top > 0 :
                self.bars_internal_top = self.n_bar_1_row2_top - 2
                #1 FILA
                for i in range(self.bars_internal_top):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_top[i]]
                    diameter_list_internal_top.append(diameter_internal) 
                #2 FILA
                for i in range(self.n_bar_2_row2_top):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_top
                                                      [i + self.bars_internal_top]]
                    diameter_list_internal_top.append(diameter_internal) 
                             
            elif self.n_bar_1_row2_top == 2 :
                #2 FILA
                if self.n_bar_2_row2_top > 0:
                    for i in range(self.n_bar_2_row2_top):
                        diameter_internal =self.diameter[self.diameter_internal_list_str_top[i]]
                        diameter_list_internal_top.append(diameter_internal)
                    
        elif self.n_row_top == 3:       
            
            if self.n_bar_1_row3_top > 2 and self.n_bar_2_row3_top > 0 and self.n_bar_3_row3_top > 0:
                self.bars_internal_top = self.n_bar_1_row3_top - 2
                #1 FILA
                for i in range(self.bars_internal_top):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_top[i]]
                    diameter_list_internal_top.append(diameter_internal) 
                #2 FILA
                for i in range(self.n_bar_2_row3_top):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_top
                                                      [i+self.bars_internal_top]]
                    diameter_list_internal_top.append(diameter_internal)
                #3 FILA    
                for i in range(self.n_bar_3_row3_top):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_top
                                                      [i+self.bars_internal_top+self.n_bar_2_row3_top]]
                    diameter_list_internal_top.append(diameter_internal)  
                
            elif self.n_bar_1_row3_top == 2 :
                if self.n_bar_2_row3_top > 0 and self.n_bar_2_row3_top >0 :
                    #2 FILA
                    for i in range(self.n_bar_2_row3_top):
                        diameter_internal = self.diameter[self.diameter_internal_list_str_top[i]]
                        diameter_list_internal_top.append(diameter_internal) 
                    #3 FILA 
                    for i in range(self.n_bar_3_row3_top):
                        diameter_internal = self.diameter[self.diameter_internal_list_str_top
                                                          [i+self.n_bar_2_row3_top]]
                        diameter_list_internal_top.append(diameter_internal) 
                    
        return diameter_list_internal_top
   
    def diameter_long_under_internal(self):
        diameter_list_internal_under = []
        self.diameter_internal_list_str_under = (self.lista_row1_under[1:-1]+
                                               self.lista_row2_under[:]+
                                               self.lista_row3_under[:])
        
        if self.n_row_under == 1:
            
            if self.n_bar_1_row1_under > 2 :
                self.bars_internal_under = self.n_bar_1_row1_under - 2
                for i in range(self.bars_internal_under):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_under[i]]
                    diameter_list_internal_under.append(diameter_internal) 
                    
        elif self.n_row_under== 2:
            
            if self.n_bar_1_row2_under >2 and self.n_bar_2_row2_under >0 :
                self.bars_internal_under = self.n_bar_1_row2_under - 2
                #1 FILA
                for i in range(self.bars_internal_under):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_under[i]]
                    diameter_list_internal_under.append(diameter_internal)     
                #2 FILA
                for i in range(self.n_bar_2_row2_under):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_under
                                                      [i + self.bars_internal_under]]
                    diameter_list_internal_under.append(diameter_internal) 
                      
            elif self.n_bar_1_row2_under == 2 :
                #2 FILA
                for i in range(self.n_bar_2_row2_under):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_under[i]]
                    diameter_list_internal_under.append(diameter_internal) 
                  
        elif self.n_row_under == 3:
            #1 FILA
            if self.n_bar_1_row3_under > 2 and self.n_bar_2_row3_under > 0 and self.n_bar_3_row3_under > 0:
                self.bars_internal_under = self.n_bar_1_row3_under - 2 

                for i in range(self.bars_internal_under):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_under[i]]
                    diameter_list_internal_under.append(diameter_internal) 
                #2 FILA
                for i in range(self.n_bar_2_row3_under):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_under
                                                      [i + self.bars_internal_under]]
                    diameter_list_internal_under.append(diameter_internal) 
                #3 FILA    
                for i in range(self.n_bar_3_row3_under):
                    diameter_internal = self.diameter[self.diameter_internal_list_str_under
                                                      [i+ self.bars_internal_under + self.n_bar_2_row3_under]]
                    diameter_list_internal_under.append(diameter_internal)
                
            elif self.n_bar_1_row3_under == 2 :
                
                if self.n_bar_2_row3_under > 0 and self.n_bar_2_row3_under > 0 :
                    #2 FILA
                    for i in range(self.n_bar_2_row3_under):
                        diameter_internal =self.diameter[self.diameter_internal_list_str_under[i]]
                        diameter_list_internal_under.append(diameter_internal) 
                    #3 FILA    
                    for i in range(self.n_bar_3_row3_under):
                        diameter_internal =self.diameter[self.diameter_internal_list_str_under
                                                         [i+self.n_bar_2_row3_under]]
                        diameter_list_internal_under.append(diameter_internal)        
        return diameter_list_internal_under

class Style():
    def __init__(self):
        comtypes.CoInitialize()
        self.acad = Autocad()
        self.doc = self.acad.doc
        self.apagado = False
    
    def selection_style_cotas(self):
        self.style = []
        for i in self.doc.DimStyles:
            self.style.append(i.name)
        return self.style 
    
    def selection_style_texto(self):
        self.text_style = []
        for i in self.doc.TextStyles:
            self.text_style.append(i.name)
        return self.text_style
    
    def get_style(self,dato1,dato2):
        self.estilo_texto = dato1
        self.estilo_cota = dato2   
      
class Viga(Acero,Seccion,Style):
    def __init__(self,b,h,r):
        comtypes.CoInitialize()
        Seccion.__init__(self,b,h,r)
    
    def get_diameter_long_top(self):
        return self.diameter_long_top()
    
    def get_diameter_long_under(self):
        return self.diameter_long_under()
    
    def get_diameter_e(self):
        return self.diameter_est()
    
    def get_row_tops(self):
        return self.row_tops()
    
    def get_row_unders(self):
        return self.row_under()
    
    def points_estribo_exterior(self):
        self.diameter_under = self.get_diameter_long_under()
        self.diameter_top = self.get_diameter_long_top()
        
        self.point1_e = AP(self.puntox + self.r,
                        self.puntoy +self.r + self.diameter_under/2,
                        0)
        self.point2_e = AP(self.puntox + self.r, 
                        self.puntoy + self.altura - self.r - self.diameter_top/2,
                        0)
        self.point3_e = AP(self.puntox + self.r + self.diameter_top/2, 
                        self.puntoy + self.altura - self.r,
                        0)
        self.point4_e = AP(self.puntox + self.base - self.r - self.diameter_top/2, 
                        self.puntoy + self.altura - self.r,
                        0)
        self.point5_e = AP(self.puntox + self.base - self.r,
                        self.puntoy + self.altura - self.r - self.diameter_top/2,
                        0)
        self.point6_e = AP(self.puntox + self.base - self.r,
                        self.puntoy + self.r + self.diameter_under/2,
                        0)
        self.point7_e = AP(self.puntox + self.base - self.r - self.diameter_under/2,
                        self.puntoy + self.r,
                        0)
        self.point8_e = AP(self.puntox + self.r + self.diameter_under/2,
                        self.puntoy + self.r,
                        0)
    
    def points_bow(self):
        self.point1_bow=AP(self.puntox + self.r + self.diameter_under/2,
                        self.puntoy +self.r + self.diameter_under/2,
                        0)
        self.point2_bow=AP(self.puntox + self.r + self.diameter_top/2 , 
                        self.puntoy + self.altura - self.r - self.diameter_top/2,
                        0)
        self.point3_bow=AP(self.puntox + self.base - self.r - self.diameter_top/2,
                        self.puntoy + self.altura - self.r - self.diameter_top/2,
                        0)
        self.point4_bow=AP(self.puntox + self.base - self.r - self.diameter_under/2,
                        self.puntoy + self.r + self.diameter_under/2,
                        0)
        
    def points_estribo_interior(self):

        self.diameter_estribo = self.get_diameter_e()

        self.point1_i = AP(self.puntox + self.r + self.diameter_estribo,
                        self.puntoy +self.r +  self.diameter_estribo + self.diameter_under/2,
                        0)
        self.point2_i = AP(self.puntox + self.r + self.diameter_estribo, 
                        self.puntoy + self.altura - self.r- self.diameter_estribo-self.diameter_top/2,
                        0)
        self.point3_i = AP(self.puntox + self.r + self.diameter_estribo+self.diameter_top/2, 
                        self.puntoy + self.altura - self.r - self.diameter_estribo,
                        0)
        self.point4_i = AP(self.puntox + self.base - self.r - self.diameter_estribo-self.diameter_top/2, 
                        self.puntoy + self.altura - self.r - self.diameter_estribo,
                        0)
        self.point5_i = AP(self.puntox + self.base - self.r - self.diameter_estribo,
                        self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2,
                        0)
        self.point6_i = AP(self.puntox + self.base - self.r - self.diameter_estribo,
                        self.puntoy + self.r + self.diameter_estribo+self.diameter_under/2,
                        0)
        self.point7_i = AP(self.puntox + self.base - self.r - self.diameter_estribo-self.diameter_under/2,
                        self.puntoy + self.r + self.diameter_estribo,
                        0)
        self.point8_i = AP(self.puntox + self.r + self.diameter_estribo+self.diameter_under/2,
                        self.puntoy + self.r + self.diameter_estribo,
                        0)
        
    def points_gancho(self):
        self.gancho_ext = AP(self.puntox + self.base - self.r - self.diameter_estribo-
                             (self.diameter_top/2*(1- cos(pi/4))),
                        self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2-
                        self.diameter_top/2*sin(pi/4),
                        0)
        self.gancho_ext_final = AP(self.puntox + self.base - self.r - self.diameter_estribo - self.long_gancho*cos(pi/4) - 
                                   self.diameter_top/2*cos(pi/4),
                        self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top / 2-
                        self.diameter_top/2*sin(pi/4) -self.long_gancho*cos(pi/4) ,
                        0)
        
        self.offsed_ext_inicial = AP(self.point5_i.x,self.gancho_ext.y-self.diameter_estribo)
        self.offsed_ext_final=AP(self.gancho_ext_final.x +(self.diameter_estribo*cos(44*pi/180) / sin(44*pi/180)/2),
                                 self.gancho_ext_final.y-self.diameter_estribo + 
                                 (self.diameter_estribo * cos(44*pi/180) / sin(44*pi/180))/2)
        
        
        self.gancho_int = AP(self.puntox + self.base - self.r - self.diameter_estribo-self.diameter_top/2 
                                                                -(self.diameter_top/2*sin(pi/4)
                                                                                       ),
                        self.puntoy + self.altura - self.r - self.diameter_estribo-(self.diameter_top/2*(1-cos(pi/4))),
                        0)
        self.gancho_int_final = AP(self.puntox + self.base - self.r - self.diameter_estribo-self.diameter_top/2-
                                                                (self.diameter_top/2*sin(pi/4))-self.long_gancho*cos(pi/4),
                        self.puntoy + self.altura - self.r - self.diameter_estribo-(self.long_gancho/(2**(1/2)))-
                        (self.diameter_top/2*(cos(pi/4))),
                        0)
        
        self.offsed_int_inicial = AP(self.gancho_int.x - self.diameter_estribo,self.point4_i.y)
        self.offsed_int_final=AP( self.gancho_int_final.x - (self.diameter_estribo*cos(44*pi/180)/sin(44*pi/180)/2) ,
                                 self.gancho_int_final.y + self.diameter_estribo - 
                                 (self.diameter_estribo * cos( * pi / 180) / sin(44 * pi / 180)) / 2)
        
    def points_circle(self):
        #Aceros superiores 
        self.point2_circle = AP(self.puntox + self.r + self.diameter_estribo + self.diameter_top / 2, 
                        self.puntoy + self.altura - self.r - self.diameter_estribo - self.diameter_top / 2,
                        0)
        self.point3_circle = AP(self.puntox + self.base - self.r - self.diameter_estribo - self.diameter_top / 2,
                        self.puntoy + self.altura - self.r - self.diameter_estribo - self.diameter_top / 2,
                        0)
        #Aceros inferiores 2
        self.point1_circle = AP(self.puntox + self.r + self.diameter_estribo + self.diameter_under / 2,
                        self.puntoy +self.r +  self.diameter_estribo + self.diameter_under / 2,
                        0)
        self.point4_circle = AP(self.puntox + self.base - self.r - self.diameter_estribo- self.diameter_under/2,
                        self.puntoy + self.r +  self.diameter_estribo + self.diameter_under / 2,
                        0)
        
    def draw_line_e(self):
        self.line_1_e = self.acad.model.AddLine(self.point1_e, self.point2_e)
        self.line_2_e = self.acad.model.AddLine(self.point3_e, self.point4_e)
        self.line_3_e = self.acad.model.AddLine(self.point5_e, self.point6_e)
        self.line_4_e = self.acad.model.AddLine(self.point7_e, self.point8_e)
        
    def draw_line_i(self):
        self.line_1_i = self.acad.model.AddLine(self.point1_i, self.point2_i)
        self.line_2_i = self.acad.model.AddLine(self.point3_i, self.point4_i)
        self.line_3_i = self.acad.model.AddLine(self.point5_i, self.point6_i)
        self.line_4_i = self.acad.model.AddLine(self.point7_i, self.point8_i)
        
    def draw_gancho(self):
        self.gancho_ext = self.acad.model.AddLine(self.gancho_ext, self.gancho_ext_final)
        self.gancho_ext_offsed = self.acad.model.AddLine( self.offsed_ext_inicial,  self.offsed_ext_final)
        self.gancho_int = self.acad.model.AddLine(self.gancho_int, self.gancho_int_final)  
        self.gancho_int_offsed = self.acad.model.AddLine(self.offsed_int_inicial, self.offsed_int_final)
        
        self.linea_union_ext = self.acad.model.AddLine(self.gancho_ext_final,self.offsed_ext_final)
        self.linea_union_int = self.acad.model.AddLine(self.gancho_int_final, self.offsed_int_final)
        
    def draw_bow(self):
        self.bow1=self.acad.model.AddArc(self.point1_bow,self.diameter_under/2,pi,3*pi/2)
        self.bow2=self.acad.model.AddArc(self.point2_bow,self.diameter_top/2,pi/2, pi)
        self.bow3=self.acad.model.AddArc(self.point3_bow,self.diameter_top/2,0,pi/2)
        self.bow4=self.acad.model.AddArc(self.point4_bow,self.diameter_under/2,3*pi/2,0)
        
    def draw_circle(self):
        self.circle1=self.acad.model.AddCircle(self.point1_circle,self.diameter_under/2)
        self.circle2=self.acad.model.AddCircle(self.point2_circle,self.diameter_top/2)
        self.circle3=self.acad.model.AddCircle(self.point3_circle,self.diameter_top/2)
        self.circle4=self.acad.model.AddCircle(self.point4_circle,self.diameter_under/2)
      
    def draw_circle_int_top(self):
        self.filas_top = self.get_row_tops()
        
        if self.n_row_top ==1:
            
            if self.filas_top>2:
                self.divisiones_top = (self.point3_circle.x-self.point2_circle.x)/(self.filas_top-1)
                i=0
                for j in self.diameter_long_top_internal():
                    i+=1
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.point2_circle.x+self.divisiones_top*i,
                                                                self.puntoy + self.altura - self.r- self.diameter_estribo-j/2,
                                        0) ,j/2)
                    
        elif self.n_row_top == 2:
            
            self.divisiones_top_row1 = (self.point3_circle.x-self.point2_circle.x)/(self.filas_top-1-self.n_bar_2_row2_top)
            
            j = self.diameter_long_top_internal()

            if self.n_bar_1_row2_top >2 and self.n_bar_2_row2_top >0:
                self.divisiones_top_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- j[-1]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_1_row2_top-2] /2))/(self.filas_top-1-self.n_bar_1_row2_top)
                #Se le resta 2 porque en la primera fijo es 2, si es 3 entonces se le resta 2, 
                # para que se realice solo una vuelta y agregue un acero más
                for i in range(self.n_bar_1_row2_top-2):
                    #Si esta bien el i, porque se debe multiplica por las divisiones + 1 porque 
                    #ya hay hacero en la primera fila
                    i+=1
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.point2_circle.x+self.divisiones_top_row1*i,
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-j[i-1] /2,
                                                                    0) ,j[i-1]/2)
                for i in range(self.n_bar_2_row2_top):
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_1_row2_top-2] /2
                                                                        +self.divisiones_top_row2*(i),
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2 - self.top_e,
                                                                    0) ,j[i+self.n_bar_1_row2_top-2]/2)
                    i+=1
            
            elif self.n_bar_1_row2_top ==2:
                self.divisiones_top_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- j[-1]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + j[0] /2))/(self.filas_top-1-self.n_bar_1_row2_top)
                
                for i in range(self.n_bar_2_row2_top):
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + j[0] /2
                                                                        +self.divisiones_top_row2*(i),
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2 - self.top_e,
                                                                    0) ,j[i]/2)
                    i+=1
                    
        elif self.n_row_top == 3:

            self.divisiones_top_row1 = (self.point3_circle.x-self.point2_circle.x)/(self.filas_top-1-self.n_bar_2_row3_top-self.n_bar_3_row3_top)
            j = self.diameter_long_top_internal()
            if self.n_bar_1_row3_top >2 and self.n_bar_2_row3_top >0 and self.n_bar_3_row3_top >0:

                self.divisiones_top_row1 = (self.point3_circle.x-self.point2_circle.x)/(self.filas_top-1-self.n_bar_2_row3_top-self.n_bar_3_row3_top)
            
                self.divisiones_top_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- j[self.n_bar_1_row3_top+self.n_bar_2_row3_top-3]/2)
                                          -(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_1_row3_top-2] /2))/(self.filas_top-1-self.n_bar_1_row3_top-self.n_bar_3_row3_top)

                self.divisiones_top_row3 = ((self.puntox + self.base - self.r - self.diameter_estribo- j[-1]/2)
                                          -(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_1_row3_top+self.n_bar_2_row3_top-2] /2))/(self.filas_top-1-self.n_bar_1_row3_top-self.n_bar_2_row3_top)
                
                for i in range(self.n_bar_1_row3_top-2):
                    
                    i+=1
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.point1_circle.x+self.divisiones_top_row1*i,
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-j[i-1] /2,
                                                                    0) ,j[i-1]/2)
                for i in range(self.n_bar_2_row3_top):
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_1_row3_top-2] /2 
                                                                        + self.divisiones_top_row2*i,
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2 - self.top_e,
                                                                    0) ,j[self.n_bar_1_row3_top+i-2]/2)   
                    i+=1
                for i in range(self.n_bar_3_row3_top):
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_1_row3_top+self.n_bar_2_row3_top-2] /2
                                                                        +self.divisiones_top_row3*i,
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2 - self.top_e - self.top_e2,
                                                                    0) ,j[self.n_bar_1_row3_top+self.n_bar_2_row3_top+i-2]/2)
                    i+=1
                    
            elif self.n_bar_1_row3_top ==2:

                self.divisiones_top_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- j[self.n_bar_2_row3_top-1]/2)
                                          -(self.puntox + self.r + self.diameter_estribo + j[0] /2))/(self.filas_top-3 - self.n_bar_3_row3_top)

                self.divisiones_top_row3 = ((self.puntox + self.base - self.r - self.diameter_estribo- j[-1]/2)
                                          -(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_2_row3_top] /2))/(self.filas_top- 3- self.n_bar_2_row3_top)
                
                for i in range(self.n_bar_2_row3_top):
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + j[0] /2 
                                                                        + self.divisiones_top_row2*i,
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2 - self.top_e,
                                                                    0) ,j[i]/2)   
                    i+=1
                for i in range(self.n_bar_3_row3_top):
                    self.circle1_int_top=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + j[self.n_bar_2_row3_top] /2
                                                                        +self.divisiones_top_row3*i,
                                                                    self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2 - self.top_e - self.top_e2,
                                                                    0) ,j[self.n_bar_2_row3_top+i]/2)
                    i+=1
         
    def draw_circle_int_under(self):
        self.filas_under = self.get_row_unders()
        if self.n_row_under ==1:
            if  self.filas_under>2:
                self.divisiones_under = (self.point4_circle.x-self.point1_circle.x)/( self.filas_under-1)
                i=0
                self.k_under = self.diameter_long_under_internal()
                for self.k_under in self.k_under:
                    i+=1
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.point1_circle.x+self.divisiones_under*i,
                                                                self.puntoy + self.r +  self.diameter_estribo+self.k_under/2,
                                                                0) ,self.k_under/2)
        
        elif self.n_row_under == 2:
            
            self.divisiones_under_row1 = (self.point4_circle.x-self.point1_circle.x)/( self.filas_under-1-self.n_bar_2_row2_under)
            self.k_under = self.diameter_long_under_internal()
            if self.n_bar_1_row2_under >2 and self.n_bar_2_row2_under >0:
                self.divisiones_under_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- self.k_under[-1]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + self.k_under[-self.n_bar_1_row2_under] /2))/( self.filas_under-1-self.n_bar_1_row2_under)
                
                for i in range(self.n_bar_1_row2_under-2):
                    i+=1
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.point1_circle.x+self.divisiones_under_row1*i,
                                                                    self.puntoy + self.r +  self.diameter_estribo+self.k_under[i-1]/2,
                                                                    0) ,self.k_under[i-1]/2)
                
                for i in range(self.n_bar_2_row2_under):
                    
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + self.k_under[self.n_bar_1_row2_under-2] /2
                                                                        +self.divisiones_under_row2*(i),
                                                                    self.puntoy + self.r +  self.diameter_estribo+ self.diameter_under/2 + self.under_e,
                                                                    0) ,self.k_under[self.n_bar_1_row2_under+i-2]/2)
                    i+=1
                    
            elif self.n_bar_1_row2_under ==2:
                self.divisiones_under_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- self.k_under[-1]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + self.k_under[0] /2))/( self.filas_under-1-self.n_bar_1_row2_under)
                
                for i in range(self.n_bar_2_row2_under):
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + self.k_under[0] /2
                                                                            +self.divisiones_under_row2*(i),
                                                                        self.puntoy + self.r +  self.diameter_estribo+ self.diameter_under/2 + self.under_e,
                                                                        0) ,self.k_under[i]/2)
                    i+=1
        
        elif self.n_row_under == 3:
            
            self.divisiones_under_row1 = (self.point4_circle.x-self.point1_circle.x)/( self.filas_under-1-self.n_bar_2_row3_under-self.n_bar_3_row3_under)
            self.k_under = self.diameter_long_under_internal()
            if self.n_bar_1_row3_under >2 and self.n_bar_2_row3_under >0 and self.n_bar_3_row3_under >0:
                
                self.divisiones_under_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- self.k_under[self.n_bar_1_row3_under+self.n_bar_2_row3_under-3]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + self.k_under[self.n_bar_1_row3_under-2] /2))/( self.filas_under-1-self.n_bar_1_row3_under-self.n_bar_3_row3_under)

                self.divisiones_under_row3 = ((self.puntox + self.base - self.r - self.diameter_estribo- self.k_under[-1]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + self.k_under[self.n_bar_1_row3_under+self.n_bar_2_row3_under-2] /2))/( self.filas_under-1-self.n_bar_1_row3_under-self.n_bar_2_row3_under)
                
                for i in range(self.n_bar_1_row3_under-2):
                    i+=1
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.point1_circle.x+self.divisiones_under_row1*i,
                                                                    self.puntoy + self.r +  self.diameter_estribo+self.k_under[i-1]/2,
                                                                    0) ,self.k_under[i-1]/2)
                for i in range(self.n_bar_2_row3_under):
                    
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + self.k_under[self.n_bar_1_row3_under-2] /2 
                                                                        + self.divisiones_under_row2*i,
                                                                    self.puntoy + self.r +  self.diameter_estribo+self.diameter_under/2 + self.under_e,
                                                                    0) ,self.k_under[self.n_bar_1_row3_under+i-2]/2)   
                    i+=1
                for i in range(self.n_bar_3_row3_under):
                    
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + self.k_under[self.n_bar_1_row3_under+self.n_bar_2_row3_under-2] /2
                                                                        +self.divisiones_under_row3*i,
                                                                    self.puntoy + self.r + self.diameter_estribo + self.diameter_under/2 + self.under_e +self.under_e2,
                                                                    0) ,self.k_under[self.n_bar_1_row3_under+self.n_bar_2_row3_under+i-2]/2)
                    i+=1
            
            elif self.n_bar_1_row3_under ==2:

                self.divisiones_under_row2 = ((self.puntox + self.base - self.r - self.diameter_estribo- self.k_under[self.n_bar_2_row3_under-1]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + self.k_under[0] /2))/( self.filas_under-3 - self.n_bar_3_row3_under)

                self.divisiones_under_row3 = ((self.puntox + self.base - self.r - self.diameter_estribo- self.k_under[-1]/2)
                                            -(self.puntox + self.r + self.diameter_estribo + self.k_under[self.n_bar_2_row3_under] /2))/( self.filas_under- 3- self.n_bar_2_row3_under)

                for i in range(self.n_bar_2_row3_under):
                    
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + self.k_under[0] /2 
                                                                        + self.divisiones_under_row2*i,
                                                                    self.puntoy + self.r +  self.diameter_estribo+self.diameter_under/2 + self.under_e,
                                                                    0) ,self.k_under[i]/2)   
                    i+=1
                for i in range(self.n_bar_3_row3_under):
                    
                    self.circle1_int_under=self.acad.model.AddCircle(AP(self.puntox + self.r + self.diameter_estribo + self.k_under[self.n_bar_2_row3_under] /2
                                                                        +self.divisiones_under_row3*i,
                                                                    self.puntoy + self.r + self.diameter_estribo + self.diameter_under/2 + self.under_e +self.under_e2,
                                                                    0) ,self.k_under[self.n_bar_2_row3_under+i]/2)
                    i+=1
        
    def draw_dimensions(self):
        self.style_selection = self.estilo_cota
        self.point_base = AP(self.puntox,self.puntoy,0)
        self.point_2 = AP(self.puntox,self.puntoy + self.altura,0)
        self.point_3 = AP(self.puntox + self.base ,self.puntoy,0)
        self.gancho_ext = AP(self.puntox + self.base - self.r - self.diameter_estribo-(self.diameter_top/2*(1- cos(pi/4))),
                        self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2-
                        self.diameter_top/2*sin(pi/4),
                        0)
        self.gancho_ext_final = AP(self.puntox + self.base - self.r - self.diameter_estribo-self.long_gancho*cos(pi/4)-self.diameter_top/2*cos(pi/4),
                        self.puntoy + self.altura - self.r - self.diameter_estribo-self.diameter_top/2-
                        self.diameter_top/2*sin(pi/4) -self.long_gancho*cos(pi/4) ,
                        0)
        
        self.cota_y = self.acad.model.AddDimAligned(self.point_base, self.point_2, AP(self.puntox - 0.05, self.altura / 2, 0))
        self.cota_x = self.acad.model.AddDimAligned(self.point_base, self.point_3, AP(self.base / 2, self.puntoy - 0.05, 0))
        self.cota_gancho = self.acad.model.AddDimAligned(self.gancho_ext,self.gancho_ext_final,
                                                         AP(self.gancho_ext.x,
                                                            self.gancho_ext.y,0),
                                                         )
        
        self.point3_e = AP(self.puntox + self.r + self.diameter_top/2, 
                        self.puntoy + self.altura - self.r,
                        0)
        self.point4_e = AP(self.puntox + self.base - self.r - self.diameter_top/2, 
                        self.puntoy + self.altura - self.r,
                        0)
        
        self.guide_line_est = self.acad.model.AddLine( AP(self.point3_e.x + (self.point4_e.x-self.point3_e.x)/2,self.point3_e.y,0 ),
                                                                AP(self.point3_e.x + (self.point4_e.x-self.point3_e.x)/2,
                                                                   self.point3_e.y + self.diameter_estribo + self.r + 0.02,0))
        self.text_est = self.acad.model.AddText(f"Ø{self.diametro_EST}", 
                                                        AP(self.point3_e.x + (self.point4_e.x-self.point3_e.x)/2,
                                                                   self.point3_e.y + self.diameter_estribo + self.r + 0.02,0),
                                                        0.02)  
        
        self.text_viga = self.acad.model.AddText(f"VIGA {self.text_viga_name}", 
                                                        AP(self.puntox, self.puntoy - 0.11,0),
                                                        0.03)
        self.cota_y.StyleName = self.style_selection
        self.cota_x.StyleName = self.style_selection
        self.cota_gancho.StyleName = self.style_selection
        
    def draw_diameters_top(self):
        
        self.text_style_selection = self.estilo_texto

        if self.n_row_top ==1:
            if self.filas_top>2:
                repetidos = {}
                list_top = self.diameter_internal_list_str_top
                for elemento in self.diameter_list:
                    contador = list_top.count(elemento)
                    repetidos[elemento] = contador
                text_2= ''
                text = ''
                a = True
                if a == True:
                    for elemento, contador in repetidos.items():
                        if elemento == str(Fraction(self.d_long_top)) and contador>0:
                            text = f"{contador+2} Ø{elemento}"
                            a = False
                            for elemento, contador in repetidos.items():
                                if contador >0 and elemento != str(Fraction(self.d_long_top)):
                                    text_1 = f"{contador}Ø{elemento}"
                                    text_2+= f" + {text_1}"
                    text_final = text + text_2 
                if a == True:
                    for elemento, contador in repetidos.items(): 
                        if contador >0:           
                            text_1 = f"{contador}Ø{elemento}"
                            text_2+= f" + {text_1}"
                    text = f"{2}Ø{self.d_long_top}"
                    text_final = text + text_2   
                                
                self.guide_line_top = self.acad.model.AddLine( self.point3_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01,0),
                                                        0.02)        
                self.text_top.StyleName = self.text_style_selection      
            else:
                self.guide_line_top = self.acad.model.AddLine( self.point3_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y,0))
                
                self.text_top = self.acad.model.AddText(f"{self.n_bar_1_row1_top} Ø{self.d_long_top}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
            
        elif self.n_row_top ==2:
            repetidos_row2 = {}
            lista_completa = self.diameter_internal_list_str_top
            list_top_row2 = lista_completa[self.n_bar_1_row2_top-2 :]
            
            for elemento in self.diameter_list:
                contador = list_top_row2.count(elemento)
                repetidos_row2[elemento] = contador
            
            if self.n_bar_1_row2_top > 2 and self.n_bar_2_row2_top > 0 :
                repetidos_row1 = {}
                #Lista de la primera fila, añadiendo los dos diametros de los extremos 
                list_top_row1 = [self.d_long_top,
                                self.d_long_top]+lista_completa[:self.n_bar_1_row2_top-2]          
                for elemento in self.diameter_list:
                    contador = list_top_row1.count(elemento)
                    repetidos_row1[elemento] = contador 
                text_2= ''
                text = ''
                a = True
                #Para la primera fila cuando hay mas de dos aceros en dicha fila
                if a == True:
                    for elemento, contador in repetidos_row1.items():
                        if elemento == str(Fraction(self.d_long_top)) and contador>0:
                            text = f"{contador} Ø{elemento}"
                            a = False
                            for elemento, contador in repetidos_row1.items():
                                if contador >0 and elemento != str(Fraction(self.d_long_top)):
                                    text_1 = f"{contador}Ø{elemento}"
                                    text_2+= f" + {text_1}"
                    text_final = text + text_2

                self.guide_line_top = self.acad.model.AddLine( self.point3_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y,0))
                
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01,0),
                                                        0.02)
                
                self.text_top.StyleName = self.text_style_selection
                #Para la segunda fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_row2.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
                            
                            text_2 += f"{text_1}"
                    
                    text_final = text_2

                self.guide_line_top = self.acad.model.AddLine( AP(self.point3_circle.x,self.point3_circle.y-self.top_e),
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y-self.top_e,0))
                
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01-self.top_e,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
                
            elif self.n_bar_1_row2_top == 2:
                
                text_final = f"{2}Ø{self.d_long_top}"
                #Para la primera fila
                self.guide_line_top = self.acad.model.AddLine( self.point3_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_row2.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = "+"
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
                            text_2 += f"{text_1}"
                    text_final = text_2
                self.guide_line_top = self.acad.model.AddLine( AP(self.point3_circle.x,self.point3_circle.y-self.top_e),
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y-self.top_e,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01-self.top_e,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection 
       
        elif self.n_row_top ==3:
            repetidos_bar2_row3 = {}
            repetidos_bar3_row3 = {}
            lista_completa = self.diameter_internal_list_str_top
            list_top_bar2_row3 = lista_completa[self.n_bar_1_row3_top-2 : self.n_bar_1_row3_top+self.n_bar_2_row3_top-2]
            list_top_bar3_row3 = lista_completa[self.n_bar_1_row3_top+self.n_bar_2_row3_top-2 :]
            for elemento in self.diameter_list:
                contador = list_top_bar2_row3.count(elemento)
                repetidos_bar2_row3[elemento] = contador
                
            for elemento in self.diameter_list:
                contador = list_top_bar3_row3.count(elemento)
                repetidos_bar3_row3[elemento] = contador
                
            if self.n_bar_1_row3_top > 2 and self.n_bar_2_row3_top > 0 and self.n_bar_3_row3_top > 0:
                repetidos_bar1_row1 = {}
                #Lista de la primera fila, añadiendo los dos diametros de los extremos 
                list_top_row1 = [self.d_long_top,
                                self.d_long_top]+lista_completa[:self.n_bar_1_row3_top-2]          
                
                for elemento in self.diameter_list:
                    contador = list_top_row1.count(elemento)
                    repetidos_bar1_row1[elemento] = contador 
                text_2= ''
                text = ''
                a = True
                #Para la primera fila cuando hay mas de dos aceros en dicha fila
                if a == True:
                    for elemento, contador in repetidos_bar1_row1.items():
                        if elemento == str(Fraction(self.d_long_top)) and contador>0:
                            text = f"{contador} Ø{elemento}"
                            a = False
                            for elemento, contador in repetidos_bar1_row1.items():
                                if contador >0 and elemento != str(Fraction(self.d_long_top)):
                                    text_1 = f"{contador}Ø{elemento}"
                                    text_2+= f" + {text_1}"
                    text_final = text + text_2
                    
                self.guide_line_top = self.acad.model.AddLine( self.point3_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
                #Para la segunda fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar2_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_top = self.acad.model.AddLine( AP(self.point3_circle.x,self.point3_circle.y-self.top_e),
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y-self.top_e,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01-self.top_e,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
                #Para la tercera fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar3_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_top = self.acad.model.AddLine( AP(self.point3_circle.x,self.point3_circle.y-self.top_e-self.top_e2),
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y-self.top_e-self.top_e2,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01-self.top_e-self.top_e2,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
            
            elif self.n_bar_1_row3_top == 2:
                
                text_final = f"{2}Ø{self.d_long_top}"
                #Para la primera fila
                self.guide_line_top = self.acad.model.AddLine( self.point3_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
                #Para la segunda fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar2_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_top = self.acad.model.AddLine( AP(self.point3_circle.x,self.point3_circle.y-self.top_e),
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y-self.top_e,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01-self.top_e,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
                #Para la tercera fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar3_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_top = self.acad.model.AddLine( AP(self.point3_circle.x,self.point3_circle.y-self.top_e-self.top_e2),
                                                                AP(self.puntox + self.base + 0.01, self.point3_circle.y-self.top_e-self.top_e2,0))
                self.text_top = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point3_circle.y-0.01-self.top_e-self.top_e2,0),
                                                        0.02)
                self.text_top.StyleName = self.text_style_selection
        
    def draw_diameters_under(self):
        self.text_style_selection = self.estilo_texto

        if self.n_row_under ==1:
            if  self.filas_under>2:
                repetidos = {}
                list_under = self.diameter_internal_list_str_under
                for elemento in self.diameter_list:
                    contador = list_under.count(elemento)
                    repetidos[elemento] = contador
                text_2= ''
                text = ''
                a = True
                if a == True:
                    for elemento, contador in repetidos.items():
                        if elemento == str(Fraction(self.d_long_under)) and contador>0:
                            text = f"{contador+2} Ø{elemento}"
                            a = False
                            for elemento, contador in repetidos.items():
                                if contador >0 and elemento != str(Fraction(self.d_long_under)):
                                    text_1 = f"{contador}Ø{elemento}"
                                    text_2+= f" + {text_1}"
                    text_final = text + text_2 
                if a == True:
                    for elemento, contador in repetidos.items(): 
                        if contador >0:           
                            text_1 = f"{contador}Ø{elemento}"
                            text_2+= f" + {text_1}"
                    text = f"{2}Ø{self.d_long_under}"
                    text_final = text + text_2   
                                
                self.guide_line_under = self.acad.model.AddLine( self.point4_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01,0),
                                                        0.02)        
                self.text_under.StyleName = self.text_style_selection      
            else:
                self.guide_line_under = self.acad.model.AddLine( self.point4_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y,0))
                
                self.text_under = self.acad.model.AddText(f"{self.n_bar_1_row1_under} Ø{self.d_long_under}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
            
        elif self.n_row_under ==2:
            repetidos_row2 = {}
            lista_completa = self.diameter_internal_list_str_under
            list_under_row2 = lista_completa[self.n_bar_1_row2_under-2 :]
            
            for elemento in self.diameter_list:
                contador = list_under_row2.count(elemento)
                repetidos_row2[elemento] = contador
            
            if self.n_bar_1_row2_under > 2 and self.n_bar_2_row2_under > 0 :
                repetidos_row1 = {}
                #Lista de la primera fila, añadiendo los dos diametros de los extremos 
                list_under_row1 = [self.d_long_under,
                                self.d_long_under]+lista_completa[:self.n_bar_1_row2_under-2]          
                for elemento in self.diameter_list:
                    contador = list_under_row1.count(elemento)
                    repetidos_row1[elemento] = contador 
                text_2= ''
                text = ''
                a = True
                #Para la primera fila cuando hay mas de dos aceros en dicha fila
                if a == True:
                    for elemento, contador in repetidos_row1.items():
                        if elemento == str(Fraction(self.d_long_under)) and contador>0:
                            text = f"{contador} Ø{elemento}"
                            a = False
                            for elemento, contador in repetidos_row1.items():
                                if contador >0 and elemento != str(Fraction(self.d_long_under)):
                                    text_1 = f"{contador}Ø{elemento}"
                                    text_2+= f" + {text_1}"
                    text_final = text + text_2

                self.guide_line_under = self.acad.model.AddLine( self.point4_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y,0))
                
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01,0),
                                                        0.02)
                
                self.text_under.StyleName = self.text_style_selection
                #Para la segunda fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_row2.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
                            
                            text_2 += f"{text_1}"
                    
                    text_final = text_2

                self.guide_line_under = self.acad.model.AddLine( AP(self.point4_circle.x, self.point4_circle.y + self.under_e),
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y + self.under_e,0))
                
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01 + self.under_e,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
                
            elif self.n_bar_1_row2_under == 2:
                
                text_final = f"{2}Ø{self.d_long_under}"
                #Para la primera fila
                self.guide_line_under = self.acad.model.AddLine( self.point4_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_row2.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = "+"
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
                            text_2 += f"{text_1}"
                    text_final = text_2
                self.guide_line_under = self.acad.model.AddLine( AP(self.point4_circle.x, self.point4_circle.y + self.under_e),
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y + self.under_e,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01 + self.under_e,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection 
       
        elif self.n_row_under == 3:
            repetidos_bar2_row3 = {}
            repetidos_bar3_row3 = {}
            lista_completa = self.diameter_internal_list_str_under
            list_under_bar2_row3 = lista_completa[self.n_bar_1_row3_under-2 : self.n_bar_1_row3_under+self.n_bar_2_row3_under-2]
            list_under_bar3_row3 = lista_completa[self.n_bar_1_row3_under+self.n_bar_2_row3_under-2 :]
            
            for elemento in self.diameter_list:
                contador = list_under_bar2_row3.count(elemento)
                repetidos_bar2_row3[elemento] = contador
            for elemento in self.diameter_list:
                contador = list_under_bar3_row3.count(elemento)
                repetidos_bar3_row3[elemento] = contador
                
            if self.n_bar_1_row3_under > 2 and self.n_bar_2_row3_under > 0 and self.n_bar_3_row3_under > 0:
                repetidos_bar1_row1 = {}
                #Lista de la primera fila, añadiendo los dos diametros de los extremos 
                list_under_row1 = [self.d_long_under,
                                self.d_long_under]+lista_completa[:self.n_bar_1_row3_under-2]          
                
                for elemento in self.diameter_list:
                    contador = list_under_row1.count(elemento)
                    repetidos_bar1_row1[elemento] = contador 
                text_2= ''
                text = ''
                a = True
                #Para la primera fila cuando hay mas de dos aceros en dicha fila
                if a == True:
                    for elemento, contador in repetidos_bar1_row1.items():
                        if elemento == str(Fraction(self.d_long_under)) and contador>0:
                            text = f"{contador} Ø{elemento}"
                            a = False
                            for elemento, contador in repetidos_bar1_row1.items():
                                if contador >0 and elemento != str(Fraction(self.d_long_under)):
                                    text_1 = f"{contador}Ø{elemento}"
                                    text_2+= f" + {text_1}"
                    text_final = text + text_2
                    
                self.guide_line_under = self.acad.model.AddLine( self.point4_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
                #Para la segunda fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar2_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_under = self.acad.model.AddLine( AP(self.point4_circle.x, self.point4_circle.y + self.under_e),
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y + self.under_e,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01 + self.under_e,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
                #Para la tercera fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar3_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_under = self.acad.model.AddLine( AP(self.point4_circle.x, self.point4_circle.y + self.under_e + self.under_e2),
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y + self.under_e + self.under_e2,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01 + self.under_e + self.under_e2,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
            
            elif self.n_bar_1_row3_under == 2:
                
                text_final = f"{2}Ø{self.d_long_under}"
                #Para la primera fila
                self.guide_line_under = self.acad.model.AddLine( self.point4_circle,
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
                #Para la segunda fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar2_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_under = self.acad.model.AddLine( AP(self.point4_circle.x,self.point4_circle.y + self.under_e),
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y + self.under_e,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01 + self.under_e,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection
                #Para la tercera fila
                a=True
                if a == True:
                    first_iteration = True
                    text_2 = ""
                    text = ""
                    for elemento, contador in repetidos_bar3_row3.items():
                        if contador > 0:
                            text_1 = f"{contador}Ø{elemento}"
                            if not first_iteration:
                                suma = " + "
                                text_2 += f"{suma}"
                            else:
                                first_iteration = False
    
                            text_2 += f"{text_1}"
                    text_final = text_2
                    
                self.guide_line_under = self.acad.model.AddLine( AP(self.point4_circle.x, self.point4_circle.y + self.under_e + self.under_e2),
                                                                AP(self.puntox + self.base + 0.01, self.point4_circle.y + self.under_e + self.under_e2,0))
                self.text_under = self.acad.model.AddText(f"{text_final}", 
                                                        AP(self.puntox + self.base + 0.015, self.point4_circle.y - 0.01 + self.under_e + self.under_e2,0),
                                                        0.02)
                self.text_under.StyleName = self.text_style_selection