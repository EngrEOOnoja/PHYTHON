from idlelib.configdialog import changes


def change(x, y, z):
    return (z, x, y)   # third → first, first → second, second → third


a, b, c = 'Doug', 22, 1984
a, b, c = change(a, b, c)
print(a, b, c)
a, b, c = change(a, b, c)
print(a, b, c)
a, b, c = change(a, b, c)
print(a, b, c)

