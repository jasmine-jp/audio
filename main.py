def on_received_number(receivedNumber):
    global count, array, n
    count += receivedNumber
    array[n] = receivedNumber
    n += 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global count
    count += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(count)
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0
n = 0
array = [0, 0, 0, 0, 0]

def on_forever():
    basic.show_number(count)
    if array[4] != 0:
        for i in range(5):
            basic.show_number(array[i])
        basic.show_string("SUM: " + count)
        control.reset()
forever(on_forever)
