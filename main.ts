radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    count += receivedNumber
    array[n] = receivedNumber
    n += 1
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    count += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(count)
})
let count = 0
let n = 0
let array = [0, 0, 0, 0, 0]
forever(function on_forever() {
    basic.showNumber(count)
    if (array[4] != 0) {
        for (let i = 0; i < 5; i++) {
            basic.showNumber(array[i])
        }
        basic.showString("SUM: " + count)
        control.reset()
    }
    
})
