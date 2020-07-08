from itertools import combinations as thecombo
from itertools import permutations as theperm

import pytest

from algorithms.basic.choices import combinations as mycombo
from algorithms.basic.choices import permutations as myperm


@pytest.fixture(params=["abcde", "fairy", "dinner", "eevee"])
def content(request):
    return request.param


@pytest.mark.math
@pytest.mark.string
class TestPerm:
    def test_permutations(self, content):
        for rcur in range(1, len(content) + 1):
            tvalue = ["".join(v) for v in sorted(theperm(content, r=rcur))]
            mvalue = [v for v in myperm(content, r=rcur)]
            assert len(tvalue) == len(mvalue)
            assert tvalue == mvalue


@pytest.mark.math
@pytest.mark.string
class TestCombo:
    def test_combinations(self, content):
        for rcur in range(1, len(content) + 1):
            tvalue = ["".join(v) for v in sorted(thecombo(content, r=rcur))]
            mvalue = [v for v in mycombo(content, r=rcur)]
            assert len(tvalue) == len(mvalue)
            assert tvalue == mvalue
