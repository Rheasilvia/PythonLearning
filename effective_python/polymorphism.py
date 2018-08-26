import os
from tempfile import TemporaryDirectory


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    # def __init__(self):
    #     super(__class__, self).__init__()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

    def read(self):
        return open(self.path).read()


class GenericWorker(object):
    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    # 类方法
    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_class))
        return workers


class LineCountWorker(GenericWorker):

    def map(self):
        pass

    def reduce(self):
        pass


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return exec(workers)


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    config = {'data_dir': tmpdir}
    result = mapreduce(LineCountWorker, PathInputData, config)
