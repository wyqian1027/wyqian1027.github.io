class FreqStack:

    def __init__(self):
        self.counter = collections.Counter()
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.counter[x] += 1
        freq = self.counter[x]
        if freq > self.max_freq:
            self.max_freq = freq
        self.group[freq].append(x)

    def pop(self) -> int:
        
        x = self.group[self.max_freq].pop()
        self.counter[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x