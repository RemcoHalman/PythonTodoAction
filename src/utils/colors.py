class BackgroundColors():
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    WHITE = '\033[37m'
    WARNING = '\033[33m'
    FAIL = '\033[31m'
    END = '\033[0m'

    def printColor(value, color, end=END):
        print(color + value + end)
