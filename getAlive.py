import face.server as server
import threading
import tools.general as general


a = 0

if __name__ == "__main__":
    s = server.Server("Terminator")
    s.start()
