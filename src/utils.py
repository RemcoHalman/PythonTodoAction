import json


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

class Writer():
    def put(data, filename):
        try:
            jsondata = json.dumps(data,
                                  indent=4,
                                  skipkeys=False,
                                  sort_keys=True)
            fd = open(filename, 'w')
            fd.write(jsondata)
            fd.close()
        except Exception as e:
            BackgroundColors.printColor(
                value=f"ERROR writing: {e.filename}",
                color=BackgroundColors.WARNING
            )
            pass

    def get(filename):
        returndata = {}
        try:
            fd = open(filename, 'r')
            text = fd.read()
            fd.close()
            returndata = json.loads(text)
            print(returndata)
        except IOError as e:
            BackgroundColors.printColor(
                value=f"COULD NOT LOAD: {e.filename}",
                color=BackgroundColors.FAIL
            )


class DoorMat():
    def top(width):
        BackgroundColors.printColor(
            value=" Check if TODO or FIXME exist ".center(width, "*"),
            color=BackgroundColors.CYAN
        )

    def middle(width):
        BackgroundColors.printColor(
            value=" End Check & Continu ".center(width, "*"),
            color=BackgroundColors.CYAN
        )

    def bottom(width):
        BackgroundColors.printColor(
            value=" Issues created ".center(width, "*"),
            color=BackgroundColors.CYAN
        )
