from distutils.core import setup
setup(
  name = 'youtubetofacebook',         # How you named your package folder (MyLib)
  packages = ['youtubetofacebook'],   # Chose the same as "name"
  version = '0.0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'upload youtube video to the facebook page',   # Give a short description about your library
  author = 'Piriyaraj S',                   # Type in your name
  author_email = 'piriyaraj1998@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/piriyaraj/youtubetofacebook',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/piriyaraj/youtubetofacebook/archive/refs/tags/test.tar.gz',    # I explain this later on
  keywords = ['youtube', 'facebook', 'youtubeTofacebook'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 1 - Planning',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
  ],
)