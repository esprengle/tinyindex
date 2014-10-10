class Index():
    def __init__(self, db, *keys, **kwargs):
        self.db = db
        self.keys = keys
        self.reverse = kwargs.get('reverse', False)

    def matches_keys(self, datum):
        return all(key in datum for key in self.keys)

    def all(self):
        for item in self.db.all():
            if self.matches_keys(item):
                yield item

    @property
    def keyfunc(self):
        def function(datum):
            return tuple(datum[k] for k in self.keys)
        return function

    def ranked(self):
        records = list(self.all())
        records.sort(
            key=self.keyfunc,
            reverse=self.reverse,
        )
        return records

    def __iter__(self):
        for item in self.ranked():
            yield item

    def __getitem__(self, idx):
        return self.ranked()[idx]
