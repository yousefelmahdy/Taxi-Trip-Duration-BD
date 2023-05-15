from mrjob.job import MRJob
import numpy as np

class HaversineDistanceMR(MRJob):

    def configure_args(self):
        super(HaversineDistanceMR, self).configure_args()
        self.add_passthru_arg('--lat1', type=float, help='Latitude of point 1')
        self.add_passthru_arg('--lng1', type=float, help='Longitude of point 1')
        self.add_passthru_arg('--lat2', type=float, help='Latitude of point 2')
        self.add_passthru_arg('--lng2', type=float, help='Longitude of point 2')

    def mapper(self, _, __):
        lat1 = self.options.lat1
        lng1 = self.options.lng1
        lat2 = self.options.lat2
        lng2 = self.options.lng2

        R = 6371  # Earth's radius in kilometers

        # Convert latitude and longitude values to radians
        lat1, lng1, lat2, lng2 = np.radians([lat1, lng1, lat2, lng2])

        # Calculate the differences between the two points
        dlat = lat2 - lat1
        dlng = lng2 - lng1

        # Apply the Haversine formula
        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlng / 2) ** 2
        c = 2 * np.arcsin(np.sqrt(a))
        h = R * c

        yield None, h

    def reducer(self, _, distances):
        # Return the haversine distance as the output
        yield None, sum(distances)


if __name__ == '__main__':
    HaversineDistanceMR.run()
