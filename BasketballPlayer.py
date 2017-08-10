import uuid


class BasketballPlayer:
    def __init__(self, name='', age=0, height=0, weight=0, team='', number=0, position='',
                 points_per_game=0, assist_per_game=0, blocks_per_game=0, rebounds_per_game=0, fouls_per_game=0,
                 steals_per_game=0, freethrows_per_game=0, championships_won=0, id=uuid.uuid4(), image=None):
        self.id = id
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.team = team
        self.number = number
        self.position = position
        self.points_per_game = points_per_game
        self.assist_per_game = assist_per_game
        self.blocks_per_game = blocks_per_game
        self.rebounds_per_game = rebounds_per_game
        self.fouls_per_game = fouls_per_game
        self.steals_per_game = steals_per_game
        self.freethrows_per_game = freethrows_per_game
        self.championships_won = championships_won
        self.image = image
