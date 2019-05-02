class RecordLog:
    def __init__(self, data, capacity):
        self.cap = capacity
        if len(data) > capacity:
            self.log = dict(enumerate(data[-capacity:]))
        else:
            self.log = dict(enumerate(data))
        self.ptr = len(data) % capacity

    def __repr__(self):
        return self.log.__str__()

    def add_entry(self, entry):
        self.log[self.ptr % self.cap] = entry
        self.ptr += 1

    def get_nth_last_entry(self, index):
        return self.log[(self.ptr - index) % self.cap]


def record(recs, order_id):
    recs.add_entry(order_id)


def get_last(recs, i):
    return recs.get_nth_last_entry(i)


if __name__ == "__main__":
    cap = 5
    data = [1, 2, 3, 4, 5]
    recs = RecordLog(data, cap)
    print(get_last(recs, 1))
    recs.add_entry(6)
    print(recs)
    print(get_last(recs, 1))
    recs.add_entry(7)
    print(recs)
    print(get_last(recs, 1))
    print(get_last(recs, 2))