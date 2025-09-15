#  Calculating Trapezoid Area

from pyscript import document

def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

def calculate_area(event=None):
    try:
        a = float(document.getElementById("a").value)
        b = float(document.getElementById("b").value)
        h = float(document.getElementById("h").value)

        area = trapezoid_area(a, b, h)
        document.getElementById("result").innerText = f"Area = {area:.2f}"
    except Exception:
        document.getElementById("result").innerText = "Please enter valid numbers."

