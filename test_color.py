from .color import Color

def test_constructor():
    c1 = Color("red")
    assert c1.toString() == "red"
    assert Color("blue").toString() == "blue"
    assert Color("green").toString() == "green"

def test_mix_rb():
    c1 = Color("red")
    c1.add("blue")
    assert c1.toString() == "magenta"

def test_mix_gb():
    c1 = Color("green")
    c1.add("blue")
    assert c1.toString() == "cyan"


def test_uppercase():
    c1 = Color("Red")
    c1.add("Green")
    assert c1.toString() == "yellow"

def test_operator():
    c1 = Color("blue")
    c2 = Color("yellow")
    c1 + c2
    assert c1.toString() == "white"