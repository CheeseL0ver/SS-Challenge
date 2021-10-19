from flask import Flask

app = Flask(__name__)
zip_codes = set()

@app.route("/insert/<int:zip_code>", methods=["POST"])
def insert_zip_code(zip_code):
    if zip_code not in zip_codes:
        zip_codes.add(zip_code)
        return {'message': f'Added {zip_code}'}

    return {'message': f'Already added {zip_code}'}

@app.route("/delete/<int:zip_code>", methods=["DELETE"])
def delete_zip_code(zip_code):
    if zip_code in zip_codes:
        zip_codes.remove(zip_code)
        return {'message': f'Deleted {zip_code}'}
    
    return {'message': f'Zip code {zip_code} was not found in system'}

@app.route("/has/<int:zip_code>")
def has_zip_code(zip_code):
    if zip_code in zip_codes:
        return {'message': True}
    
    return {'message': False}    

@app.route("/display")
def display_zip_codes():
    return {'message': Print()}   

def Print():
    ret = []
    tmp = None #Last see value
    rangeStart = None
    rangeEnd = None
    rangeAddition = None
    for value in zip_codes:
        if rangeStart is None and tmp is None:
            tmp = value
            rangeStart = value
        elif value == tmp + 1:
            tmp = value
            rangeEnd = value
        elif value != tmp + 1 and rangeEnd is None:
            ret.append(f'{rangeStart}')
            tmp = value
            rangeStart = value
        else:
            if rangeEnd != value:
                ret.append(f'{rangeStart} - {rangeEnd}')
                ret.append(f'{value}')
                rangeStart = value
                rangeEnd = None
                tmp = value
            else:
                rangeStart = value
                tmp = value
                ret.append(value)

    return ret