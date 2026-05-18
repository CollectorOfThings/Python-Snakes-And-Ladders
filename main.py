import random

SnakesAndLadders = {
    1:12,
    5:16,
    11:22,
    15:23,
    20:31,
    7:4,
    10:2,
    21:13,
    24:6,
    33:19
}

FinishPos = 34

class Player():
    def __init__(self,StartPosition,PlayerNum):
        self.StartPosition = StartPosition
        self.Position = StartPosition
        self.PlayerNum = PlayerNum
        self.Win = False
    
    def Roll(self):
        d = random.randint(1,6)
        self.Position += d
        if self.Position in SnakesAndLadders:
            self.Position = SnakesAndLadders[self.Position]
        #print(f'Player: {self.PlayerNum} Roll: {d} Position: {self.Position}')
        if self.Position >= FinishPos:
            self.Win = True
    
    def Reset(self):
        self.Position = self.StartPosition
        self.Win = False
    

class Game():
    def __init__(self,Players):
        self.Players = Players
        self.Winner = None
        self.Rolls = 0
        
    def Play(self):
        while self.Winner == None:
            for p in self.Players:
                p.Roll()
                self.Rolls+=1
                if p.Win:
                    self.Winner = p.PlayerNum             
                    return       
                    
    def Reset(self):
        self.Winner = None
        self.Rolls = 0
        for p in self.Players:
            p.Reset()

def OnePlayerGame():
    P1 = Player(0,1)
    Wins = []
    Rolls = []
    Players = [P1]
    G = Game(Players)
    for i in range(1, 10001):
        G.Play()
        Wins.append(G.Winner)
        Rolls.append(G.Rolls)
        G.Reset()
    print('One Player Game')
    print(f'Player One Winrate: {Wins.count(1) / len(Wins)}')
    print(f'One Player Game Average Rolls: {sum(Rolls) / len(Rolls)}')

def TwoPlayerGame(PlayerTwoStartPos):
    P1 = Player(0,1)
    P2 = Player(PlayerTwoStartPos,2)
    Wins = []
    Rolls = []
    Players = [P1,P2]
    G = Game(Players)
    for i in range(1, 10001):
        G.Play()
        Wins.append(G.Winner)
        Rolls.append(G.Rolls)
        G.Reset()
    print('\nTwo Player Game')
    print(f'Player Two Start Position {PlayerTwoStartPos}')
    print(f'Player One Winrate: {Wins.count(1) / len(Wins)}')
    print(f'Player Two Winrate: {Wins.count(2) / len(Wins)}')
    print(f'Two Player Game Average Rolls: {sum(Rolls) / len(Rolls)}')

if __name__ == "__main__":
    OnePlayerGame() 
    TwoPlayerGame(0) 

    TwoPlayerGame(3)
    TwoPlayerGame(6)
    TwoPlayerGame(9)
    TwoPlayerGame(12) 


