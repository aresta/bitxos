import bitxos.consts
from bitxos.world.land import Land


class World:
    
    time = 0  # Universal time in ticks, shared with all organisms
    world = None

    def __init__(self):
        self.land = Land()
        self.organisms = []

    @classmethod
    def getWorld(cls):
        if cls.world is None: 
            cls.world = World()
        return cls.world

    def get_organism_at_distance(self, organism, dist):
        """Returns lists of (organism, distance) at distance less than dist"""
        orgs = []
        for org in self.organisms:
            if org == organism: continue
            org_distance = org.distance(organism)
            if org_distance < dist:
                orgs.append((org, org_distance))
        return orgs
