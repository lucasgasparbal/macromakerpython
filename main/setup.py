from setuptools import setup

setup(
    name='macromakerpython',
    version='0.0.1',
    packages=['macromaker', 'macromaker.template', 'macromaker.conditionparsing'],
    package_dir={'': 'main'},
    url='https://github.com/lucasgasparbal/macromakerpython',
    license='',
    author='Lucas Ballester',
    author_email='lucasgasparbal@gmail.com',
    description='console based macromaker for WoW'
)
