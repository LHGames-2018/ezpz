from helper import *


class Bot:
    def __init__(self):
        self.count = 0

        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        def RetourMaison():
            DirectionMaison = self.PlayerInfo.Position - self.PlayerInfo.HouseLocation

            if DirectionMaison.y < 0:
                return create_move_action(Point(0, 1))
            elif DirectionMaison.y > 0:
                return create_move_action(Point(0, -1))
            elif DirectionMaison.x < 0:
                return create_move_action(Point(1, 0))
            elif DirectionMaison.x > 0:
                return create_move_action(Point(-1, 0))
            else:
                trouverObjet()

        def MarcheRoche():
            DirectionRoche = self.PlayerInfo.Position - (self.PlayerInfo.HouseLocation - Point(-3, -5))
            if DirectionRoche.y < 0:
                return create_move_action(Point(0, 1))
            elif DirectionRoche.y > 0:
                return create_move_action(Point(0, -1))
            elif DirectionRoche.x < 0:
                return create_move_action(Point(1, 0))
            elif DirectionRoche.x > 0:
                return create_move_action(Point(-1, 0))
            else:
                return create_empty_action()

        def faireMouvement(direction):
            if direction.y < 0:
                return create_move_action(Point(0, 1))
            elif direction.y > 0:
                return create_move_action(Point(0, -1))
            elif direction.x < 0:
                return create_move_action(Point(1, 0))
            elif direction.x > 0:
                return create_move_action(Point(-1, 0))

        def trouverObjet(type):
            position = self.PlayerInfo.Position
            if gameMap.getTileAt(Point(position.x + 1, position.y)) == TileContent(1) or gameMap.getTileAt(
                    Point(position.x + 1, position.y)) == TileContent(6):
                return create_attack_action(Point(1, 0))
            if gameMap.getTileAt(Point(position.x - 1, position.y)) == TileContent(1) or gameMap.getTileAt(
                    Point(position.x - 1, position.y)) == TileContent(6):
                return create_attack_action(Point(-1, 0))
            if gameMap.getTileAt(Point(position.x, position.y + 1)) == TileContent(1) or gameMap.getTileAt(
                    Point(position.x, position.y + 1)) == TileContent(6):
                return create_attack_action(Point(0, 1))
            if gameMap.getTileAt(Point(position.x, position.y - 1)) == TileContent(1) or gameMap.getTileAt(
                    Point(position.x, position.y - 1)) == TileContent(6):
                return create_attack_action(Point(0, -1))

            if self.PlayerInfo.CarriedResources == self.PlayerInfo.CarryingCapacity:
                return RetourMaison()

            if gameMap.getTileAt(Point(position.x + 1, position.y)) == TileContent(4):
                return create_collect_action(Point(1, 0))
            if gameMap.getTileAt(Point(position.x - 1, position.y)) == TileContent(4):
                return create_collect_action(Point(-1, 0))
            if gameMap.getTileAt(Point(position.x, position.y + 1)) == TileContent(4):
                return create_collect_action(Point(0, 1))
            if gameMap.getTileAt(Point(position.x, position.y - 1)) == TileContent(4):
                return create_collect_action(Point(0, -1))



            position = self.PlayerInfo.Position
            roche = []
            for y in range(position.y - 10, position.y + 10):
                for x in range(position.x - 10, position.x + 10):
                    if gameMap.getTileAt(Point(x, y)) == TileContent(type):
                        roche.append(Point(x, y))
            petitdistance=10000
            for x in range(len(roche)):
                distance = roche[x].Distance(roche[x], position)
                if(distance<=petitdistance):
                    petitPoint=roche[x]
            x=petitPoint.x
            y=petitPoint.y
            if position.x - x == 1 and position.y - y == 0:
                return create_collect_action(Point(-1, 0))
            elif position.x - x == -1 and position.y - y == 0:
                return create_collect_action(Point(1, 0))
            if position.y - y == 1 and position.x - x == 0:
                return create_collect_action(Point(0, -1))
            elif position.y - y == -1 and position.x - x == 0:
                return create_collect_action(Point(0, 1))
            direction = position - Point(x, y)
            return faireMouvement(direction)

        def bouger():
            direction = self.PlayerInfo.Position - (self.PlayerInfo.HouseLocation - Point(-5, 3))

            if direction.x < 0:
                return create_move_action(Point(1, 0))
            elif direction.x > 0:
                return create_move_action(Point(-1, 0))
            elif direction.y < 0:
                return create_move_action(Point(0, 1))
            elif direction.y > 0:
                return create_move_action(Point(0, -1))

            else:

                return create_collect_action(Point(0, -1))

        return trouverObjet(4)

        # return RetourMaison()

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
