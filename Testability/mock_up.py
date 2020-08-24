import operator
from unittest.mock import Mock, MagicMock


class TextSearcher:

    def __init__(self, db):
        """ Initializer - keyword and database object """
        self.cache = False
        self.cache_dict = {}
        self.db = db
        self.db.connect()

    def setup(self, cache=False, max_items=500):
        """ Setup parameters such as caching """
        self.cache = cache
        # Call configure on the db
        self.db.configure(max_items=max_items)

    def get_results(self, keyword, num=10):
        """ Query keyword on db and get results for given keyword """

        # If results in cache return from there
        if keyword in self.cache_dict:
            print('From cache')
            return self.cache_dict[keyword]

        results = self.db.query(keyword)
        # Results are list of (string, weightage) tuples
        results = sorted(results, key=operator.itemgetter(1), reverse=True)[:num]
        # Cache it
        if self.cache:
            self.cache_dict[keyword] = results

        return results


def test_search():
    """ Test search via a mock """
    # Mock the database object
    db = Mock()
    searcher = TextSearcher(db)
    # Verify connect has been called with no arguments
    db.connect.assert_called_with()
    # Setup searcher
    searcher.setup(cache=True, max_items=100)
    # Verify configure called on db with correct parameter
    searcher.db.configure.assert_called_with(max_items=100)
    canned_results = [('Python is wonderful', 0.4),
                      ('I like Python', 0.8),
                      ('Python is easy', 0.5),
                      ('Python can be learnt in an afternoon!', 0.3)]
    db.query = MagicMock(return_value=canned_results)
    # Mock the results data
    keyword, num = 'python', 3
    data = searcher.get_results(keyword, num=num)
    searcher.db.query.assert_called_with(keyword)
    # Verify data
    results = sorted(canned_results, key=operator.itemgetter(1),
                     reverse=True)[:num]
    assert data == results


if __name__ == "__main__":
    print("Start testing")
    test_search()
    print("Done testing")



