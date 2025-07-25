from setuptools import find_packages, setup

package_name = 'hexapod_step_detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/hexapod_step_cycle.launch.py']),  # Add your launch file

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saieswaram',
    maintainer_email='saieswaram@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publish_gyro = hexapod_step_detection.publish_gyro:main',
        ],
    },
)
