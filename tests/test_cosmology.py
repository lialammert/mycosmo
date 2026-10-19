import pytest

from mycosmo.cosmology import hubble, critical_density

FID_COSMO = {
    "H0": 70,
    "omega_m_0": 0.3,
    "omega_k_0": 0.0,
    "omega_lambda_0": 0.7,
}


@pytest.mark.parametrize(
    "redshift, expected",
    [
        (0.0, 70),
        (0.5, 91.60),
        (1.0, 123.24),
    ],
)
def test_hubble(redshift, expected):
    assert hubble(redshift, FID_COSMO) == pytest.approx(expected, abs=0.01)

@pytest.mark.parametrize(
    "redshift, expected",
    [
        (0.0, 9.3e-29),
        (0.5, 1.2e-28),
        (1.0, 1.8e-28),
    ],
)
def test_crit_density(redshift, expected):
    assert critical_density(redshift, FID_COSMO) == pytest.approx(expected, rel=1e-30)