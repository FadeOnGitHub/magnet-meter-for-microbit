def on_microbit_id_button_a_evt():
    if input.magnetic_force(Dimension.STRENGTH) < 0 and input.magnetic_force(Dimension.STRENGTH) < 20:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
        """)
    elif input.magnetic_force(Dimension.STRENGTH) > 20 and input.magnetic_force(Dimension.STRENGTH) < 40:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
        """)
    elif input.magnetic_force(Dimension.STRENGTH) > 40 and input.magnetic_force(Dimension.STRENGTH) < 60:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif input.magnetic_force(Dimension.STRENGTH) > 60 and input.magnetic_force(Dimension.STRENGTH) < 80:
        basic.show_leds("""
            . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif input.magnetic_force(Dimension.STRENGTH) > 80 and input.magnetic_force(Dimension.STRENGTH) < 100:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        basic.show_leds("""
            # . # . #
                        # . # . #
                        # . # . #
                        . . . . .
                        # . # . #
        """)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_EVT_ANY,
    on_microbit_id_button_a_evt)

basic.show_string("MAGNET METER")
basic.show_leds("""
    . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
""")
control.wait_micros(48)
basic.clear_screen()
basic.show_leds("""
    . # # # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
""")
control.raise_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_EVT_ANY)

def on_forever():
    if input.button_is_pressed(Button.AB):
        basic.show_leds("""
            # # # # #
                        # . . . .
                        # . # . #
                        # . . . .
                        # # # # #
        """)
        music.play_melody("E F G A G - B C5 ", 500)
basic.forever(on_forever)
