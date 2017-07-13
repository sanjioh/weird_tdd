# coding: utf-8
from iscontained import iscontained


def test_step1():
    assert iscontained([], []) is True


def test_step2():
    assert iscontained([1], []) is False


def test_step3():
    assert iscontained([], [1]) is True


def test_step4():
    assert iscontained([1], [1, 2]) is True


def test_step5():
    assert iscontained([1], [2, 1]) is True


def test_step6():
    assert iscontained([1, 3], [2, 1]) is False


def test_step7():
    assert iscontained([1, 2], [2, 1]) is True
