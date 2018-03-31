from setuptools import setup

if __name__ == '__main__':
    setup(
        name='writed-up',
        description='Automation for writeups',
        author='kjscezy developers',
        author_email='meetmangukiya98@gmail.com',
        maintainer='kjscezy developers',
        maintainer_email=('meetmangukiya98@gmail.com', ),
        url='https://github.com/kjscezy/hacked-up-write-up',
        license='MIT',
        packages=['writedup'],
        entry_points={
            'console_scripts': [
                'writed-up=writedup.main:main',
            ]
        }
    )
