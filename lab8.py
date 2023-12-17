from flask import Blueprint, render_template, request, abort, jsonify

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {'name': 'c++', 'videos': 3, 'price': 3000},
    {'name': 'basic', 'videos': 30, 'price': 0},
    {'name': 'c#', 'videos': 8},
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return jsonify(courses)

@lab8.route('/lab8/api/courses/<int:courses_num>', methods=['GET'])
def get_course(courses_num):
    if courses_num-1 > len(courses):
        abort(404)
    return courses[courses_num]

@lab8.route('/lab8/api/courses/<int:courses_num>', methods=['DELETE'])
def del_course(courses_num):
    if courses_num-1 > len(courses):
        abort(404)
    del courses[courses_num]
    return '', 204

@lab8.route('/lab8/api/courses/<int:courses_num>', methods=['PUT'])
def put_course(courses_num):
    if courses_num-1 > len(courses):
        abort(404)
    course = request.get_json()
    courses[courses_num] = course
    return courses[courses_num]

@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    courses.append(course)
    return {'num': len(courses)-1}