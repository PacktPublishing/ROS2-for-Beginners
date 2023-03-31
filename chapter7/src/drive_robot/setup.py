from setuptools import setup

package_name = 'drive_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='magnum',
    maintainer_email='ogunsdavis53@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'move_sub=drive_robot.move_sub.py',
        'velocity_drive=drive_robot.move_robot:main',
        'trangle=drive_robot.traingle_movement',
        'obstacle_avoidance=drive_robot.avoid_obstacle:main',
        ],
    },
)
