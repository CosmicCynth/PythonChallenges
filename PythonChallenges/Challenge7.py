#Create a function that takes damage and speed (attacks per second)
#and returns the amount of damage after a given time.

def DamagePerSecond(Damage,Time):
    DPS = Damage/Time
    DPS = round(DPS,2)
    return DPS

print("DPS: " + str(DamagePerSecond(17600,5.7)))