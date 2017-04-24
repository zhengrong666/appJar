import sys
sys.path.append("../../")
from appJar import gui

def press(*args):
    if args[0]=="newRow":
        app.addGridRow('airflow_data_raw', app.getGridEntries('airflow_data_raw'))
    else:
        print(args)

app=gui("GridTest")


app.startLabelFrame("Standard Conditions", 0, 0)
app.addLabel("st1", "Temperature", 0, 0)
app.addEntry("sTemperature", 0, 1)
app.addLabel("st2", "oF", 0, 2)
app.addLabel("sp1", "Pressure", 1, 0)
app.addEntry("sPressure", 1, 1)
app.addLabel("sp2", "in Hg", 1, 2)
app.stopLabelFrame()

app.startLabelFrame("Conditions", 0, 1)
app.addLabel("t1", "Temperature", 0, 0)
app.addEntry("temperature", 0, 1)
app.addLabel("t2", "oF", 0, 2)
app.addLabel("p1", "Pressure", 1, 0)
app.addEntry("pressure", 1, 1)
app.addLabel("p2", "in Hg", 1, 2)
app.stopLabelFrame()

app.startLabelFrame("Scaling", 0, 2)
app.addLabel("s1", "Speed", 0, 0)
app.addEntry("speed", 0, 1)
app.addLabel("s2", "Size", 1, 0)
app.addEntry("size", 1, 1)
app.stopLabelFrame()

app.addGrid(
    'airflow_data_raw',
    [
        ['Nozzle Diameter', 'Number of Nozzles', 'Differential Pressure', 'Static Pressure', 'Voltage', 'Current', 'Frequency'],
    ],
    row=1,
    column=0,
    colspan=3,
    action=press,
    addRow=True
)

app.go()
