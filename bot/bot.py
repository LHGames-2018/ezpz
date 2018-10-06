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
                return create_empty_action()

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

            for x in range(0, 21):
                for y in range(0, 21):
                    if gameMap.getTileAt(Point(0, 0)) == type:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(-1, 0))

                    elif gameMap.getTileAt(Point(0, 0)) == 0:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(-1, 0))

                    elif gameMap.getTileAt(Point(0, 0)) == 1:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(-1, 0))

                    elif gameMap.getTileAt(Point(0, 0)) == 2:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(-1, 0))

                    elif gameMap.getTileAt(Point(0, 0)) == 3:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(-1, 0))


                    elif gameMap.getTileAt(Point(0, 0)) == 4:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(-1, 0))

                    if gameMap.getTileAt(Point(0, 0)) == 5:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(1, 0))

                    if gameMap.getTileAt(Point(0, 0)) == 6:
                        position = Point(x, y)
                        direction = position - Point(10, 10)
                        return create_move_action(Point(1, 0))

        def bouger():
            direction = self.PlayerInfo.Position - (self.PlayerInfo.HouseLocation - Point(-5,3))

            if direction.x < 0:
                return create_move_action(Point(1, 0))
            elif direction.x > 0:
                return create_move_action(Point(-1, 0))
            elif direction.y < 0:
                return create_move_action(Point(0, 1))
            elif direction.y > 0:
                return create_move_action(Point(0, -1))

            else:
                self.count += 1
                return create_collect_action(Point(0, -1))


        return RetourMaison()

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
