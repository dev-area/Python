import unittest
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    def test_default_size(self):
        self.assertEqual(self.widget.size(),(50,50),'incorrect default size')
    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(),(100,150),'wrong size after resize')

def suite():
    tests = ['test_default_size', 'test_resize']
    return unittest.TestSuite(map(WidgetTestCase, tests))


unittest.TextTestRunner(verbosity=2).run(suite())

