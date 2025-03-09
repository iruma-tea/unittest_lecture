def test_func():
    """ pytestのテスト関数
    """
    assert 2 == 2


class TestPyTestClass:
    """ pytestのテストクラス"""

    def test_method(self):
        """pytestのテストメソッド"""
        assert 2 == 2

    def test_method_2(self):
        """pytestのテストメソッド"""
        assert "foo" == "foo"
