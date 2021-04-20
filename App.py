from email.mime import application

from flask import Flask,jsonify,request, Response, redirect
import json
app = Flask(__name__)
employees = [
    {
    "name": "Dipti",
    "id" : "1",
    "skills": [
        {"name":"Ansible", "proficiency_level": "beginner" },
         {"name":"Linux", "proficiency_level": "Intermediate" },
          {"name":"Jenkins", "proficiency_level": "Professional" },
    ]
},

    {
        "name": "Harshada",
        "id": "2",
        "skills": [
            {"name": "Docker", "proficiency_level": "beginner"},
            {"name": "Kubernetes", "proficiency_level": "Intermediate"},
            {"name": "VMware", "proficiency_level": "Professional"}
        ]
    }

]


@app.route('/')
def main():
    return 'Employee Information'

def Validate_put_data(data_object):
    if ( 'name' in data_object and 'id' in data_object and 'skills' in data_object):
        return True
    else:
        return False



# To display all the employees
@app.route('/employees')
def get_employees():
    return  jsonify({'employees' : employees})


#To check Employee is present or not
@app.route('/employees/<string:name>')
def check_employee(name):
    for employee in employees:
        if employee['name'] == name :
            return jsonify(employee)
    return jsonify({'Alert' : 'Sorry, No employee found'})


#  TO add new employee
@app.route('/employees', methods=['PUT'])
def add_employee():
    data = request.get_json()

    if Validate_put_data(data_object=data):
        new_employee = {
        'name': data['name'],
        'id': data['id'],
        'skills': data['skills']
    }
        employees.append(new_employee)
        #return jsonify({'Messgae' : 'New Employee Successfully Added..!!'})
        return redirect('/employees')
    else:
        response = Response(json.dumps({
            'Error' : 'Invalid Employee data'
        }), status=400, mimetype='application/json')
        return response


# for Update Employee
@app.route('/employees/<string:name>', methods=['POST'])
def update_employee(name):
    global employees
    request_data = request.get_json()
    new_employee = {
        'name': name,
        'skills': request_data['skills'],
        'id':  request_data['id']

    }
    i=0
    result = False
    for employee in employees:
        if employee['name'] == name:
            employees[i] = new_employee
            result = True

            i += 1
    if result:
        return redirect(f'/employees/{name}')
    else:
        return Response("", status=404)


# For Delete Employee
@app.route('/employees/<string:name>', methods=['DELETE'])
def delete_employee(name):
    global employees
    i = 0
    deleted = False

    for employee in employees:
        if employee['name'] == name:
            employees.pop(i)

            deleted = True
        i += 1

    if deleted:
        return  Response("", status=204, mimetype='application/json')
    else:
        return  Response("", status=400, mimetype='application/json')





app.run(debug=True, port=7000)