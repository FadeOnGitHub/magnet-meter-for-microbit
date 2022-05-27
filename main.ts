control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_EVT_ANY, function on_microbit_id_button_a_evt() {
    if (input.magneticForce(Dimension.Strength) < 0 && input.magneticForce(Dimension.Strength) < 20) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
        `)
    } else if (input.magneticForce(Dimension.Strength) > 20 && input.magneticForce(Dimension.Strength) < 40) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
        `)
    } else if (input.magneticForce(Dimension.Strength) > 40 && input.magneticForce(Dimension.Strength) < 60) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
        `)
    } else if (input.magneticForce(Dimension.Strength) > 60 && input.magneticForce(Dimension.Strength) < 80) {
        basic.showLeds(`
            . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        `)
    } else if (input.magneticForce(Dimension.Strength) > 80 && input.magneticForce(Dimension.Strength) < 100) {
        basic.showLeds(`
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        `)
    } else {
        basic.showLeds(`
            # . # . #
                        # . # . #
                        # . # . #
                        . . . . .
                        # . # . #
        `)
    }
    
})
basic.showString("MAGNET METER")
basic.showLeds(`
    . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
`)
control.waitMicros(48)
basic.clearScreen()
basic.showLeds(`
    . # # # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
`)
control.raiseEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_EVT_ANY)
basic.forever(function on_forever() {
    if (input.buttonIsPressed(Button.AB)) {
        basic.showLeds(`
            # # # # #
                        # . . . .
                        # . # . #
                        # . . . .
                        # # # # #
        `)
        music.playMelody("E F G A G - B C5 ", 500)
    }
    
})
