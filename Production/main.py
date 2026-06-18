import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.encoder import Encoder
from kmk.extensions.peg_oled import Oled, OledDisplayMode, OledReactionType

keyboard = KMKKeyboard()

keyboard.row_pins = (board.D8, board.D9, board.D10)
keyboard.col_pins = (board.D3, board.D6, board.D7)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = Encoder()
keyboard.extensions.append(encoder)

encoder.pin_a = board.D0
encoder.pin_b = board.D1

encoder.map = [
    ((KC.VOLU, KC.VOLD),)
]

oled_ext = Oled(
    OledDisplayMode.TXT,
    to_display=OledReactionType.LAYER,
    flip=False,
)
keyboard.extensions.append(oled_ext)

keyboard.keymap = [
    [
        KC.MPRV, KC.MPLY, KC.MNXT,
        KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C),
        KC.MUTE, KC.LCTL(KC.V), KC.MO(1)
    ],
    [
        KC.F1,   KC.F2,   KC.F3,
        KC.F4,   KC.F5,   KC.F6,    
        KC.TRNS, KC.TRNS, KC.TRNS     
    ]
]

if __name__ == '__main__':
    keyboard.go()