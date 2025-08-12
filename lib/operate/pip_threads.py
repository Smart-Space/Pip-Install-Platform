from concurrent.futures import ThreadPoolExecutor

class PipThreads:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=3)

    def submit(self, fn, *args, **kwargs):
        return self.executor.submit(fn, *args, **kwargs)

    def shutdown(self):
        self.executor.shutdown(wait=False, cancel_futures=True)
    
    def __del__(self):
        self.shutdown()

pipthreads=PipThreads()
