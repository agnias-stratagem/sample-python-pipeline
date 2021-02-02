#!/usr/bin/env python3

import pytest

from num_return.num_return import num_return

def test_num_return():
    one = num_return(1)
    assert one == 1


if __name__ == "__main__":
    pytest.main()

