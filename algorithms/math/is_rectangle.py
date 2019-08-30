from math import sqrt

 def isRectangle(points):
    a1, a2, a3, a4 = points
    a1x, a1y = a1
    a2x, a2y = a2 
    a3x, a3y = a3 
    a4x, a4y = a4 

     if (a1x - a2x) != 0 and (a3x - a4x) != 0:
        slop1 = (a1y - a2y) / (a1x - a2x)
        slop2 = (a3y - a4y) / (a3x - a4x)
        if slop2 != slop1:
            return False

     if (a2x - a3x) != 0 and (a1x - a4x) != 0:
        slop3 = (a2y - a3y) / (a2x - a3x)
        slop4 = (a1y - a4y) / (a1x - a4x)
        if slop3 != slop4:
            return False


     cx = (a1x + a2x + a3x + a4x) / 4
    cy = (a1y + a2y + a3y + a4y) / 4

     # distance from center of mass

     c1 = sqrt(pow((cx - a1x),2) + pow((cy - a1y),2))
    c2 = sqrt(pow((cx - a2x),2) + pow((cy - a2y),2))
    c3 = sqrt(pow((cx - a3x),2) + pow((cy - a3y),2))
    c4 = sqrt(pow((cx - a4x),2) + pow((cy - a4y),2))

     if len(set([c1,c2,c3,c4])) > 1:
        return False

     return True

 # https://www.wikihow.com/Figure-out-if-Two-Lines-Are-Parallel
# https://stackoverflow.com/questions/2303278/find-if-4-points-on-a-plane-form-a-rectangle
