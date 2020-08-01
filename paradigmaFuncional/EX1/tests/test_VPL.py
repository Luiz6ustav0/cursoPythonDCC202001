from VPL_mSort import *

def test_givenTupple_whenGettingHead_shouldReturnTuppleHead():
    test_tuple = (1, (2, (3, None)))
    expected = 1

    result = head(test_tuple)

    assert result == expected

def test_givenNone_whenGettingHead_shouldReturnNone():
    test_tuple = None
    expected = None

    result = head(test_tuple)

    assert result == expected

def test_givenTupple_whenGettingTail_shouldReturnTuppleTail():
    test_tuple = (1, (2, (3, None)))
    expected = (2, (3, None))

    result = tail(test_tuple)

    assert result == expected

def test_givenNone_whenGettingTail_shouldReturnNone():
    test_tuple = ()
    expected = None

    result = tail(test_tuple)

    assert result == expected

def test_givenList_whenCallingpy2ll_shouldReturnLinkedlist():
    test_list = [1, 2, 3]
    expected = (1, (2, (3, None)))

    result = py2ll(test_list)

    assert result == expected

def test_givenEmptyList_whenCallingpy2ll_shouldReturnNone():
    test_list = []
    expected = None

    result = py2ll(test_list)

    assert result == expected

def test_givenTupple_whenCallingLL2py_shouldReturnPythonList():
    test_tupple = (1, (2, (3, None)))
    expected = [1, 2, 3]

    result = ll2py(test_tupple)

    assert result == expected

def test_givenNone_whenCallingLL2py_shouldReturnEmptyList():
    test_tupple = None
    expected = []

    result = ll2py(test_tupple)

    assert result == expected

def test_givenTupple_whenCalculatingSize_shouldReturnLength():
    test_tupple = (1, (2, (3, (4, None))))
    expected = 4

    result = size(test_tupple)

    assert result == expected

def test_givenNone_whenCalculatingSize_shouldReturnZero():
    test_tupple = None
    expected = 0

    result = size(test_tupple)

    assert result == expected

def test_givenNone_whenCallingSplit_shouldReturnNone():
    test_tupple = None
    expected = (None, None)

    result = split(test_tupple)

    assert result == expected

def test_givenLenOneTupple_whenCallingSplit_shouldReturnTheTwoHalfs():
    test_tupple = (1, (None))
    expected = (test_tupple, None)

    result = split(test_tupple)

    assert result == expected

def test_givenTupple_whenCallingSplit_shouldReturnTheTwoHalfs():
    test_tupple = (1, (2, (3, (4, None))))
    expected = ( (1, (3, None)), (2, (4, None)) )

    result = split(test_tupple)

    assert result == expected

def test_givenNone_whenCallingSorted_shouldReturnTrue():
    test_tupple = None
    expected = True

    result = sorted(test_tupple)

    assert result == expected

def test_givenOneElementTupple_whenCallingSorted_shouldReturnTrue():
    test_tupple = (1, (None))
    expected = True

    result = sorted(test_tupple)

    assert result == expected

def test_givenSortedTupple_whenCallingSorted_shouldReturnTrue():
    test_tupple = (1, (2, (3, (4, None))))
    expected = True

    result = sorted(test_tupple)

    assert result == expected

def test_givenFirstTupple_whenCallingMerge_shouldReturnItself():
    T0 = (1, (2, (3, None)))
    T1 = None
    expected = T0

    result = merge(T0, T1)

    assert result == expected

def test_givenSecondTupple_whenCallingMerge_shouldReturnItself():
    T0 = None
    T1 = (1, (2, (3, None)))
    expected = T1

    result = merge(T0, T1)

    assert result == expected

def test_givenTwoTupples_whenCallingMerge_shouldReturnMerged():
    T0 = (1, (2, (3, None)))
    T1 = (5, (4, (6, None)))
    expected = (1, (2, (3, (5, (4, (6, None))))))

    result = merge(T0, T1)

    assert result == expected

def test_givenNone_whenCallingSum_shouldReturnZero():
    T0 = None
    expected = 0

    result = sum(T0)

    assert result == expected

def test_givenOneElementTupple_whenCallingSum_shouldReturnHead():
    T0 = (1, (None))
    expected = 1

    result = sum(T0)

    assert result == expected

def test_givenTupple_whenCallingSum_shouldReturnSumOfAllElements():
    T0 = (1, (2, (3, None)))
    expected = 6

    result = sum(T0)

    assert result == expected

def test_givenTupple_whenCallingMax_returnsTheBiggestElement():
    T0 = (1, (2, (3, None)))
    expected = 3

    result = max(T0)

    assert result == expected

def test_givenTuppleAndN_whenCallingGet_shouldReturnNthElement():
    T0 = (8, (6, (5, None)))
    n = 2
    expected = 5

    result = get(T0, n)

    assert result == expected

def test_givenLargeTuppleAndN_whenCallingGet_shouldReturnNthElement():
    T0 = (8, (6, (5, (8, (6, (5, (13, (6, (5, None)))))))))
    n = 6
    expected = 13

    result = get(T0, n)

    assert result == expected

def test_givenTupple_whenCallingMSort_shouldReturnSortedTupple():
    test_tupple = (3, (2, (4, (1, None))))
    expected = (1, (2, (3, (4, None))))

    result = mSort(test_tupple)

    assert result == expected