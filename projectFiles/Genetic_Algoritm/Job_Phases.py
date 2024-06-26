
class Phases:
    def __init__(self, job, phase_order, machine, duration):
        self.job = job
        self.phase_order = phase_order
        self.machine = machine
        self.duration = duration

    def __repr__(self):
        return f"{self.job}, order {self.phase_order} , machine {self.machine}, duration {self.duration}"

    def __eq__(self, other):
        if isinstance(other, Phases):
            return self.job == other.job and self.phase_order == other.phase_order and self.machine == other.machine and self.duration == other.duration
        return False

    def __hash__(self):
        return hash((self.job, self.phase_order, self.machine, self.duration))


class ProcessPhases (Phases):
    def __init__(self, job, phase_order, machine, duration, start_time):
        super().__init__(job, phase_order, machine, duration)
        self.start_time = start_time

    def __repr__(self):
        return super().__repr__() + f" start time {self.start_time}"


