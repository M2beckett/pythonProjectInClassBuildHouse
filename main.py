import arcade

my_window = arcade.open_window(800,650, "Our First Window Demo")
arcade.set_background_color(arcade.color.BLUEBERRY)

arcade.start_render()
arcade.draw_xywh_rectangle_filled(1, 1, 880, 150, arcade.color.APPLE_GREEN)
#building
arcade.draw_xywh_rectangle_filled(10, 10, 380, 250, arcade.color.BLACK)
#door
arcade.draw_xywh_rectangle_filled(200, 16, 130, 200, arcade.color.CANDY_APPLE_RED)
#window frame
arcade.draw_xywh_rectangle_outline(60, 100, 120, 100, arcade.color.BISTRE_BROWN, 6)
#glass to window
arcade.draw_xywh_rectangle_filled(64, 104, 110, 94, arcade.color.ALICE_BLUE)
#chimney
arcade.draw_xywh_rectangle_filled(20, 260, 80, 140, arcade.color.CARMINE_RED)
#door Knob
arcade.draw_circle_filled(300, 120, 10, arcade.color.ALLOY_ORANGE)
#roof
arcade.draw_triangle_filled(10, 260, 220, 460, 395, 260, arcade.color.ANTIQUE_BRONZE)
arcade.finish_render()
arcade.run()