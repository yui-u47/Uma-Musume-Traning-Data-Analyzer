import json
import pandas as pd

from scripts.config import *
from scripts.read_data import *

Gids = json.load(open("data/gids.json"))

def GetData(Tittle):
    print(Tittle)
    df = pd.read_csv(URL.replace('[GID]',Gids[Tittle]))
    return df.to_numpy()

if __name__ == "__main__":
    while True:
        flags = False

        res = input('> ')
        UserInput = res.split()

        if "--" in res:
            flags = True

        match UserInput[0]:
            case "help":
                pass
            case "check":
                pass
            case "":
                pass

