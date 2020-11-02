import json

from .colors import BackgroundColors


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
