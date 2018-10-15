import Basic3
import unittest

class test(unittest.TestCase):
    ''' 
        Simple Test case with English aplhabet with lower cases letters
     '''
    def test_code_1(self):
        aplha = "abcdefghijklmnopqrstuvwxyz"
        innp = 'b'
        toIncreaseBy = 2
        result = Basic3.sencode(aplha,innp, toIncreaseBy)
        self.assertEquals(result,'d')
    
    ''' 
        Test case with English aplhabet with lower cases letters with last letter
     '''
    def test_code_2(self):
        aplha = "abcdefghijklmnopqrstuvwxyz"
        innp = 'z'
        toIncreaseBy = 2
        result = Basic3.sencode(aplha,innp, toIncreaseBy)
        self.assertEquals(result,'b')

    ''' 
        Test case with English aplhabet with lower cases letters with last letter
     '''
    def test_code_3(self):
        aplha = "abcdefghijklmnopqrstuvwxyz"
        innp = 'z'
        toIncreaseBy = 26
        result = Basic3.sencode(aplha,innp, toIncreaseBy)
        self.assertEquals(result,'z')
    
    ''' 
        Test case with English aplhabet with a string
     '''
    def test_code_4(self):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        innp = 'the quick onyx goblin jumps over the lazy dwarf'
        toIncreaseBy = 2
        strin = ''
        for x in innp:
            if x==' ':
                strin = strin+ ' '
            else:
                strin = strin + Basic3.sencode(alpha, x, toIncreaseBy)
        self.assertEquals(strin,'vjg swkem qpaz iqdnkp lworu qxgt vjg ncba fycth')
    
    ''' 
        Test case with English aplhabet with a string but the direction is opposite
     '''
    def test_code_5(self):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        innp = 'vjg swkem qpaz iqdnkp lworu qxgt vjg ncba fycth'
        toIncreaseBy = -2
        strin = ''
        for x in innp:
            if x==' ':
                strin = strin+ ' '
            else:
                strin = strin + Basic3.sencode(alpha, x, toIncreaseBy)
        self.assertEquals(strin,'the quick onyx goblin jumps over the lazy dwarf')

if __name__ == '__main__':
    unittest.main()