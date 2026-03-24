import json
import pandas as pd

from scripts.config import *
from scripts.read_data import *

Gids = json.load(open("data/gids.json"))

def GetData(Tittle):
    try:
        df = pd.read_csv(URL.replace('[GID]',Gids[Tittle]))
        return df.to_numpy()
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        res = input('- ')

