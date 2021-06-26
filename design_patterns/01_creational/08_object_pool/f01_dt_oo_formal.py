import random
import time

from typing import List, Dict, Optional, cast


class NotFromPoolException(Exception):
    pass


class ResourceNotInUseException(Exception):
    pass


class Resource:

    _last_id = 0

    @property
    def identity(self) -> int:
        return self._id

    @property
    def owner_pool(self) -> 'Pool':
        return self._owner_pool

    def __init__(self, owner_pool: 'Pool') -> None:
        Resource._last_id += 1
        self._id: int = self._last_id

        self._owner_pool: 'Pool' = owner_pool

        # simulate long initialization time
        print(f"Creating resource {self._id} ...")
        sleep_duration = random.random()
        # time.sleep(sleep_duration)


class Pool:

    def __init__(self, size: int) -> None:
        self._available: List[Resource] = [Resource(self) for _ in range(size)]
        self._in_use: Dict[int, Resource] = dict()

    def __str__(self) -> str:
        return (
            f"Pool(\n"
            f"  Available: {[r.identity for r in self._available]}\n"
            f"  In use: {list(self._in_use.keys())}\n"
            f")"
        )

    def get_resource(self) -> Optional[Resource]:
        if len(self._available) <= 0:
            return None

        releaseable_resource: Resource = self._available.pop()
        self._in_use[releaseable_resource.identity] = releaseable_resource
        return releaseable_resource

    def release_resource(self, resource: Resource) -> None:
        if resource.owner_pool != self:
            raise NotFromPoolException

        if resource.identity not in self._in_use:
            raise ResourceNotInUseException

        self._in_use.pop(resource.identity)
        self._available.append(resource)


if __name__ == '__main__':
    print("# Create pool")
    pool = Pool(2)
    print(str(pool))

    print("\n# a. Pluck a resource")
    res1 = pool.get_resource()
    print(f"Plucked {res1.identity}")  # type: ignore
    print(str(pool))

    print("\n# b. Pluck a resource")
    res2 = pool.get_resource()
    print(f"Plucked {res2.identity}")  # type: ignore
    print(str(pool))

    print("\n# c. Pluck a resource")
    res3 = pool.get_resource()
    print(f"Plucked {res3}")
    print(str(pool))

    print("\n# d. Return a resource")
    print(f"Release {res2.identity}")  # type: ignore
    pool.release_resource(res2)  # type: ignore
    print(str(pool))

    print("\n# d. Return non-used resource")
    print(f"Release {res2.identity}")  # type: ignore
    try:
        pool.release_resource(res2)  # type: ignore
    except ResourceNotInUseException:
        print("Detected ResourceNotInUseException")
        print(str(pool))

    print("\n# f. Return a non-belonging resource")
    pool2 = Pool(1)
    non_related_res = pool2.get_resource()
    try:
        pool.release_resource(non_related_res)  # type: ignore
    except NotFromPoolException:
        print("Detected NotFromPoolException")
        print(str(pool))
