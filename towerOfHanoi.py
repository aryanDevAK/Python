# Objective and rules of the puzzle
# The objective is to move n number of disks from one tower to another following a set of rules. These rules are as follows: 

# Only one disk can be moved at a time 

# Only the upper disk of any of the towers can be moved 

# Larger disks cannot be placed over smaller disks

def towerOfHanoi(disks,source,helper,destination):
    if disks==1:
        print(f"Disk {disks} moves from tower {source} to tower {destination}")
        return
    towerOfHanoi(disks-1,source,destination,helper)
    print(f"Disk {disks} moves from tower {source} to tower {destination}")
    towerOfHanoi(disks-1,helper,source,destination)

numberOfDisks = int(input("Enter number of disks to be moved :"))
towerOfHanoi(numberOfDisks,"A","B","C")
