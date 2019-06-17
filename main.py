import sys

class PacMan ():
      def __init__(self, args):
            fileName = str(args[0])
            self.alpha = args[1]
            self.epsilon = args[2]
            self.times = args[3]


def main():
      args = sys.argv
      if len(args) < 4:
            print("Erro na quantidade de entradas")
            exit(1)

      game = PacMan(args)

if __name__ == "__main__":
    main()