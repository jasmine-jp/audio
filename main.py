def on_received_number(receivedNumber):
    global count
    count += receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global count
    count += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(count)
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0

def on_forever():
    basic.show_number(count)
forever(on_forever)
