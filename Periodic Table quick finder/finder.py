import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

periodic_table = {
    'H': {'name': 'Hydrogen', 'number': 1, 'group': 1, 'period': 1},
    'He': {'name': 'Helium', 'number': 2, 'group': 18, 'period': 1},
    'Li': {'name': 'Lithium', 'number': 3, 'group': 1, 'period': 2},
    'Be': {'name': 'Beryllium', 'number': 4, 'group': 2, 'period': 2},
    'B': {'name': 'Boron', 'number': 5, 'group': 13, 'period': 2},
    'C': {'name': 'Carbon', 'number': 6, 'group': 14, 'period': 2},
    'N': {'name': 'Nitrogen', 'number': 7, 'group': 15, 'period': 2},
    'O': {'name': 'Oxygen', 'number': 8, 'group': 16, 'period': 2},
    'F': {'name': 'Fluorine', 'number': 9, 'group': 17, 'period': 2},
    'Ne': {'name': 'Neon', 'number': 10, 'group': 18, 'period': 2},
    'Na': {'name': 'Sodium', 'number': 11, 'group': 1, 'period': 3},
    'Mg': {'name': 'Magnesium', 'number': 12, 'group': 2, 'period': 3},
    'Al': {'name': 'Aluminium', 'number': 13, 'group': 13, 'period': 3},
    'Si': {'name': 'Silicon', 'number': 14, 'group': 14, 'period': 3},
    'P': {'name': 'Phosphorus', 'number': 15, 'group': 15, 'period': 3},
    'S': {'name': 'Sulfur', 'number': 16, 'group': 16, 'period': 3},
    'Cl': {'name': 'Chlorine', 'number': 17, 'group': 17, 'period': 3},
    'Ar': {'name': 'Argon', 'number': 18, 'group': 18, 'period': 3},
    'K': {'name': 'Potassium', 'number': 19, 'group': 1, 'period': 4},
    'Ca': {'name': 'Calcium', 'number': 20, 'group': 2, 'period': 4},
    'Sc': {'name': 'Scandium', 'number': 21, 'group': 3, 'period': 4},
    'Ti': {'name': 'Titanium', 'number': 22, 'group': 4, 'period': 4},
    'V': {'name': 'Vanadium', 'number': 23, 'group': 5, 'period': 4},
    'Cr': {'name': 'Chromium', 'number': 24, 'group': 6, 'period': 4},
    'Mn': {'name': 'Manganese', 'number': 25, 'group': 7, 'period': 4},
    'Fe': {'name': 'Iron', 'number': 26, 'group': 8, 'period': 4},
    'Co': {'name': 'Cobalt', 'number': 27, 'group': 9, 'period': 4},
    'Ni': {'name': 'Nickel', 'number': 28, 'group': 10, 'period': 4},
    'Cu': {'name': 'Copper', 'number': 29, 'group': 11, 'period': 4},
    'Zn': {'name': 'Zinc', 'number': 30, 'group': 12, 'period': 4},
    'Ga': {'name': 'Gallium', 'number': 31, 'group': 13, 'period': 4},
    'Ge': {'name': 'Germanium', 'number': 32, 'group': 14, 'period': 4},
    'As': {'name': 'Arsenic', 'number': 33, 'group': 15, 'period': 4},
    'Se': {'name': 'Selenium', 'number': 34, 'group': 16, 'period': 4},
    'Br': {'name': 'Bromine', 'number': 35, 'group': 17, 'period': 4},
    'Kr': {'name': 'Krypton', 'number': 36, 'group': 18, 'period': 4},
    'Rb': {'name': 'Rubidium', 'number': 37, 'group': 1, 'period': 5},
    'Sr': {'name': 'Strontium', 'number': 38, 'group': 2, 'period': 5},
    'Y': {'name': 'Yttrium', 'number': 39, 'group': 3, 'period': 5},
    'Zr': {'name': 'Zirconium', 'number': 40, 'group': 4, 'period': 5},
    'Nb': {'name': 'Niobium', 'number': 41, 'group': 5, 'period': 5},
    'Mo': {'name': 'Molybdenum', 'number': 42, 'group': 6, 'period': 5},
    'Tc': {'name': 'Technetium', 'number': 43, 'group': 7, 'period': 5},
    'Ru': {'name': 'Ruthenium', 'number': 44, 'group': 8, 'period': 5},
    'Rh': {'name': 'Rhodium', 'number': 45, 'group': 9, 'period': 5},
    'Pd': {'name': 'Palladium', 'number': 46, 'group': 10, 'period': 5},
    'Ag': {'name': 'Silver', 'number': 47, 'group': 11, 'period': 5},
    'Cd': {'name': 'Cadmium', 'number': 48, 'group': 12, 'period': 5},
    'In': {'name': 'Indium', 'number': 49, 'group': 13, 'period': 5},
    'Sn': {'name': 'Tin', 'number': 50, 'group': 14, 'period': 5},
    'Sb': {'name': 'Antimony', 'number': 51, 'group': 15, 'period': 5},
    'Te': {'name': 'Tellurium', 'number': 52, 'group': 16, 'period': 5},
    'I': {'name': 'Iodine', 'number': 53, 'group': 17, 'period': 5},
    'Xe': {'name': 'Xenon', 'number': 54, 'group': 18, 'period': 5},
    'Cs': {'name': 'Cesium', 'number': 55, 'group': 1, 'period': 6},
    'Ba': {'name': 'Barium', 'number': 56, 'group': 2, 'period': 6},
    'La': {'name': 'Lanthanum', 'number': 57, 'group': 3, 'period': 6},
    'Ce': {'name': 'Cerium', 'number': 58, 'group': 3, 'period': 6},
    'Pr': {'name': 'Praseodymium', 'number': 59, 'group': 3, 'period': 6},
    'Nd': {'name': 'Neodymium', 'number': 60, 'group': 3, 'period': 6},
    'Pm': {'name': 'Promethium', 'number': 61, 'group': 3, 'period': 6},
    'Sm': {'name': 'Samarium', 'number': 62, 'group': 3, 'period': 6},
    'Eu': {'name': 'Europium', 'number': 63, 'group': 3, 'period': 6},
    'Gd': {'name': 'Gadolinium', 'number': 64, 'group': 3, 'period': 6},
    'Tb': {'name': 'Terbium', 'number': 65, 'group': 3, 'period': 6},
    'Dy': {'name': 'Dysprosium', 'number': 66, 'group': 3, 'period': 6},
    'Ho': {'name': 'Holmium', 'number': 67, 'group': 3, 'period': 6},
    'Er': {'name': 'Erbium', 'number': 68, 'group': 3, 'period': 6},
    'Tm': {'name': 'Thulium', 'number': 69, 'group': 3, 'period': 6},
    'Yb': {'name': 'Ytterbium', 'number': 70, 'group': 3, 'period': 6},
    'Lu': {'name': 'Lutetium', 'number': 71, 'group': 3, 'period': 6},
    'Hf': {'name': 'Hafnium', 'number': 72, 'group': 4, 'period': 6},
    'Ta': {'name': 'Tantalum', 'number': 73, 'group': 5, 'period': 6},
    'W': {'name': 'Tungsten', 'number': 74, 'group': 6, 'period': 6},
    'Re': {'name': 'Rhenium', 'number': 75, 'group': 7, 'period': 6},
    'Os': {'name': 'Osmium', 'number': 76, 'group': 8, 'period': 6},
    'Ir': {'name': 'Iridium', 'number': 77, 'group': 9, 'period': 6},
    'Pt': {'name': 'Platinum', 'number': 78, 'group': 10, 'period': 6},
    'Au': {'name': 'Gold', 'number': 79, 'group': 11, 'period': 6},
    'Hg': {'name': 'Mercury', 'number': 80, 'group': 12, 'period': 6},
    'Tl': {'name': 'Thallium', 'number': 81, 'group': 13, 'period': 6},
    'Pb': {'name': 'Lead', 'number': 82, 'group': 14, 'period': 6},
    'Bi': {'name': 'Bismuth', 'number': 83, 'group': 15, 'period': 6},
    'Po': {'name': 'Polonium', 'number': 84, 'group': 16, 'period': 6},
    'At': {'name': 'Astatine', 'number': 85, 'group': 17, 'period': 6},
    'Rn': {'name': 'Radon', 'number': 86, 'group': 18, 'period': 6},
    'Fr': {'name': 'Francium', 'number': 87, 'group': 1, 'period': 7},
    'Ra': {'name': 'Radium', 'number': 88, 'group': 2, 'period': 7},
    'Ac': {'name': 'Actinium', 'number': 89, 'group': 3, 'period': 7},
    'Th': {'name': 'Thorium', 'number': 90, 'group': 3, 'period': 7},
    'Pa': {'name': 'Protactinium', 'number': 91, 'group': 3, 'period': 7},
    'U': {'name': 'Uranium', 'number': 92, 'group': 3, 'period': 7},
    'Np': {'name': 'Neptunium', 'number': 93, 'group': 3, 'period': 7},
    'Pu': {'name': 'Plutonium', 'number': 94, 'group': 3, 'period': 7},
    'Am': {'name': 'Americium', 'number': 95, 'group': 3, 'period': 7},
    'Cm': {'name': 'Curium', 'number': 96, 'group': 3, 'period': 7},
    'Bk': {'name': 'Berkelium', 'number': 97, 'group': 3, 'period': 7},
    'Cf': {'name': 'Californium', 'number': 98, 'group': 3, 'period': 7},
    'Es': {'name': 'Einsteinium', 'number': 99, 'group': 3, 'period': 7},
    'Fm': {'name': 'Fermium', 'number': 100, 'group': 3, 'period': 7},
    'Md': {'name': 'Mendelevium', 'number': 101, 'group': 3, 'period': 7},
    'No': {'name': 'Nobelium', 'number': 102, 'group': 3, 'period': 7},
    'Lr': {'name': 'Lawrencium', 'number': 103, 'group': 3, 'period': 7},
    'Rf': {'name': 'Rutherfordium', 'number': 104, 'group': 4, 'period': 7},
    'Db': {'name': 'Dubnium', 'number': 105, 'group': 5, 'period': 7},
    'Sg': {'name': 'Seaborgium', 'number': 106, 'group': 6, 'period': 7},
    'Bh': {'name': 'Bohrium', 'number': 107, 'group': 7, 'period': 7},
    'Hs': {'name': 'Hassium', 'number': 108, 'group': 8, 'period': 7},
    'Mt': {'name': 'Meitnerium', 'number': 109, 'group': 9, 'period': 7},
    'Ds': {'name': 'Darmstadtium', 'number': 110, 'group': 10, 'period': 7},
    'Rg': {'name': 'Roentgenium', 'number': 111, 'group': 11, 'period': 7},
    'Cn': {'name': 'Copernicium', 'number': 112, 'group': 12, 'period': 7},
    'Nh': {'name': 'Nihonium', 'number': 113, 'group': 13, 'period': 7},
    'Fl': {'name': 'Flerovium', 'number': 114, 'group': 14, 'period': 7},
    'Mc': {'name': 'Moscovium', 'number': 115, 'group': 15, 'period': 7},
    'Lv': {'name': 'Livermorium', 'number': 116, 'group': 16, 'period': 7},
    'Ts': {'name': 'Tennessine', 'number': 117, 'group': 17, 'period': 7},
    'Og': {'name': 'Oganesson', 'number': 118, 'group': 18, 'period': 7},
}

