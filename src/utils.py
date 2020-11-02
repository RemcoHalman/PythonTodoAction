import json


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
            print('ERROR writing', filename)
            print(e)
            pass

    def get(filename):
        returndata = {}
        try:
            fd = open(filename, 'r')
            text = fd.read()
            fd.close()
            returndata = json.loads(text)
        except IOError as e:
            print('COULD NOT LOAD:', e.filename)
        print(returndata)


class DoorMat():
    def top(width):
        print(" Check if TODO or FIXME exist ".center(width, "*"))
        print("".center(width, "*"))
        print("")

    def bottom(width):
        print("")
        print("".center(width, "*"))
        print(" End Check ".center(width, "*"))
