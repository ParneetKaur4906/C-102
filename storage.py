import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BJn4KnKazHQPnUsfJNjoUtZE1KddZc4oKGFO88tNNJI9JzGydUOqKfUxZuiKHenz3m9duSlrrhab5j0XU0Fx_NtEsETYdzdQcWGscIVceYBhAPPqutL-9gP_t9GRLW3QmFArJTY'
    transferData = TransferData(access_token)

    file_from = 'parneet.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

main()