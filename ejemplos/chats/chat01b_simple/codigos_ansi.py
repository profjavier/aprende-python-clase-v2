class CodigosAnsi:
    # ------- RESET -------
    RESET = "\033[0m"

    # ------- ESTILOS -------
    ESTILO_BOLD = "\033[1m"
    ESTILO_DIM = "\033[2m"
    ESTILO_ITALIC = "\033[3m"
    ESTILO_UNDERLINE = "\033[4m"
    ESTILO_BLINK = "\033[5m"
    ESTILO_REVERSE = "\033[7m"
    ESTILO_HIDDEN = "\033[8m"
    ESTILO_STRIKETHROUGH = "\033[9m"

    # ------- COLORES DE TEXTO -------
    TEXT_NEGRO = "\033[30m"
    TEXT_ROJO = "\033[31m"
    TEXT_VERDE = "\033[32m"
    TEXT_AMARILLO = "\033[33m"
    TEXT_AZUL = "\033[34m"
    TEXT_MAGENTA = "\033[35m"
    TEXT_CIAN = "\033[36m"
    TEXT_BLANCO = "\033[37m"

    # ------- COLORES DE FONDO -------
    BG_NEGRO = "\033[40m"
    BG_ROJO = "\033[41m"
    BG_VERDE = "\033[42m"
    BG_AMARILLO = "\033[43m"
    BG_AZUL = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CIAN = "\033[46m"
    BG_BLANCO = "\033[47m"

    # ------- BRILLANTES (TEXTO) -------
    TEXT_NEGRO_CLARO = "\033[90m"
    TEXT_ROJO_CLARO = "\033[91m"
    TEXT_VERDE_CLARO = "\033[92m"
    TEXT_AMARILLO_CLARO = "\033[93m"
    TEXT_AZUL_CLARO = "\033[94m"
    TEXT_MAGENTA_CLARO = "\033[95m"
    TEXT_CIAN_CLARO = "\033[96m"
    TEXT_BLANCO_CLARO = "\033[97m"

    # ------- BRILLANTES (FONDO) -------
    BG_NEGRO_CLARO = "\033[100m"
    BG_ROJO_CLARO = "\033[101m"
    BG_VERDE_CLARO = "\033[102m"
    BG_AMARILLO_CLARO = "\033[103m"
    BG_AZUL_CLARO = "\033[104m"
    BG_MAGENTA_CLARO = "\033[105m"
    BG_CIAN_CLARO = "\033[106m"
    BG_BLANCO_CLARO = "\033[107m"

    # ------- CONTROL DE CURSOR -------
    CURSOR_UP = "\033[A"
    CURSOR_DOWN = "\033[B"
    CURSOR_RIGHT = "\033[C"
    CURSOR_LEFT = "\033[D"
    CURSOR_NEXT_LINE = "\033[E"
    CURSOR_PREV_LINE = "\033[F"
    CURSOR_COLUMN = "\033[G"
    CURSOR_POS = "\033[{};{}H"

    # ------- BORRADO -------
    CLEAR_SCREEN = "\033[2J"
    CLEAR_LINE = "\033[2K"

    # ------- SAVE / RESTORE -------
    SAVE_CURSOR = "\033[s"
    RESTORE_CURSOR = "\033[u"

    # ------------------------------------------------
    #  MÉTODOS ESTÁTICOS PARA 256 COLORS Y RGB
    # ------------------------------------------------

    @staticmethod
    def color_256(n: int) -> str:
        """Texto en color ANSI de 0–255"""
        return f"\033[38;5;{n}m"

    @staticmethod
    def bg_256(n: int) -> str:
        """Fondo ANSI 256 colores"""
        return f"\033[48;5;{n}m"

    @staticmethod
    def rgb(r: int, g: int, b: int) -> str:
        """Texto RGB real (TrueColor, 24 bits)"""
        return f"\033[38;2;{r};{g};{b}m"

    @staticmethod
    def bg_rgb(r: int, g: int, b: int) -> str:
        """Fondo RGB real (TrueColor)"""
        return f"\033[48;2;{r};{g};{b}m"

    @staticmethod
    def texto_color(texto: str, color: str) -> str:
        """Aplica color y hace reset al final."""
        return f"{color}{texto}{CodigosAnsi.RESET}"

    @staticmethod
    def posicion(fila: int, columna: int) -> str:
        """Mueve el cursor a fila y columna."""
        return f"\033[{fila};{columna}H"

    @staticmethod
    def columna(n: int) -> str:
        """Mueve solo la columna, mantiene la fila."""
        return f"\033[{n}G"

    @staticmethod
    def limpiar_pantalla():
        """Borra la pantalla y mueve el cursor al inicio."""
        print ("\033[2J\033[H", end="")

    @staticmethod
    def cursor_inicio() -> str:
        """Posiciona el cursor en 1,1 (arriba izquierda)."""
        return "\033[H"

    @staticmethod
    def activa(codigo:str):
        print(codigo, end="")

    @staticmethod
    def reset():
        print("\033[0m", end="")
