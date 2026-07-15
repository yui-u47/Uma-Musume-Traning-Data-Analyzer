import json

import numpy as np
import pandas as pd

GIDS = json.load(open("data/gids.json"))
DOCUMENT_ID = "1Axt8wCL-um4cg6LLgkkUrH3iEzycwukGivAwNIaQWso"
URL = f"https://docs.google.com/spreadsheets/d/{DOCUMENT_ID}/export?format=csv&gid=[GID]"

def __GetData(Title):
    try:
        df = pd.read_csv(URL.replace('[GID]',GIDS[Title][0]))
        return df.to_numpy()
    except:
        return e

def HelpCommand():
    Umas = []
    for data in GIDS:
        Umas.append(data)
    
    print("Exact code for every Uma:")
    print("UMA | CODE")
    for uma in Umas:
        print(f"{GIDS[uma][1]} : {uma}" )

def CheckCommand(UserInput, flags):
    if len(flags) > 0:
        for flag in flags:
            match flag:
                case '--best':
                    Data = __GetData(UserInput[len(UserInput)-1])

                    if len(Data) > 0:
                        BestPlay = []
                        BestRate = 0

                        for d in Data:
                            if d[12] > BestRate:
                                BestRate = d[12]
                                BestPlay = d

                        stats = f"""| SPEED | STAMINA | POWER | GUTS | WIT | 
| {d[2]} | {d[3]} | {d[4]} | {d[5]} | {d[6]} |"""

                        print(f"Rating: {d[12]}")
                        print(stats)
                        print(f"Scenario Link: {d[13]}")
                        print(f"Total Skill Points: {d[8]}")
                        print(f"Win-rate: {d[10]/d[9]}%")
                        print(f"Total Fans: {d[11]}")
                        print(f"Deck: {d[14]}")
                    else:
                        print("There are no playthroughs register yet.")
    else:
        Data = __GetData(UserInput[1])

        print(f"There are {len(Data)} playthroughs resgister in the {GIDS[UserInput[1]][1]} database.")