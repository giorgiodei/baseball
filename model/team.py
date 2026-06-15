import dataclasses


@dataclasses.dataclass
class Team():
    div_ID : int
    divID: str
    divisionWinnner: str
    games: int
    gamesHome: int
    hits: int
    hitsAllowed: int
    homeruns: int
    homerunsAllowed: int
    ID: int
    leagueWinner: str
    losses: int
    name: str
    park: str
    runs: int
    stolenBases: int
    teamCode: str
    teamRank: int
    wins: int
    worldSeriesWinnner: str
    year: int


    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return f"{self.name} ({self.teamCode})"