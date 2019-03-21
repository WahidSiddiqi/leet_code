def hasGroupsSizeX(deck):
        deck_dict = dict()
        for numb in deck:
            deck_dict[numb] = deck_dict.get(numb, 0) + 1

        if len(list(set({1: 3, 2: 3, 3: 1}.values()))) == 1:
            print(len(list(set({1: 3, 2: 3, 3: 1}.values()))))
        else:
            print('False')