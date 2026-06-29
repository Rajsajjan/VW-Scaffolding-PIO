import vs
from SymbolLibrary import STANDARDS, LEDGERS

def place_symbol(symbol_name, x, y):
    if vs.GetObject(symbol_name):
        vs.Symbol(symbol_name, x, y, 0)
    else:
        vs.AlrtDialog("Symbol not found: " + symbol_name)

def place_ledger(symbol_name, x, y, rotation):
    if vs.GetObject(symbol_name):
        vs.Symbol(symbol_name, x, y, rotation)

def main():
    # Read Plug-in Parameters
bays_x = int(vs.PBaysX)
bays_y = int(vs.PBaysY)

    # Read Plug-in Parameters
    standard_choice = vs.PStandardType
    ledger_choice = vs.PLedgerType
    
    standard_symbol = STANDARDS[standard_choice]
    ledger_symbol = LEDGERS[ledger_choice]

    bay_length = vs.PBayLength
    bay_width = vs.PBayWidth

    # Create corner points for every bay
    for ix in range(bays_x + 1):
        for iy in range(bays_y + 1):

            x = ix * bay_length
            y = iy * bay_width

            place_symbol("Layher ZB Adjustiable Base 20", x, y)
            place_symbol("Layher TR Base Collar", x, y)
            place_symbol(standard_symbol, x, y)

           # X Direction
           if ix < bays_x:
               place_ledger(ledger_symbol, x, y + 190, 0)

           # Y Direction
           if iy < bays_y:
               place_ledger(ledger_symbol, x, y + 190, 90)
               
main() 
