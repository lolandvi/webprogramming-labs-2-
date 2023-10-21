from flask import Blueprint, render_template, request
from emoji import emojize


deff3 = Blueprint('deff3', __name__)


@deff3.route('/def3/')
def def3():
    exist = request.args.get('exist')
    full = request.args.get('full')
    if exist == '' or full == '':
        return render_template('def3.html')
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)

    def sinus(x, n):
        result = 0
        for i in range (n+1):
            num = (-1)**i*x**(2*i+1)
            denum = factorial(2*i+1)
            result += num/denum
        return result

    x = float(exist)
    n = int(full)
    approx = sinus(x, n)
    return render_template('def3.html', approx=approx, exist=exist, full=full)

@deff3.route('/def3/ifff')
def ifff():
    one = request.args.get('one')
    two = request.args.get('two')
    three = request.args.get('three')
    four = request.args.get('four')
    if one == '' or two == '' or three == '' or four == '':
        return render_template('def3.html')
    
    def find_num(a, b, c, d):
        if a == b == c:
            return 4
        elif a == b == d:
            return 3
        elif a == c == d:
            return 2
        else:
            return 1

    a = int(one)
    b = int(two)
    c = int(three)
    d = int(four)
    result = find_num(a, b, c, d)
    return render_template('ifff.html', result=result, one=one, two=two, three=three, four=four)


