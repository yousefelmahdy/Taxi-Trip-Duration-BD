from mrjob.job import MRJob
from math import fabs
import sys

class ManhattanDistanceJob(MRJob):
    
    def configure_args(self):
        super().configure_args()
        self.add_passthru_arg('--lat1', type=float, help='Latitude 1')
        self.add_passthru_arg('--lng1', type=float, help='Longitude 1')
        self.add_passthru_arg('--lat2', type=float, help='Latitude 2')
        self.add_passthru_arg('--lng2', type=float, help='Longitude 2')
        
    def mapper_init(self):
        lat1 = self.options.lat1
        lng1 = self.options.lng1
        lat2 = self.options.lat2
        lng2 = self.options.lng2
        self.distance = fabs(lng1 - lng2) + fabs(lat1 - lat2)
        
    def mapper(self, _, __):
        yield None, self.distance
        
    def reducer(self, _, distances):
        yield None, sum(distances)
        
if __name__ == '__main__':
    ManhattanDistanceJob.run()
