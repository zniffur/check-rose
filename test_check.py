from check import check_rose_html, check_rose, check_rose_print


def test_print():
    ret_code = check_rose_print()
    assert ret_code == 200


def test_string():
    mystring = check_rose()
    assert (mystring is not None)


def test_html():
    mystring = check_rose_html()
    assert (mystring is not None)
