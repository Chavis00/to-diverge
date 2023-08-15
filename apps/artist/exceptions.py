from rest_framework import status
from rest_framework.exceptions import APIException


class ArtistNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Artist not found.'
    default_code = 'artist_not_found'

    def __init__(self, artist_id):
        self.album_id = artist_id
        self.msg = f"Artist with ID {artist_id} not found"
        super().__init__(self.msg)


class ArtistAlreadyExistException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Artist already exist.'
    default_code = 'artist_already_exist'

    def __init__(self, name):
        self.title = name
        self.msg = f"Artist with name1 {name} already exist"
        print(self.msg)
        super().__init__(self.msg)


class CheckSentDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Check sent data.'
    default_code = 'check_sent_data'

    def __init__(self):
        self.msg = "Check sent data: name must be not empty and albums must be list of albums"
        super().__init__(self.msg)
