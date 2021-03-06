import helperClass
import string
reload(helperClass)
from helperClass import *
import time
import unittest
import re

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

        box = find("1618200552934.png")

        keyboard = find("1618067537487.png")
       
        r = Region(box.x,box.y,box.w, box.h)

        exp_output = "1618067321870.png";
        up = 20
        x = 100
        nullLoc = Location(keyboard.x+50,keyboard.y+keyboard.h-20)
        X = nullLoc.x
        Y = nullLoc.y-50
        
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
        click(nullLoc)

        self.assertTrue(len(r.collectLinesText()[0]) <=20)


    def test_calc_purple(self):

        self.assertTrue(exists("1618065626706.png"))
        num = find("1618202041851.png")
        
        multiplication = find("1618201685932.png")

        purple = find("1618065626706.png")

        r = Region(purple.x,purple.y,purple.w, purple.h)

        click(num)
        click(multiplication)
        click(num)
                

        self.assertTrue(exists("1618224504332.png"))
        click(multiplication)

        self.assertTrue(exists("1618224504332.png"))

        
            
class Converter(unittest.TestCase):

    h = Helper("lab08-Homework")  #name of the jar

    def setUp(self):
        self.h.openSUT()
        click("1618224894063.png")
        time.sleep(0.2)
        
    def tearDown(self):
        self.h.closeSUT()  

    def test_text2uni(self):
        boxes = find("1618226002118.png")
        left_box = find("1618225076597.png")
        right_box = find("1618226379812.png")

        r = Region(right_box.x,right_box.y,right_box.w, right_box.h)

        click(left_box)
        type("hello world")
        click(r)
        click(r)
        mouseDown(Button.LEFT)
        mouseUp(Button.LEFT)
        wait(0.01)
        mouseDown(Button.LEFT)
        mouseUp(Button.LEFT)
        type("c",KEY_CTRL)

        tekst = Env.getClipboard()
        tekst = tekst.replace(" ","")

        self.assertTrue(tekst.isdigit())

    def test_fields(self):

        left_box = find("1618225076597.png")
        right_box = find("1618226379812.png")

        r = Region(right_box.x,right_box.y,right_box.w, right_box.h)
        
        click(left_box)

        type("a")

        click(r)

        type("b")

        click(r)
        mouseDown(Button.LEFT)
        mouseUp(Button.LEFT)
        wait(0.01)
        mouseDown(Button.LEFT)
        mouseUp(Button.LEFT)
        type("c",KEY_CTRL)

        tekst = Env.getClipboard()

        self.assertFalse("b" in tekst)

    def test_switch(self):

        switch = find("1618229479401.png")

        start = find("1618229726482.png")
        boxes = find("1618229969333.png")

        r = Region(switch.x,switch.y,switch.w,switch.h)

        s = Region(start.x,start.y,start.w,start.h)

        click(r)
        self.assertEquals(boxes, find("1618229969333.png"))

        click(r)


        self.assertEquals(start,find("1618229726482.png"))


    def test_uni2text(self):

        switch = find("1618229479401.png")
       
        left_box = find("1618225076597.png")
        right_box = find("1618226379812.png")

        warning = "Error! Not unicode"

        r = Region(right_box.x,right_box.y,right_box.w, right_box.h)

        click(switch)

        click(left_box)
        type("hello world")

        click(r)
        mouseDown(Button.LEFT)
        mouseUp(Button.LEFT)
        wait(0.01)
        mouseDown(Button.LEFT)
        mouseUp(Button.LEFT)
        type("c",KEY_CTRL)

        tekst = Env.getClipboard()

        self.assertEquals(warning, tekst)

        


        

class PinCode(unittest.TestCase):

    h = Helper("lab08-Homework")  # name of the jar
    
    def setUp(self):
        self.h.openSUT()
        click("1618157994928.png")
        time.sleep(0.2)
    def tearDown(self):
        self.h.closeSUT()

    def test_pin_x(self):
        numpad = find ("numpad.png")
        tab =find ("1618158104773.png")
        one = find("one.png")
        two = find("1618156526764.png")
        three = find("1618156552071.png")
        four = find("1618156578926.png")
        
        for j in  range(4):
            click(one)
            time.sleep(0.4)
            self.assertEquals( j+1,len(tab.findAllList("1618158294890.png")))
        click(one)
        time.sleep(0.4)
        self.assertEquals( 4,len(tab.findAllList("1618158294890.png")))
    def test_pin_unlock(self):
        numpad = find ("numpad.png")
        tab =find ("1618158104773.png")
        one = find("one.png")
        two = find("1618156526764.png")
        three = find("1618156552071.png")
        four = find("1618156578926.png")
        l = (one,two,three,four)

        for key in  l:
            click(key)  
        time.sleep(0.5)
         
        s = tab.collectLinesText()[0]
        m=re.search('Welcome, [A-Z][a-z]+!' ,s )   
        self.assertTrue(m != None)

    def test_pin_lock(self):
        tab =find ("1618158104773.png")
        one = find("one.png")
        for j in range(4):
            click(one)
        self.assertTrue(exists("1618159666091.png"))
        
