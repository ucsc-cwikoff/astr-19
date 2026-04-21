class FennecFox:
    def __init__(self):
        self.armLen = 8.0
        self.legLen = 8.0
        self.eyeNum = 2
        self.hasTail = True
        self.isFurry = True
    

def main():
    data = FennecFox()
    print(f"Fennec Foxes have an arm length of around {data.armLen} inches, "
          + f"and a leg lenth of the same size ({data.legLen} inches). "
          + f"They have {data.eyeNum} eyes. It is both {data.hasTail} "
          + f"that they have a tail, and {data.isFurry} that they are very fluffy.")

if __name__ == "__main__":
    main()