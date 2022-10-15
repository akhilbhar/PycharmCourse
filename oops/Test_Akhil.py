print(f"first module's name is {__name__}")

from oops.CreatingConstructor import Operation

if __name__ == '__main__':
    ops = Operation(10,5)
    ops.add()