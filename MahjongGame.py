def sorter(e):
    return e.amount


class MahjongTile:
    def __init__(self, amount, type, doraHan):
        self.amount = amount
        self.type = type
        self.doraHan = doraHan
        
    def __str__(self):
        return str(self.amount) + " " + self.type

    def __repr__(self):
        return str(self)


class MahjongHand:
    def __init__(self, playerSeat):
        self.playerSeat = playerSeat
        self.riichi = False
        self.tiles = []
        self.discard = []
        self.menzen = []

    def if_ron(self):
        mans = []
        pins = []
        sous = []
        honors = []
        for tile in self.tiles:
            if tile.type == "man":
                mans.append(tile.amount)
            elif tile.type == "pin":
                pins.append(tile.amount)
            elif tile.type == "sou":
                sous.append(tile.amount)
            else:
                honors.append(tile.type)

        mans.sort(key=sorter)
        pins.sort(key=sorter)
        sous.sort(key=sorter)
        honors.sort(key=sorter)


    def detect_remove_trios(self, listed):
        occurrence = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for tile in listed:
            occurrence[tile.amount-1] += 1
        
        recount = occurrence.copy()
        for i in range(0, 9):
            recount[i] = min(recount[i], 3)
            
        trios = 0
        for tile in listed:
            if (occurrence[tile.amount-1] >= 3 and recount[tile.amount-1] > 0):
                recount[tile.amount-1] -= 1
                tile.amount = 0
                trios += 1
                
        reconstruct = []
        for tile in listed:
            if tile.amount != 0:
                reconstruct.append(tile)
        
        listed.clear()
        for tile in reconstruct:
            listed.append(tile)
        
        return int(trios/3)
