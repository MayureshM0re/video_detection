from setuptools import setup

package_name = 'video_detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'video_publisher',  # Registers video_publisher.py
        'yolo_subscriber'   # Registers yolo_subscriber.py
    ],
    package_dir={'': 'scripts'},  # Tell setuptools to find the scripts here
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mayuresh',
    maintainer_email='mayuresh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'video_publisher = video_publisher:main',  # Registers publisher script
            'yolo_subscriber = yolo_subscriber:main',  # Registers subscriber script
        ],
    },
)

