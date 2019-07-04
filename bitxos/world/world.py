import bitxos.consts
from bitxos.world.land import Land


class World:
    
    time = 0  # Universal time in ticks, shares with all organisms
    world = None

    def __init__(self):
        self.land = Land()
        self.organisms = []

    @classmethod
    def getWorld(cls):
        if cls.world is None: 
            cls.world = World()
        return cls.world

    def get_organism_at_distances(self, organism, dist_1, dist_2):
        """Returns 2 lists of organism:
            - from 1 to dist_1
            - from dist_1 to dist_2
        """
        orgs_1, orgs_2 = [], []
        for org in self.organisms:
            if org == organism:
                continue
            dist = org.distance(organism)
            if 1 <= dist <= dist_1:
                orgs_1.append(org)
            elif dist <= dist_2:
                orgs_2.append(org)
        return orgs_1, orgs_2
