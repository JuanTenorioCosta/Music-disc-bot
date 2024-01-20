import os

from FakeDBs.DbHandler.DbHandler import DbHandler

class RuletaModel(DbHandler):
    def __init__(self):
      current_dir = os.path.dirname(__file__)
      file_rel_path = "ruleta.json"
      super().__init__(os.path.join(current_dir, file_rel_path))

    def userHasGames( self, username: str ) -> bool:
      try:
        userGames = self._getById(username)
        if len(userGames) > 0:
          return True
        else:
          return False
      except AttributeError:
        return False
      
    def userHasGame( self, username: str, gameName: str ) -> bool:
      try:
        userGames = self._getById(username)
        for game in userGames:
          if gameName == game["name"]:
            return True
        else:
          return False
      except AttributeError:
        return False

    # Conseguir juegos. Devuelve del usuario o en su defecto los por defecto
    def getGames( self, username: str, numPlayers: int = 0 ) -> dict:
      try:
        userGames = self._getById(username)
      except AttributeError:
        userGames = self._getById("default")
      if numPlayers == 0:
        return userGames
      else:
        validUserGames = []
        for game in userGames:
          if "availableNumPlayers" in game:
            if numPlayers in game["availableNumPlayers"]:
              validUserGames.append(game)
          else:
            validUserGames.append(game)
        return validUserGames

    # Escribir un juego para un usuario
    def writeGame(self, username: str, content: dict) -> None:
      try:
        games: [dict] = self._getById( username )
      except AttributeError:
        games: [dict] = []
      
      for game in games:
        if(game["name"] == content["name"]):
          game["availableNumPlayers"] = content["availableNumPlayers"]
          break
      else:
        games.append(content)
    
      try:
        self._writeContentById(username, games)
      except AttributeError:
        raise AttributeError
    
    # Borrar la ruleta de un usuario
    def deleteAllGames( self, username: str ) -> None:
      try:
        self._deleteContentById( username )
      except AttributeError:
        raise AttributeError

    # Borrar solo un juego de un usuario
    def deleteGame( self, username: str, gameName: str ) -> None:
      try:
        games: [dict] = self._getById( username )
      except AttributeError:
        raise AttributeError
      
      for game in games:
        if(game["name"] == gameName):
          games.remove(game)
          break
      else:
        raise AttributeError
    
      self._writeContentById( username, games )