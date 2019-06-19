class Army:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.power = 1

cityMap, armyMap = {}, {}
supports = []
def simulate(actions):
    # init army and city
    for actionStr in actions:
        action = actionStr.split(' ')
        name, src, cmd = action[0], action[1], action[2]
        army = Army(name, src)
        armyMap[name] = army
        if cmd == 'Hold':
            if src not in cityMap:
                cityMap[src] = []
            cityMap[src].append(army)
        elif cmd == 'Move':
            dst = action[3]
            army.city = dst
            if dst not in cityMap:
                cityMap[dst] = []
            cityMap[dst].append(army)
        else:
            if src not in cityMap:
                cityMap[src] = []
            cityMap[src].append(army)
            supportee = action[3]
            supports.append((army, supportee))

    # init power
    for support in supports:
        if len(cityMap[support[0].city]) == 1:
            armyMap[support[1]].power += 1

    # state transform
    for city, armyList in cityMap.iteritems():
        strongest = max(armyList, key=lambda x: x.power)
        maxPower = strongest.power
        for army in armyList:
            if army is strongest: continue
            if army.power < maxPower:
                army.power = 0
            elif army.power == maxPower:
                army.power = 0
                strongest.power = 0

    # output
    ans = []
    for name in sorted(armyMap.keys()):
        army = armyMap[name]
        if army.power == 0:
            ans.append('%s [Dead]' % name)
        else:
            ans.append('%s %s' % (name, army.city))
    return ans


input = ["A Munich Hold", "B Bohemia Move Munich", "C Prussia Move Munich", "D Warsaw Hold"]
# input = ["A Munich Support B","B Oakland Move Munich"];
input = ["A Munich Support B", "B Bohemia Move Prussia", "C Prussia Hold", "D Warsaw Move Munich"]
# nput = ["A BJ Hold", "B NJ Support A", "C BJ Hold"]
for line in simulate(input): print line