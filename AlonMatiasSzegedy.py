import random


class Item:
    def __init__(self, id):
        self.id = id
        self.count = 1


class Filter:
    def __init__(self, filter_id):
        self.id = filter_id
        self.items = dict()
        self.size = 0


class AMS:
    # AMS : Alon-Matias-Szegedy algorithm
    def __init__(self, k, stream_size):
        self.__current_index = -1
        self.__indexes = random.sample(range(stream_size), k)
        self.__indexes.sort()
        self.__items = []
        self.__n = stream_size
        self.filtered_items = dict()

    def run(self, item, filter):
        self.__current_index += 1
        if filter not in self.filtered_items:
            self.filtered_items[filter] = Filter(filter)
        self.filtered_items[filter].size += 1
        # Increase string counter
        if item in self.filtered_items[filter].items:
            self.filtered_items[filter].items[item].count += 1
        # If must be added
        elif item in self.__items:
            self.filtered_items[filter].items[item] = Item(item)
        # See index for the first time
        elif self.__current_index in self.__indexes:
            self.filtered_items[filter].items[item] = Item(item)
            self.__items.append(item)

    def getResult(self):
        for filter_id, filter_obj in self.filtered_items.iteritems():
            __sum_counters = 0
            __filter_items_num = 0
            for item_id, item_obj in filter_obj.items.iteritems():
                __sum_counters += filter_obj.size * (2 * item_obj.count - 1)
                __filter_items_num += 1
            yield filter_id, (__sum_counters / __filter_items_num)
