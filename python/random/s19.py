from typing import Optional


class Message:
    pass


class Organism:

    @property
    def message(self):
        return self._message

    def __init__(self, name):
        self._name = name
        self._message: Optional[Message] = None

    def __str__(self):
        return f"Organism({self._name})"

    def learn(self, message):
        print(f"L | {str(self)} learns {message}")
        self._message = message

    def hear(self, message: Optional[Message]):
        print(f"H | {str(self)} hears: {message}")


class CommunicationChannel:

    def __init__(self, organism_a, organism_b):
        self.organism_a = organism_a
        self.organism_b = organism_b

    def exchange(self):
        print(f"T | {str(self.organism_a)} and {str(self.organism_b)} talk")
        self.organism_b.hear(self.organism_a.message)
        self.organism_a.hear(self.organism_b.message)


if __name__ == "__main__":

    o1 = Organism("Katia")
    o2 = Organism("Sophia")
    o3 = Organism("Maxima")

    o1.learn("Lipsum dolores")
    o2.learn("Three is bigger than two")

    c1 = CommunicationChannel(o1, o2)
    c1.exchange()
