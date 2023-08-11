from rest_framework import status
from rest_framework.exceptions import APIException


class AlbumNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Album not found.'
    default_code = 'album_not_found'

    def __init__(self, album_id):
        self.album_id = album_id
        self.msg = f"Album with ID {album_id} not found"
        super().__init__(self.msg)


class AlbumAlreadyExistException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Album already exist.'
    default_code = 'album_already_exist'

    def __init__(self, title):
        self.title = title
        self.msg = f"Album with title {title} already exist"
        print(self.msg)
        super().__init__(self.msg)


class CheckSentDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Check sent data.'
    default_code = 'check_sent_data'

    def __init__(self):
        self.msg = "Check sent data: title max length is 190, release_year is integer between 1900 and today's year"
        super().__init__(self.msg)
