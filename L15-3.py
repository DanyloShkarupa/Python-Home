class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.n = 1

    def first_channel(self):
        print(f'1st channel: {self.channels[0]}')
        self.n = 1
        return self.channels[self.n]

    def last_channel(self):
        print(f'{len(self.channels)} channel: {self.channels[-1]}')
        self.n = len(self.channels)-1
        return self.channels[self.n]

    def turn_channel(self, n):
        print(f'{n} channel: {self.channels[n-1]}')
        self.n = n
        return self.channels[self.n]

    def next_channel(self):
        print(f'{self.n+1} channel: {self.channels[self.n]}')
        self.n += 1
        return self.channels[self.n]

    def previous_channel(self):
        print(f'{self.n-1} channel: {self.channels[self.n-2]}')
        self.n -= 1
        return self.channels[self.n]

    def current_channel(self):
        print(self.channels[self.n])
        return self.channels[self.n]

    def is_exist(self, n):
        try:
            if n-1 in range(len(self.channels)):
                print('Yes')
                return 'Yes'
            else:
                print('No')
                return 'No'
        except:
            if n in self.channels:
                print('Yes')
                return 'Yes'
            else:
                print('No')
                return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.is_exist(4) == "No"

controller.is_exist("BBC") == "Yes"