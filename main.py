import json
import pandas as pd

from scripts.config import *
from scripts.read_data import *

Gids = json.load(open("data/gids.json"))


def GetData(Title):
    try:
        df = pd.read_csv(URL.replace('[GID]',Gids[Title][0]))
        return df.to_numpy()
    except:
        return "error"

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
            case "list":
                if flags:
                    pass
                
                print("UMA | CODE")
                for uma in Gids:
                    print(f"{Gids[uma][1]} : {uma}")
            case "check":                
                if flags:
                    pass

                Data = GetData(UserInput[1])

                print(f"There are {len(Data)} playthrough resgister in the {Gids[UserInput[1]][1]} database.")

