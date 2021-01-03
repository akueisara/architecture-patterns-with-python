import abc

import model


@abc.abstractmethod
def add(self, batch: model.Batch):
    raise NotImplementedError


@abc.abstractmethod
def get(self, reference) -> model.Batch:
    raise NotImplementedError