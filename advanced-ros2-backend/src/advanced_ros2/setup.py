from setuptools import setup

setup(
    name='advanced_ros2',
    version='0.0.0',
    packages=['advanced_ros2'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/advanced_ros2']),
        ('share/' + 'advanced_ros2', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='advanced-ros2 description',
    entry_points={
        'console_scripts': [
            'main = advanced_ros2.main:main'
        ],
    },
)