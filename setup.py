from setuptools import setup, find_packages

setup(name='NotifyBot',
      version='0.0.1',
      description='Python Client for LINE Notify API',
      author='Kashu Yamazaki',
      author_email='echo_six0566@yahoo.co.jp',
      url='https://github.com/Kashu7100/NotifyBot',
      packages=find_packages(),
      entry_points="""
      [console_scripts]
      register_notify_token = notifybot:register_token
      send_notify = notifybot:main
      """,
      include_package_data=True,
      )