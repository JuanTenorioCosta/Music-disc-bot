import json

class DbHandler():
    def __init__(self, path):
      self.file_path = path

    def _getFromJson(self) -> dict:
      with open(self.file_path, 'r') as file:
          return json.load(file)

    def _getAllValues(self) -> dict:
      return self._getFromJson()

    def _getById( self, id ) -> dict:
      values = self._getFromJson()
      if id in values:
        return values[id]
      else:
        raise AttributeError


    def _overwriteFile( self, overwrite: dict ) -> None:
      with open(self.file_path, "w") as writing_file:
        json.dump(overwrite, writing_file, indent=2)

    def _writeContentById( self, id, content) -> None:
      fileContent: dict = self._getFromJson()
      fileContent[id] = content
      self._overwriteFile(fileContent)
    
    
    def _deleteContentById( self, id ) -> None:
      fileContent: dict = self._getFromJson()
      if id in fileContent:
        del fileContent[id]
      else:
        raise AttributeError
      
      self._overwriteFile(fileContent)