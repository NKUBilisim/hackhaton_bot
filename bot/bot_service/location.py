class Location():

    def __init__(self, **kwargs):
        if "location" in kwargs:
            self.location = kwargs["location"]
        else:
            self.location = None

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location


