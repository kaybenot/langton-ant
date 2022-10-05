from langton import *
import console
import sys


def main(argv):
    '''
    Glowna funkcja uruchamiajaca program.
    Pobiera argumenty.
    '''
    if argv[0] == '-h' or argv[0] == '--help':
        console.help()
        return
    elif argv[0] == '-v' or argv[0] == '--version':
        console.version()
        return
    elif len(argv) < 2 and len(argv) > 5:
        print("Zla ilosc argumentow!")
        console.help()
        return
    windowW = int(argv[0])
    windowH = int(argv[1])
    if len(argv) > 2:
        scale = int(argv[2])
        w = int(argv[0]) // scale
        h = int(argv[1]) // scale
        if scale <= 0 or w == 0 or h == 0:
            print(
            "Niepoprawna skala, powinna być w przedziale" +
            "[1, rozmiar okna]")
            return
    else:
        w = int(argv[0]) // 10
        h = int(argv[1]) // 10
    if len(argv) > 3:
        fps = int(argv[3])
    else:
        fps = 120
    if len(argv) > 4 and str(argv[4]) == "draw":
        lt = Langton(windowW, windowH, w, h, fps, True)
    else:
        lt = Langton(windowW, windowH, w, h, fps, False)
    lt.run()


if __name__ == "__main__":
    main(sys.argv[1:])
