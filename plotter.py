# python3.10

import Equation as eq
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np


def main():
    file_input_column = [
        [
            sg.Text("Insert an Equation:"),
        ],
        [
            sg.In(size=(50, 2), enable_events=True, key="-EQUATION-"),
        ],
        [
            sg.Text("Enter Lower Bound: "),
            sg.In(size=(31, 1), enable_events=True, key="-MINVALUE-"),
        ],
        [
            sg.Text("Enter Higher Bound:"),
            sg.In(size=(31, 1), enable_events=True, key="-MAXVALUE-"),
        ],
        [
            sg.Button(button_text="Plot", enable_events=True, key="-PLOTBUTTON-", size=(30, 2), pad=(55, 10)),
        ],
    ]
    file_output_column = [
        [
            sg.Text(font=["", 20, "bold"], text="Result", justification="center"),
        ],
        [
            sg.Text(key="-RESULTOF-", justification="center"),
        ],
    ]
    layout = [
        [
            sg.Column(file_input_column),
            sg.VSeparator(),
            sg.Column(file_output_column, element_justification="center"),
        ],
    ]
    window = sg.Window("Function Plotter", layout)
    while True:
        event, values = window.Read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-EQUATION-":
            eqn = values["-EQUATION-"]
            assert isinstance(eqn, str)
        if event == "-MINVALUE-":
            a = values["-MINVALUE-"]
        if event == "-MAXVALUE-":
            b = values["-MAXVALUE-"]
        if event == "-PLOTBUTTON-":
            try:
                assert isinstance(int(a), int)
                assert isinstance(int(b), int)
                solve_x = eq.Expression(expression=eqn, argorder=["x"])
                xlist = np.linspace(int(a), int(b), num=1000)
                ylist = solve_x(xlist)
                plt.figure(num=0, dpi=120)
                plt.plot(xlist, ylist)
                plt.xlabel("X")
                plt.ylabel("f(X)")
                plt.show()
            finally:
                window["-RESULTOF-"].update("please enter an equation")
    window.close()


if __name__ == "__main__":
    main()
