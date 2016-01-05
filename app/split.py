from utils.tools import to_bcd
from utils.tools import to_timestamp


class PositionSplit:
    """
    Input a tuple as it's argument
    """

    def __init__(self, val):
        self.val = val
        self.hash_data = {'alarm': self.val[0:4],
                          'status': self.val[4:8],
                          'latitude': self.val[8:12],
                          'longitude': self.val[12:16],
                          'altitude': self.val[16:18],
                          'speed': self.val[18:20],
                          'direction': self.val[20:22],
                          'datetime': self.val[22:28]
                          }
        print 'self.hash_data   :', self.hash_data
        self.temp = to_bcd(self.hash_data['datetime'])
        self.hash_data['datetime'] = to_timestamp(self.temp)


if __name__ == '__main__':
    sample1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 99, 22, 1, 5, 17, 64, 25)
    instance1 = PositionSplit(sample1)
    print instance1.hash_data