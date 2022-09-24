import gui
import db
import math_f

def Calc():
    arg_1 = gui.input_data()
    db.export('arg_1 = ' + str(arg_1))
    arg_2 = gui.input_data()
    db.export('arg_2 = ' + str(arg_2))
    option = gui.user_option()
    result = 0
    match option:
        case 1:
            result = math_f.summ(arg_1, arg_2)
        case 2:
            result = math_f.subs(arg_1, arg_2)
        case 3:
            result = math_f.mult(arg_1, arg_2)
        case 4:
            result = math_f.div(arg_1, arg_2)
    db.export('result = ' + str(result))
    gui.output_data(result)