from adafruit_hid.keycode import Keycode as kc
from adafruit_hid.consumer_control_code import ConsumerControlCode as cc


STRING = 1
KEY = 2
CONTROL_CODE = 3

keys = [
    # ROW 1, COLUMN 1
    (STRING, "Button 1"),
    # ROW 1, COLUMN 2
    (KEY, [kc.GUI, kc.C]),
    # ROW 1, COLUMN 3
    (KEY, [kc.GUI, kc.V]),
    # ROW 1, COLUMN 4
    (STRING, "Button 4"),
    # ROW 2, COLUMN 1
    (STRING, "Button 5"),
    # ROW 2, COLUMN 2
    (STRING, "Button 6"),
    # ROW 2, COLUMN 3
    (STRING, "Button 7"),
    # ROW 2, COLUMN 4
    (CONTROL_CODE, cc.VOLUME_INCREMENT),
    # ROW 3, COLUMN 1
    (STRING, "Button 9"),
    # ROW 3, COLUMN 2
    (STRING, "Button 10"),
    # ROW 3, COLUMN 3
    (STRING, "Button 11"),
    # ROW 3, COLUMN 4
    (CONTROL_CODE, cc.VOLUME_DECREMENT)
]

