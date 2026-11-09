class MinHeap:
    def __init__(self):
        # heap = [2, 5, 4, 9, 7, 8]
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        # heap = [2, 5, 4, 9, 7, 8, 3]
        i = len(self.heap) - 1 # 6

        while i > 0:
            # 1era vuelta: 6-1 // 2 = 2.5 = 2
            # 2da vuelta: 2-1 // 2 = 0.5 = 0
            parent = (i - 1) // 2 # div entera

            # 1era vuelta: heap[2] = 4  <= heap[6] = 3 - padre > hijo
            # 2da vuelta: heap[0] = 2  <= heap[2] = 3 padre < hijo - break
            if self.heap[parent] <= self.heap[i]:
                break # heap = [2, 5, 3, 9, 7, 8, 4]

            # intercambio posiciones
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            # i = 2
            i = parent

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")

        popped = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        i = 0

        while True:
            i_left = 2 * i + 1
            i_right = 2 * i + 2

            if i_left >= len(self.heap):
                break

            i_smallest = i_left

            if i_right < len(self.heap) and self.heap[i_right] < self.heap[i_left]:
                i_smallest = i_right

            if self.heap[i] <= self.heap[i_smallest]:
                break

            self.heap[i], self.heap[i_smallest] = (
                self.heap[i_smallest],
                self.heap[i],
            )

            i = i_smallest

        return popped

# peek, len, 