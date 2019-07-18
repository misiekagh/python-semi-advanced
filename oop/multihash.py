from dataclasses import dataclass

BUCKET_SIZE = 16
INC_FACTOR = 2

@dataclass
class MultiHash:
    buckets=[[] for _ in range(BUCKET_SIZE)]
    payload_factor=0.25
    bucket_free=BUCKET_SIZE

    def add(self, e: str):
        bucket_no = hash(e) % BUCKET_SIZE
        self.buckets[ bucket_no ].append(e)
        if self.bucket_free/len(self.buckets) < self.payload_factor:
            self.inc_bucket_count()
        self.bucket_free -=1

    def __str__(self):
        return str([e for e in [b for b in self.buckets]])

    def __contains__(self, item):
        return self.contains(item)

    def contains(self, e):
        return(e in self.buckets[hash(e) % BUCKET_SIZE])

    def inc_bucket_count(self):
        new_size=INC_FACTOR * len(self.buckets)
        new_buckets=[[] for _ in range(new_size)]
        for b in self.buckets:
            for e in b:
                new_buckets[hash(e) % new_size].append(e)
