import os
import pickle

from molpher.algorithms.classic.pathfinder import ClassicPathFinder


def run(settings):
    """
    Run a search with the given settings and return the path found.

    :param settings: `Settings` instance
    :return: path as a `list` of `str`
    """

    pathfinder = ClassicPathFinder(settings)
    pathfinder()

    # pickle the resulting path
    pickled_path = open(os.path.join(settings.storage_dir, 'path.pickle'), mode='wb')
    pickle.dump(pathfinder.path, pickled_path)
    pickled_path.close()

    return pathfinder.path