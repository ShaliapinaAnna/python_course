class Song:
    def __init__(self, name, singer):
        self.__time = None
        self.name = name
        self._singer = singer
        self.__time = '3:11'


song = Song('Save Your Tears', 'The Weeknd')
print(song.name, song._singer, song.__time)
