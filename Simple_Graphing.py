from cmath import exp
import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Setting theme
sg.theme("DarkBlue14")

# Layout setup: 2 columns
table_content = []
layout = [
    # Columns to house the input values and their 
    [sg.Table(headings= ["Observation", "Results"], 
    values = table_content, 
    expand_x=True, 
    hide_vertical_scroll=True,
    key = "-TABLE-")],
    
    # Adding button and input field
    [sg.Input(key = "-INPUT-", 
    expand_x=True, 
    do_not_clear=False
    ),
    sg.Button("Submit")],

    [sg.Canvas(key = "-CANVAS-")],

    # TODO: add bar and pie chart options
    [sg.DropDown(["Line", "Bar", "Pie"], 
    default_value="Line", 
    expand_x=True)]
]

# Initializing the window
window = sg.Window("Simple Graphing", layout, finalize=True)


# Initializing the plot area (figure) and connecting it to the canvas 
fig = matplotlib.figure.Figure(figsize=(5,4))
fig.add_subplot(111).plot([],[])
figure_canvas = FigureCanvasTkAgg(fig, window["-CANVAS-"].TKCanvas)
figure_canvas.draw()
figure_canvas.get_tk_widget().pack()

# Funtion to add input values to chart
def fig_update(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x,y, "ro-")
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Submit":
        new_value = values["-INPUT-"]
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            window["-TABLE-"].update(table_content)
            fig_update(table_content)


window.close()
