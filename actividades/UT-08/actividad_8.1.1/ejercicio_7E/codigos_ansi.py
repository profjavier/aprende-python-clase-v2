class CodigosAnsi:
    """Constantes ANSI para colores, estilos y control del cursor."""

    # ----- Reset -----
    RESET = "\033[0m"

    # ----- Estilos -----
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    INVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    STRIKETHROUGH = "\033[9m"

    # ----- Colores básicos FG -----
    FG_BLACK = "\033[30m"
    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_YELLOW = "\033[33m"
    FG_BLUE = "\033[34m"
    FG_MAGENTA = "\033[35m"
    FG_CYAN = "\033[36m"
    FG_WHITE = "\033[37m"

    # ----- Colores brillantes FG -----
    FG_BRIGHT_BLACK = "\033[90m"
    FG_BRIGHT_RED = "\033[91m"
    FG_BRIGHT_GREEN = "\033[92m"
    FG_BRIGHT_YELLOW = "\033[93m"
    FG_BRIGHT_BLUE = "\033[94m"
    FG_BRIGHT_MAGENTA = "\033[95m"
    FG_BRIGHT_CYAN = "\033[96m"
    FG_BRIGHT_WHITE = "\033[97m"

    # ----- Colores básicos BG -----
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # ----- Colores brillantes BG -----
    BG_BRIGHT_BLACK = "\033[100m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_YELLOW = "\033[103m"
    BG_BRIGHT_BLUE = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN = "\033[106m"
    BG_BRIGHT_WHITE = "\033[107m"

    # ----- Limpieza -----
    CLEAR_SCREEN = "\033[2J"
    CLEAR_LINE = "\033[2K"

    # ----- Movimientos de cursor -----
    CURSOR_HOME = "\033[H"
    CURSOR_SAVE = "\0337"
    CURSOR_RESTORE = "\0338"

    # Movimientos relativos (usa format para número)
    @staticmethod
    def cursor_up(n=1): return f"\033[{n}A"
    @staticmethod
    def cursor_down(n=1): return f"\033[{n}B"
    @staticmethod
    def cursor_forward(n=1): return f"\033[{n}C"
    @staticmethod
    def cursor_back(n=1): return f"\033[{n}D"
    @staticmethod
    def cursor_to(row, col): return f"\033[{row};{col}H"


    @staticmethod
    def activa(codigo:str):
        print(codigo, end="")

    @staticmethod
    def reset():
        print("\033[0m", end="")

    def texto_color(texto: str, color: str) -> str:
        return f"{color}{texto}{CodigosAnsi.RESET}"

    def print_texto_color(texto: str, color: str, end=""):
        print(f"{color}{texto}{CodigosAnsi.RESET}", end=end)
