import helperClass
reload(helperClass)
from helperClass import *
import time
import unittest

class Folders(unittest.TestCase):

    h = Helper("lab08-Homework")  # name of the jar

    def setUp(self):
        self.h.openSUT()
        #click(*tab that you want to open*)
        time.sleep(0.2)
        
    def tearDown(self):
        self.h.closeSUT()

    def test_menu(self):

        file = find("1618056125455.png")

        dragDrop(file, Location(100,100))

    def test_apps_delete(self):
        files = findAllList("1618056125455.png")
        blue = find("1618056478311.png")
        green = find("1618056494164.png")
        orange = find("1618056508960.png")
        size = len(files)

        folders = {
                blue:2,
                orange:0,
                green:1
                }

        for folder in folders.keys():
            for i in range(folders[folder]+1):
               
                dragDrop(files[0], folder)
                files = findAllList("1618056125455.png")

                k = 1
                if(i==folders[folder]-1):
                    k = 0
                            
                self.assertEquals(size-k,len(files))
                size = len(files)


    def test_move_folders(self):
        blue = find("1618056478311.png")
        green = find("1618056494164.png")     
        orange = find("1618056508960.png")

        dragDrop(blue, orange)
        self.assertTrue(exists("1618056478311.png"))
        dragDrop(green, orange)        


        self.assertTrue(exists("1618056494164.png"))

    def test_menu(self):

        screen =find("1618060448053.png")

        file = find("1618056125455.png")

        dragDrop(file, Location(screen.x, screen.y))

        rightClick(Location(screen.x,screen.y))

        hover(above(screen.y))

        menu = find("f07cbd7d2bdb3f9945d6491f309ddcea.png")

        self.assertTrue(menu.x >= screen.x)
        self.assertTrue(menu.y >= screen.y)
       




class Calculator(unittest.TestCase):

    h = Helper("lab08-Homework")  # name of the jar

    def setUp(self):
        self.h.openSUT()
        click("1618063139266.png")
        time.sleep(0.2)
        
    def tearDown(self):
        self.h.closeSUT()

    def test_calc_black(self):
        self.assertTrue(exists("1618062862971.png"))

        num = find("1618063304231.png")
        black = find("1618066416370.png")

        keyboard = find("1618067537487.png")
       
        

        exp_output = "1618067321870.png";
        up = 20
        x = 100
        nullLoc = Location(keyboard.x+50,keyboard.y+keyboard.h-20)
        X = nullLoc.x
        Y = nullLoc.y-50
        print(collectWords())
        for k in range(2):
            click(nullLoc)
            for i in range(3):
                X_help = X
                for j in range(3):
                    click(Location(X_help,Y))
                    X_help += 50
                Y -= 50  
            X = nullLoc.x
            Y = nullLoc.y-50
            
            

        self.assertTrue(exists(exp_output))
            #self.assertEquals(exp_output, r.collectLinesText()[0])
            
            

class Abi(unittest.TestCase):

    h = Helper("lab08-Homework")  # name of the jar

    def setUp(self):
        self.h.openSUT()
        click("1618063139266.png")
        time.sleep(0.2)
        
    def tearDown(self):
        self.h.closeSUT()

    def test_calc_purple(self):

        self.assertTrue(exists("1618065626706.png"))

        

        

        


        

     
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator)
    unittest.TextTestRunner(verbosity=3).run(suite)
    #reporter = createReporter(NAME)
    #reporter.run(suite)