class CatFlower(unittest.TestCase):

    h = Helper("lab08-Homework")  #name of the jar

    def setUp(self):
        self.h.openSUT()
        click("1618159836094.png")
        time.sleep(0.2)
        
    def tearDown(self):
        self.h.closeSUT()

    def test_place_cat(self):
        rocks = findAllList("1618160308422.png")
        test_rock = rocks[0]

        rockX = test_rock.x
        rockY = test_rock.y

        field_cats = Region(817,107,119,468)

        (test_cat,catType,types) = selectCat(field_cats)

        click(test_cat)
        
        
                    
         
        click(test_rock)
        time.sleep(0.3)
        new_rocks = findAllList("1618160308422.png")
        self.assertEquals(len(rocks)-1,len(new_rocks))

        isOnSelectedRock = False

        new_cats_of_type = findAllList(types[catType])
        print(len(new_cats_of_type))
        for cat in new_cats_of_type:
            print("CAT:",cat.x,cat.y)
            print("ROCK:",test_rock.x,test_rock.w,test_rock.y,test_rock.h)
            if(cat.x >=test_rock.x -10 and cat.x <= test_rock.x+test_rock.w +10 and cat.y >= test_rock.y -20 and cat.y <= test_rock.y+test_rock.h +20):
                isOnSelectedRock = True
        self.assertTrue(isOnSelectedRock)
        
    def test_cat_moves(self):
        lane = Region(340,216,470,122)
        test_rock = lane.find("1618160308422.png")
        rockX = test_rock.x
        rockY = test_rock.y

        field_cats = Region(817,107,119,468)
        (test_cat,catType,types) = selectCat(field_cats)
    
        click(test_cat)
        click(test_rock)
        time.sleep(0.2)
        cat = lane.find(types[catType])
        prevLoc = cat.x
        prevStep = -1
        step = -1
        for i in range(8):
            time.sleep(1)
            cat = lane.find(types[catType])
            print(cat.x,cat.y)
            step = prevLoc-cat.x
            if(i!=0):
                self.assertEquals(prevStep,step)
            prevStep=step
            prevLoc = cat.x

    def test_flower_gone(self):
        
    
        

        lane =Region(340,216,470,122)

        field_cats = Region(817,107,119,468)
        (test_cat,catType,types) = selectCat(field_cats)

        test_rock = lane.find("1618160308422.png")

        flower = lane.findAllList("1618167775626.png")[0]


        
        click(test_cat)
        click(test_rock)
        time.sleep(0.2)
        for i in range(8):
            time.sleep(1)
            cat = lane.find(types[catType])
            time.sleep(0.2)
            X = cat.x+cat.w//2
            if(X >= flower.x and X <= flower.x+flower.w):
                self.assertTrue(not(flower.exists("1618167775626.png")))



    def test_cats_win(self):
        field_flower =Region(338,220,469,353)

        field_cats = Region(817,107,119,468)
        

        rocks = field_flower.findAllList("1618160308422.png")
        

        for rock in rocks:
            (test_cat,catType,types) = selectCat(field_cats)
            click(test_cat)
            click(rock)
            time.sleep(0.2)
            self.assertTrue(not(exists("1618169804849.png")))
            

        time.sleep(8)
        self.assertTrue(exists("1618169804849.png"))
    
    def test_cat_backup(self):

        tab = Region(341,106,596,470)
        field_cats = Region(817,107,119,468)

        initial = len(findAllCatsInRegion(tab))
        
        rocks = tab.findAllList("1618160308422.png")
        rock = rocks[0]

        (test_cat,catType,types) = selectCat(field_cats)

        click(test_cat)
        click(rock)

        self.assertEquals(initial+1,len(findAllCatsInRegion(tab)))






            
            





def selectCat(region):
    type1 = Pattern("1618162633584.png")
    cat1=findAllList(type1)

    type2 = Pattern("1618162694294.png")
    cat2 = findAllList(type2)

    type3 = Pattern("1618162731550.png")
    cat3 = findAllList(type3)

    types = (type1,type2,type3)
    

    cats_of_type = [] 
    catType = -1
    for i,c in enumerate((cat1,cat2,cat3)):
        if(len(c)!=0):
            cats_of_type = c
            catType = i
            break;
    test_cat = cats_of_type[0]

    return (test_cat,catType,types)

def findAllCatsInRegion(region):
    type1 = Pattern("1618162633584.png")
    cat1=findAllList(type1)

    type2 = Pattern("1618162694294.png")
    cat2 = findAllList(type2)

    type3 = Pattern("1618162731550.png")
    cat3 = findAllList(type3)
    catsList = []
    for cats in (cat1,cat2,cat3):
        catsList.extend([cat for cat in cats])

    return catsList

        
if __name__ == '__main__':
    

    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    reporter = createReporter("HW7")
    reporter.run(suite)

    #unittest.TextTestRunner(verbosity=3).run(suite)
    #reporter = createReporter(NAME)
    #reporter.run(suite)