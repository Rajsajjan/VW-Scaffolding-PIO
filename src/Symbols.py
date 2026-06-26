# Symbol name# Symbol names used by the Scaffolding Plug-in

import vs


class Symbols:
    FRAME = "Scaffold_Frame"
    BASE_JACK = "Scaffold_Base_Jack"
    LEDGER = "Scaffold_Ledger"
    TRANSOM = "Scaffold_Transom"

    STANDARD = "Scaffold_Standard"
    BRACE_DIAGONAL = "Scaffold_Diagonal_Brace"

    DECK = "Scaffold_Deck"
    TOE_BOARD = "Scaffold_Toe_Board"

    GUARDRAIL = "Scaffold_Guardrail"
    MIDRAIL = "Scaffold_Midrail"
    KICKBOARD = "Scaffold_Kickboard"

    LADDER = "Scaffold_Ladder"
    STAIR = "Scaffold_Stair"

    @staticmethod
    def list_all():
        return [
            Symbols.FRAME,
            Symbols.BASE_JACK,
            Symbols.LEDGER,
            Symbols.TRANSOM,
            Symbols.STANDARD,
            Symbols.BRACE_DIAGONAL,
            Symbols.DECK,
            Symbols.TOE_BOARD,
            Symbols.GUARDRAIL,
            Symbols.MIDRAIL,
            Symbols.KICKBOARD,
            Symbols.LADDER,
            Symbols.STAIR,
        ]

    @staticmethod
    def exists(symbol_name):
        h = vs.GetObject(symbol_name)
        return h is not Nones used by the Scaffolding Plug-in
