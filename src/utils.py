import json


class writer():
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
        except Exception as e:
            print('COULD NOT LOAD:', filename)
            print(e)
        print(returndata)
