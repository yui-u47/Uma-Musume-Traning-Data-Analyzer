import json
import os
import pandas as pd

from scripts.commands import *

Clear = lambda: os.system("clear")

if __name__ == "__main__":
    while True:
        flags = []

        res = input('> ')
        UserInput = res.split()
        Clear()

        for n in UserInput:
            if "--" in n:
                flags.append(n)
        
        match UserInput[0]:
            case "help":
                HelpCommand()
                
            case "list":
                if flags > 0:
                    pass
                
                print("UMA | CODE")
                for uma in GIDS:
                    print(f"{GIDS[uma][1]} : {uma}")
            case "check":                
                CheckCommand(UserInput, flags)
