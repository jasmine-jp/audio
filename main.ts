radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    count += receivedNumber
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    count += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(count)
})
let count = 0
forever(function on_forever() {
    basic.showNumber(count, 1)
})
