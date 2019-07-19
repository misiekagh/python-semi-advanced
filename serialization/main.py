from serialization.worker import Worker

import pickle, json

def serialize_pkl():
    kowalska=Worker('Madzia', 'Kowalska')
    kowalski=Worker('Jan', 'Kowalski')

    employs=[kowalska, kowalski]
    print(employs)

    with open('emps.pkl','wb') as f:
        pickle.dump(employs, f)

def try_serialize_json():
    kowalska=Worker('Madzia', 'Kowalska')
    kowalski=Worker('Jan', 'Kowalski')

    employs=[kowalska, kowalski]
    print(employs)


def serialize_json():
    emps= {
        'kowalska':{"first_name":"madzia","last_name":"kowalska"},
        'kowalski':{'first_name':'jan','last_name':'kowalski'}
    }

    with open('emps.json','w') as f:
        json.dump(emps, f)

    print(json.dumps(emps))

def deserialize_json():
    with open('emps.json') as f:
        return json.load(f)

def deserialize_pkl():
    with open('emps.pkl', 'rb') as f:
        return(pickle.load(f))

serialize_json()
print(deserialize_json())
