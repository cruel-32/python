import sys
import mod1
from mod2 import multi, div

# 1
# import game.sound.echo
# game.sound.echo.echo_test()

# 2
# from game.sound import echo
# echo.echo_test()

# 3
# from game.sound.echo import echo_test
# echo_test()

from game.sound import *

echo.echo_test()


print(sys.path)

print(mod1.add(1, 2))

print(multi(2, 3))

print("__name__ : ", __name__)

