class Square:

    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.compute_area()
        self.compute_perimeter()


    def header(self):
        print("Input the dimensions of the Square( equal Length and Width ): ")

    @classmethod
    def getDimensions(self):
        length = int(input("Length :"))
        width = int(input("Width: "))
        return self(length,width)

    def compute_area(self):
        area = self.width * self.length
        return area

    def compute_perimeter(self):
         return 2 * (self.length + self.width)


    def print_results(self):
        print("Perimeter and Area of the Square: ")
        area_result = self.compute_area()
        perimeter_result = self.compute_perimeter()
        print("Length : " + str(self.length))
        print("Width : " + str(self.width))
        print("Perimeter : " + str(perimeter_result))
        print("Area : " + str(area_result))

Square.header = classmethod(Square.header)
Square.header()
square = Square.getDimensions()
square.print_results()




