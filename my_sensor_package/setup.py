from setuptools import setup

package_name = 'my_sensor_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tomasmartinik',
    maintainer_email='your-email@example.com',
    description='Radar and camera nodes for data acquisition',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'radar_node = my_sensor_package.radar_node:main',
            'camera_node = my_sensor_package.camera_node:main',
        ],
    },
)
