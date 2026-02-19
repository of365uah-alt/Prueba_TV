import arcade

arcade.open_window(800, 600, "Dibujo Pancho")

# pone el fondo en blanco
arcade.set_background_color((3, 194, 252))
arcade.start_render() # empieza el renderizado
arcade.draw_lbwh_rectangle_filled(0, 0, 1200, 250, (255, 221, 0)) # dibuja el suelo
def draw_tank(x,y, scale):
    # dibuja el tanque
    ## cuerpo del tanque
    arcade.draw_lbwh_rectangle_filled(x,y, 200*scale, 75*scale, (44, 71, 48)) 
    arcade.draw_lbwh_rectangle_filled(x+50*scale, y+75*scale, 100*scale, 25*scale, (44, 71, 48))

    # ruedas del tanque
    arcade.draw_circle_filled(x+25*scale, y, 25*scale, (73, 105, 89))
    arcade.draw_circle_filled(x+75*scale, y, 25*scale, (73, 105, 89))
    arcade.draw_circle_filled(x+125*scale, y, 25*scale, (73, 105, 89))
    arcade.draw_circle_filled(x+175*scale, y, 25*scale, (73, 105, 89))
    arcade.draw_arc_outline(x+25*scale, y, 50*scale, 50*scale, (13, 15, 14), 90, 270, 10*scale)
    arcade.draw_arc_outline(x+175*scale, y, 50*scale, 50*scale, (13, 15, 14), 90, 270, 10*scale, 180)
    arcade.draw_line(x+25*scale, y+25*scale, x+175*scale, y+25*scale, (13, 15, 14), 5*scale)
    arcade.draw_line(x+25*scale, y-25*scale, x+175*scale, y-25*scale, (13, 15, 14), 5*scale)

    # Cañon del tanque
    arcade.draw_line(x +150*scale, y+82*scale, x+250*scale, y+82*scale, (44, 71, 48), 10*scale)

draw_tank(100, 250, 0.5) # dibuja el tanque en la posición (100, 250) con escala 1/2


arcade.finish_render() # termina el renderizado
arcade.run() # corre el programa

