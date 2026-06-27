import vs

def place_symbol(symbol_name, x, y):
    if vs.GetObject(symbol_name):
        vs.Symbol(symbol_name, x, y, 0)
    else:
        vs.AlrtDialog("Symbol not found: " + symbol_name)

def main():

    # Read Plug-in Parameters
    bays_x = int(vs.PBaySX)
    bays_y = int(vs.PBaySY)

    bay_length = vs.PBayLength
    bay_width = vs.PBayWidth

    # Create corner points for every bay
    for ix in range(bays_x + 1):
        for iy in range(bays_y + 1):

            x = ix * bay_length
            y = iy * bay_width

            place_symbol("Layher ZB Adjustiable Base 20", x, y)
            place_symbol("Layher TR Base Collar", x, y)

main() Scaffolding Plug-in
