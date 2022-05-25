# auto generated
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split,SplitSide,SplitType
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap) 

# keymap
keyboard.keymap = [ [KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.ESC,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCLN,KC.QUOT,KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,KC.SLSH,KC.ENT,KC.PIPE,KC.LCTL,KC.LALT,KC.LGUI,KC.MO(1),KC.SPC,KC.SPC,KC.MO(2),KC.LEFT,KC.DOWN,KC.UP,KC.RGHT],
[KC.GRV,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.DEL,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.MINS,KC.EQL,KC.LBRC,KC.RBRC,KC.BSLS,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.NUHS,KC.NUBS,KC.PGUP,KC.PGDN,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.MNXT,KC.VOLD,KC.VOLU,KC.MPLY],
[KC.TILD,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.DEL,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.UNDS,KC.PLUS,KC.LCBR,KC.RCBR,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.MNXT,KC.VOLD,KC.VOLU,KC.MPLY],
[KC.TILD,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.DEL,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.UNDS,KC.PLUS,KC.LCBR,KC.RCBR,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.MNXT,KC.VOLD,KC.VOLU,KC.MPLY],
[KC.TILD,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.DEL,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.UNDS,KC.PLUS,KC.LCBR,KC.RCBR,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.MNXT,KC.VOLD,KC.VOLU,KC.MPLY],
[KC.TILD,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.DEL,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.UNDS,KC.PLUS,KC.LCBR,KC.RCBR,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.MNXT,KC.VOLD,KC.VOLU,KC.MPLY],
[KC.TILD,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.DEL,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.UNDS,KC.PLUS,KC.LCBR,KC.RCBR,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.MNXT,KC.VOLD,KC.VOLU,KC.MPLY],
[KC.TILD,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.DEL,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.UNDS,KC.PLUS,KC.LCBR,KC.RCBR,KC.PIPE,KC.TRNS,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.HOME,KC.END,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.MNXT,KC.VOLD,KC.VOLU,KC.MPLY] ]
# keymap

if __name__ == '__main__':  
    keyboard.go(hid_type=HIDModes.USB) 