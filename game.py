from menu import *

summon_menu()

from menu import gameactive

if gameactive:

    from clickerexterior import *
    from notefunctions import *
    from songanalyzer import *
    from menu import *

    playGame(gamearr=timearr, timeout=times[-1], waiting=2)

    print("Game finished!")

print("Game exited")
