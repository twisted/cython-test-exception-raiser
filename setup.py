from setuptools import Extension, setup
from Cython.Build import cythonize

# Py_LIMITED_API values:
#
# 0x03080000 - Python 3.8 - the minimum version that Cython supports.
# 0x030B0000 - Python 3.11 - support typed memoryviews.
# 0x030C0000 - Python 3.12 - support vectorcall (performance improvement).

setup(
    ext_modules=cythonize([
        Extension(
            name="raiser",
            sources=["cython_test_exception_raiser/raiser.pyx"],
            define_macros=[
                # For now we are at python 3.8 as we still support 3.10.
                ("Py_LIMITED_API", 0x03080000),
            ],
            py_limited_api=True
        ),
    ]),
    options={"bdist_wheel": {"py_limited_api": "cp38"}},
)
