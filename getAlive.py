print("-------------------------------------------------------------------------------------")
print("-------------------------starting application server---------------------------------")
import brain.config as config
import face.server as server


if __name__ == "__main__":
    server.start()
    config.display()

