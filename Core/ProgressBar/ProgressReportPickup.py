# Tai Sakuma <tai.sakuma@gmail.com>
import multiprocessing
import time

##__________________________________________________________________||
class ProgressReportPickup(multiprocessing.Process):
    def __init__(self, queue, presentation):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.presentation = presentation
        self.last_wait_time = 1.0 # [second]

    def run(self):
        self._run_until_the_end_order_arrives()
        self._run_until_reports_stop_coming()

    def _run_until_the_end_order_arrives(self):
        end_order_arrived = False
        while True:
            while not self.queue.empty():
                report = self.queue.get()
                if report is None: # the end order
                    end_order_arrived = True
                    continue
                self.presentation.present(report)
            if end_order_arrived: break

    def _run_until_reports_stop_coming(self):
        self._read_time()
        while self.presentation.nreports() > 0:
            if self._time() - self.last_time > self.last_wait_time: break
            while not self.queue.empty():
                report = self.queue.get()
                if report is None: continue
                self._read_time()
                self.presentation.present(report)

    def _time(self): return time.time()
    def _read_time(self): self.last_time = self._time()

##__________________________________________________________________||
