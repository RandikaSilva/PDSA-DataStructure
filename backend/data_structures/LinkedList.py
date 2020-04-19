from constants.errors import ERRORS

class Node:
    def __init__(self, station_name, next_station, distance):
        self.station_name = station_name
        self.distance = distance
        self.next_station = next_station

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def _add(self, src, next_station, distance):
        try:
            if(self.head == None):
                first = Node(src, next_station, distance)
                self.head = first
            else:
                tmp = self.head
                while(tmp.next_station != None):
                    tmp = tmp.next_station
                tmp.next_station = Node(src, next_station, distance)
        except Exception:
            return ERRORS.get("error")

    def _get(self, key):
        try:
            target_node = None
            temp = self.head
            while temp != None:
                if temp.station_name==key:
                    target_node=temp
                    break
                temp = temp.next_station
            if target_node is not None:
                return target_node
            else:
                return ERRORS.get("not_exist")
        except Exception:
            return ERRORS.get("error")

    def _pop(self, key):
        try:
            target_node = self.head
            target_node_prev = None
            while target_node.station_name != key:
                target_node_prev = target_node
                target_node = target_node.next_station
                if target_node is None:
                    break
            if target_node!=None:
                if target_node_prev != None:
                    target_node_prev.next_station = target_node.next_station
                else:
                    self.head = target_node.next_station
        except Exception:
            return ERRORS.get("error")

    def _get_all(self):
        station_list=[]
        current_station = self.head
        while current_station != None:
            station_list.append({current_station.station_name: current_station.distance})
            current_station = current_station.next_station
        return station_list

    def _print(self):
        current_station = self.head
        while current_station != None:
            print(str(current_station.station_name)+":"+str(current_station.distance))
            current_station = current_station.next_station

    def _update(self,key,station_name=None,distance=None):
        target_station = self._get(key)
        if station_name is None:
            target_station.distance=distance
        elif distance is None:
            if target_station is not None:
                target_station.station_name=station_name
        elif station_name and distance is not None:
            target_station.distance=distance
            target_station.station_name=station_name

class Graph:
    def __init__(self):
        self.stations = []
        self.stations_arr = []

    def _add(self, src, dest, distance):
        if src not in self.stations:
            self.stations_arr.append(SinglyLinkedList())
            self.stations.append(src)
        index = self.stations.index(src)
        self.stations_arr[index]._add(dest, None, distance)

    def _add_station(self,key):
        if key not in self.stations:
            self.stations_arr.append(SinglyLinkedList())
            self.stations.append(key)

    def _print_graph(self):
        for i in range(len(self.stations_arr)):
            print(str(self.stations[i])+"->")
            print(self.stations_arr[i]._print())
            print(" \n")
        if len(self.stations_arr) is 0:
            print("Graph empty")

    def _get(self, key):
        if key is not None:
            index = self.stations.index(key)
            if index is not None:
                node_list = self.stations_arr[index]
                return node_list._get_all()
        else:
            return []

    def _pop(self, key):
        if key is not None:
            index = self.stations.index(key)
            if index is not None:
                self.stations_arr.pop(index)
                self.stations.pop(index)
                for station in self.stations_arr:
                    station._pop(key)
        else:
            self.stations_arr = []

    def _update_station_distance(self,src,dest=None,station_name=None,distance=None):
        if src is not None:
            index = self.stations.index(src)
            if index is not None:
                if station_name is None:
                    node_list = self.stations_arr[index]
                    node_list._update(dest,None,distance)
                if dest is None:
                    for station in self.stations_arr:
                        station._update(src,station_name)
                    self.stations[index]=station_name
    
