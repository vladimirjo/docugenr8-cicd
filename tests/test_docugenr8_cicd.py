from docugenr8_cicd import example_sum


def test__example_sum() -> None:
    assert example_sum(1, 2) == 3
