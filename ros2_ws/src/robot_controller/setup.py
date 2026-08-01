from setuptools import setup

package_name = "robot_controller"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Platform Engineering",
    maintainer_email="platform@example.com",
    description="Manufacturing robot controller subscriber.",
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "robot_controller = robot_controller.controller:main",
        ],
    },
)
