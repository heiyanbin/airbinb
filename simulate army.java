static List<String> emulateArmy(List<String> actions) {
        class Army implements Comparable<Army> {
            String name;
            String city;
            String supporting;
            int strength = 1;
            public Army(String name, String city) {
                this.name = name;
                this.city = city;
            }
            @Override
            public int compareTo(Army o) {
                return this.name.compareTo(o.name);
            }
        }

        Map<String, List<Army>> cityMap = new HashMap<> ();
        Map<String, Army> armyMap = new TreeMap<>();
        List<String> supportList = new ArrayList<>();
        for (String line : actions) {
            String[] action = line.split(" ");
            String name = action[0], src = action[1], cmd = action[2];
            if (cmd.equals("Move")) {
                String dst = action[3];
                Army army = new Army(name, dst);
                armyMap.put(name, army);
                if (!cityMap.containsKey(dst)) {
                    cityMap.put(dst, new ArrayList<>());
                }
                cityMap.get(dst).add(army);
            }
            else if (cmd.equals("Hold")) {
                Army army = new Army(name, src);
                armyMap.put(name, army);
                if (!cityMap.containsKey(src)) {
                    cityMap.put(src, new ArrayList<>());
                }
                cityMap.get(src).add(army);
            }
            else {
                Army army = new Army(name, src);
                army.supporting = action[3];
                armyMap.put(name, army);
                supportList.add(name);
                if (!cityMap.containsKey(src)) {
                    cityMap.put(src, new ArrayList<>());
                }
                cityMap.get(src).add(army);
            }
        }

        for (String name: supportList) {
            Army supportingArmy = armyMap.get(name);
            if (cityMap.get(supportingArmy.city).size() == 1) {
                Army supportedArmy = armyMap.get(supportingArmy.supporting);
                supportedArmy.strength += 1;
            }
        }

        for (List<Army> city : cityMap.values()) {
            if (city.size() == 1) continue;
            int bully = 0, bullyIndex = -1;
            for (int i = 0; i < city.size(); ++i) {
                if (city.get(i).strength > bully) {
                   bully = city.get(i).strength;
                   bullyIndex = i;
                }
            }
            for (int i = 0; i < city.size(); ++i) {
                if (i == bullyIndex) continue;
                Army army = city.get(i);
                if (army.strength < bully) {
                    army.strength = 0;
                }
                else if (army.strength == bully) {
                    army.strength = 0;
                    city.get(bullyIndex).strength = 0;
                }
            }
        }
        List<String> ans = new ArrayList<>();
        for (Map.Entry<String, Army> en : armyMap.entrySet()) {
            Army a = en.getValue();
            if (a.strength == 0) {
                ans.add(a.name + " [dead]");
            }
            else {
                ans.add(a.name + " " + a.city);
            }
        }
        return ans;
    }