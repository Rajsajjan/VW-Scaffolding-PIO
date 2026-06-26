# Parameters for the Scaffolding Plug-in

import vs


class Parameters:
    """
    Stores all user-controlled scaffold settings.
    These will later connect to Vectorworks PIO fields.
    """

    # Basic scaffold dimensions
    BAY_LENGTH = 2000      # distance between vertical frames (mm)
    BAY_WIDTH = 1000       # scaffold depth (mm)

    # Vertical settings
    LEVEL_HEIGHT = 2000    # height between lifts (mm)
    NUMBER_OF_LEVELS = 3   # how many scaffold levels

    # Base settings
    BASE_JACK_HEIGHT = 150

    # Safety settings
    HAS_GUARDRAIL = True
    HAS_TOEBOARD = True

    # Optional settings
    INCLUDE_LADDER = True

    @staticmethod
    def get_total_height():
        """
        Returns total scaffold height.
        """
        return Parameters.LEVEL_HEIGHT * Parameters.NUMBER_OF_LEVELS

    @staticmethod
    def get_total_length(num_bays):
        """
        Returns total scaffold length based on number of bays.
        """
        return Parameters.BAY_LENGTH * num_bays# Parameters for the Scaffolding Plug-in
