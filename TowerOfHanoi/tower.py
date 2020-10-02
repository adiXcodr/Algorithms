def tower(disks, startRing, tempRing, endRing):
    if disks == 1:
        print('Move disk 1 from tower {} to tower {}.'.format(startRing, endRing))
        return
 
    tower(disks - 1, startRing, endRing, tempRing)
    print('Move disk {} from tower {} to tower {}.'.format(disks, startRing, endRing))
    tower(disks - 1, tempRing, startRing, endRing)
 
 
disks = 3
tower(disks, 'A', 'B', 'C')
