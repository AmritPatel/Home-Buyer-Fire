from src.getBox import getBox
from nose.tools import assert_almost_equal


def test_getBox():
    obs = getBox('11714 College View Drive   Maryland 20902', 0.1)
    exp = (39.04860820941063, 39.04570892556861, -77.06767891229457, -77.07139696932713)
    assert_almost_equal(exp, obs)