def find_element_group(symbol):
    element = periodic_table.get(symbol)
    if element:
        return element['group']
    else:
        return None

def find_element_name(symbol):
    element = periodic_table.get(symbol)
    if element:
        return element['name']
    else:
        return None

def find_element_period(symbol):
    element = periodic_table.get(symbol)
    if element:
        return element['period']
    else:
        return None

def handle_find_element():
    symbol = entry_element.get().strip()
    name = find_element_name(symbol)
    group = find_element_group(symbol)
    period = find_element_period(symbol)
    
    if name and group and period:
        messagebox.showinfo('Element Found', f"{name} (symbol: {symbol}) is at group {group} on the periodic table and period {period}.")
    else:
        messagebox.showwarning('Element Not Found', f"Element with symbol '{symbol}' not found in the periodic table.")

window = tk.Tk()
window.title('Periodic Table Element Finder')

try:
    table_image = PhotoImage(file='C:\\Users\\ShySkill\\Downloads\\Periodic Table quick finder\\periodic-table.png') 
    image_label = tk.Label(window, image=table_image)
    image_label.pack(pady=10)
except Exception as e:
    messagebox.showwarning('Image Load Error', f"Failed to load the periodic table image: {e}")

try:
    icon_image = PhotoImage(file='C:\\Users\\ShySkill\\Downloads\\Periodic Table quick finder\\7812701.png') 
    window.iconphoto(True, icon_image)  
except Exception as e:
    messagebox.showwarning('Icon Load Error', f"Failed to load the custom icon: {e}")


label = tk.Label(window, text='Enter element symbol (e.g., H, He, Li):')
label.pack(pady=10)

entry_element = tk.Entry(window, width=10)
entry_element.pack(pady=5)

btn_find = tk.Button(window, text='Find Element', command=handle_find_element)
btn_find.pack(pady=10)

window.mainloop()



