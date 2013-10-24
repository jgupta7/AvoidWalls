## Vicki Shaw, Jason Gupta; section B03
## vshaw3@gatech.edu, jgupta7@gatech.edu
##We worked on the homework assignment alone, using only this semester's course materials.

from Myro import *

init("com4")
def avoidWalls():
    for seconds in timer(60):
        while getObstacle()[1] <= 6000:
            forward(.5)

        else:
            stop()
            rotate(.5,1.5)

#Celebration

    backward(0.5,1)
    beep(2,400)

    forward(0.5,0.5)
    beep(2,400)
    backward(0.5,1)
    beep(2,600)
    forward(.5,1)

    stop()