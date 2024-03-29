from setuptools import setup
from setuptools_scm.version import get_local_dirty_tag


def clean_scheme(version):
    return get_local_dirty_tag(version) if version.dirty else "+clean"

setup(use_scm_version={"local_scheme": clean_scheme})
