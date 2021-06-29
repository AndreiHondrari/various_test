
import abc


class Subject(abc.ABC):

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class RealSubject(Subject):

    def do_something(self) -> None:
        print("RealSubject does something")


class SubjectProxy(Subject):

    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def do_something(self) -> None:
        print("Calling real subject from Proxy")
        self._real_subject.do_something()


class Client:

    def __init__(self, subject: Subject) -> None:
        self._subject = subject

    def set_subject(self, subject: Subject) -> None:
        self._subject = subject

    def do(self) -> None:
        print("Calling subject from client")
        self._subject.do_something()


if __name__ == '__main__':
    real_subject = RealSubject()
    proxied_subject = SubjectProxy(real_subject)
    client = Client(real_subject)

    print("# Call client with real subject ")
    client.do()

    print("\n# Call client with proxied subject ")
    client.set_subject(proxied_subject)
    client.do()
