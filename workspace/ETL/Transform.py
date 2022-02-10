from workspace.Entities.Track import Track
import logging


class Transform:
    @staticmethod
    def transform_data(entities_list):
        logging.basicConfig(filename="search_log_file.log", format='%(asctime)s %(message)s', filemode='w')
        logger = logging.getLogger()

        tracks_list = list()
        for entity in entities_list:
            track = Track(entity['track']['album'], entity['track']['artists'], entity['track']['id'],
                          entity['track']['name'], entity['track']['popularity'])
            tracks_list.append(track)

        if not tracks_list:
            logger.error("Error! Couldn't read the tracks from the file.")

        return tracks_list
