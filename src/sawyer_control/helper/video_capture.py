import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.insert(0,'/opt/ros/kinetic/lib/python2.7/dist-packages')
# import cv2
import queue, threading, time

# bufferless VideoCapture
class VideoCapture:
  streams = {}

  def __init__(self, name):
    print("starting video stream", name)
    self.name = name
    if name in self.streams:
        print("already started, returning stream")
        return

    cap = cv2.VideoCapture(name)
    if not cap.isOpened():
        print("Error opening resource: " + str(name))
        print("Maybe opencv VideoCapture can't open it")
        exit(0)
    q = queue.Queue()
    self.streams[name] = (cap, q)
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      cap, q = self.streams[self.name]
      ret, frame = cap.read()
      if not ret:
        break
      if not q.empty():
        try:
          q.get_nowait()   # discard previous (unprocessed) frame
        except queue.Empty:
          pass
      q.put(frame)

  def read(self):
    cap, q = self.streams[self.name]
    return q.get()

if __name__ == "__main__":
  import sys
  resource = int(sys.argv[1])
  # resource = 4 # "/dev/video1"
  cap = VideoCapture(resource)
  frame = cap.read()
  cv2.imwrite("frame.png", frame)
