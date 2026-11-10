# Non-Metal Element Details
from pyscript import display , document

def check(e):
    # Calls out the variables
    document.getElementById('output3').innerHTML = ' '
    symbol = document.getElementById('symbol').value

    # Elements in the dictionary
    elements = {
        'h': {
            'Symbol': 'H',
            'Element': 'Hydrogen',
            'Atomic Number': 1,
            'Atomic Mass': 1008
        },

        'he': {
            'Symbol': 'He',
            'Element': 'Helium',
            'Atomic Number': 2,
            'Atomic Mass': 4.0026
        },
        
        'c': {
            'Symbol': 'C',
            'Element': 'Carbon',
            'Atomic Number': 6,
            'Atomic Mass': 12.011
        },

        'n': {
            'Symbol': 'N',
            'Element': 'Nitrogen',
            'Atomic Number': 7,
            'Atomic Mass': 14.007
        },

        'o': {
            'Symbol': 'O',
            'Element': 'Oxygen',
            'Atomic Number': 8,
            'Atomic Mass': 15.999
        },

        'f': {
            'Symbol': 'F',
            'Element': 'Fluorine',
            'Atomic Number': 9,
            'Atomic Mass': 18.998
        },

        'ne': {
            'Symbol': 'Ne',
            'Element': 'Neon',
            'Atomic Number': 10,
            'Atomic Mass': 20.180
        },

        'p': {
            'Symbol': 'P',
            'Element': 'Phosphorus',
            'Atomic Number': 15,
            'Atomic Mass': 30.974,
        },

        's': {
            'Symbol': 'S',
            'Element': 'Sulfur',
            'Atomic Number': 16,
            'Atomic Mass': 32.065
        },

        'cl': {
            'Symbol': 'Cl',
            'Element': 'Chlorine',
            'Atomic Number': 17,
            'Atomic Mass': 35.45,
        },

        'ar': {
            'Symbol': 'Ar',
            'Element': 'Argon',
            'Atomic Number': 18,
            'Atomic Mass': 39.948,
        },

        'se': {
            'Symbol': 'Se',
            'Element': 'Selenium',
            'Atomic Number': 34,
            'Atomic Mass': 78.97,
        },

        'br': {
            'Symbol': 'Br',
            'Element': 'Bromine',
            'Atomic Number': 35,
            'Atomic Mass': 79.90
        },

        'kr': {
            'Symbol': 'Kr',
            'Element': 'Krypton',
            'Atomic Number': 36,
            'Atomic Mass': 83.80
        },

        'i':{
            'Symbol': 'I',
            'Element': 'Iodine',
            'Atomic Number': 53,
            'Atomic Mass': 126.90
        },

        'xe':{
            'Symbol': 'Xe',
            'Element': 'Xenon',
            'Atomic Number': 54,
            'Atomic Mass': 131.29
        },

        'rn': {
            'Symbol': 'Rn',
            'Element': 'Radon',
            'Atomic Number': 86,
            'Atomic Mass': 222
        }
    }

    # The output
    info = elements.get(symbol)
    display(info, target="output3")
