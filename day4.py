from datetime import datetime
from enum import Enum


class EventType(Enum):
    START = 0
    SLEEP = 1
    WAKE  = 2

class Event:
    def __init__(self, event_type, event_time, event_data=None):
        self.type = event_type
        self.time = event_time
        self.data = event_data

    @staticmethod
    def from_log(line):
        dt = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
        msg = line[19:]
        event_type = None
        event_data = None
        if msg == "falls asleep":
            event_type = EventType.SLEEP
        elif msg == "wakes up":
            event_type = EventType.WAKE
        else:
            event_type = EventType.START
            event_data = int(msg.split()[1][1:])
        return Event(event_type, dt, event_data)

    def __str__(self):
        return "Event({}, {}, {})".format(self.type.name,
                    self.time, self.data)
    __repr__ = __str__


class Shift:
    def __init__(self, start, events):
        self.start = start
        self.events = events
        
        minutes = [False for m in range(60)]
        last = None
        for e in self.events:
            if e.type == EventType.SLEEP:
                last = e
            if e.type == EventType.WAKE:
                for m in range(last.time.minute, e.time.minute):
                    minutes[m] = True
        self.minutes = minutes

    def total_asleep(self):
        return sum(self.minutes)

    @staticmethod
    def gen_from_events(events):
        events = sorted(events, key=lambda e: e.time)
        if len(events) == 0:
            return
        start = events[0]
        shift_events = []
        if len(events) == 1:
            yield Shift(start, shift_events)
            return
        for e in events[1:]:
            if e.type == EventType.START:
                yield Shift(start, shift_events)
                start = e
                shift_events = []
            else:
                shift_events.append(e)

    def __str__(self):
        return "Shift(start={}, events={})".format(self.start, self.events)
    __repr__ = __str__


class Guard:
    def __init__(self, guard_id, shifts=None):
        self.id = guard_id
        self.shifts = []
        self.totals = None
        if shifts:
            for s in shifts:
                self.add_shift(s)

    def add_shift(self, shift):
        self.shifts.append(shift)
        self.shifts = sorted(self.shifts, key=lambda s: s.start.time)
        self.totals = [sum(s.minutes[m] for s in self.shifts) for m in range(60)]

    def total_asleep(self):
        return sum(s.total_asleep() for s in self.shifts)

    def likely_minute(self):
        freq = max(self.totals)
        return self.totals.index(freq), freq

    def __str__(self):
        return "Guard(id={}, [{} shifts])".format(self.id, len(self.shifts))
    __repr__ = __str__


with open("day4_input.txt") as f:
    events = map(Event.from_log, f.read().rstrip().split('\n'))
    
    guards = {}
    for s in Shift.gen_from_events(events):
        if s.start.data not in guards:
            g = Guard(s.start.data)
            guards[s.start.data] = g
        else:
            g = guards[s.start.data]
        g.add_shift(s)
   
    # part 1
    g1 = sorted(guards.values(), key=lambda g: g.total_asleep())[-1]
    print(g1.id * g1.likely_minute()[0])

    # part 2
    g2 = sorted(guards.values(), key=lambda g: g.likely_minute()[1])[-1]
    print(g2.id * g2.likely_minute()[0])

