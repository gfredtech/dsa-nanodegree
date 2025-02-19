import math


class Node(object):
    def __init__(self, element = None, priority = None):
        self.element = element
        self.priority = priority


class min_priority_queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not self.queue

    def enqueue(self, element, priority):
        node = Node(element, priority)
        if self.is_empty():
            self.queue.append(node)
            return
        for index, queueItem in enumerate(self.queue):
            if node.priority < queueItem.priority:
                self.queue.insert(index, node)
                return
        self.queue.append(node)

    def dequeue(self):
        return self.queue.pop(0)

    def __repr__(self):
        return ''.join([str(inde) + ' - ' + str(queueItem.priority) + ' - ' +
            str(queueItem.element) + '\n' for index, queueItem in enumerate(self.queue)])

def calculate_distance(point_xy1, point_xy2):
    #euclidean distance
    x1, y1 = point_xy1[0], point_xy1[1]
    x2, y2 = point_xy2[0], point_xy2[1]
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def shortest_path(M, start, goal):
    print("shortest path called")
    mpq = min_priority_queue()
    mpq.enqueue(start, 0)

    # points or paths prior to the paths in the frontier
    explored = {}
    explored[start] = None
    unexplored = None
    cost_estimate = {}
    cost_estimate[start] = 0

    while not mpq.is_empty():
        low_pri_removed = mpq.dequeue()
        current, l_priority = low_pri_removed.element, low_pri_removed.priority
       

        if current == goal:
            best_path = []
            # backtrack through the explored points
            while current != start:
                best_path.append(current)
                current = explored[current]
            best_path.append(start)
            # reverse it -> start to goal
            return best_path[::-1]

        for path in M.roads[current]:
            # total cost through the current point/road to the next point/road
            total_cost = cost_estimate[current] + calculate_distance(M.intersections[current], M.intersections[path])
            if path not in cost_estimate or total_cost < cost_estimate[path]:
                cost_estimate[path] = total_cost
                cost_value = total_cost + calculate_distance(M.intersections[path], M.intersections[goal]) #minimum priority for the priority queue
                mpq.enqueue(path, cost_value) # add it to the queue
                explored[path] = current
    # mpq is empty but goal was not found
    return -1