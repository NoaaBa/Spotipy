from workspace.Entities.Track import Track


class Transform:
    @staticmethod
    def transform_data(entities_list):
        tracks_list = list()
        for entity in entities_list:
            track = Track(entity['track']['album'], entity['track']['artists'], entity['track']['id'],
                          entity['track']['name'], entity['track']['popularity'])
            tracks_list.append(track)

        return tracks_list
