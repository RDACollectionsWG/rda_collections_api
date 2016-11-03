from setuptools import setup

setup(name='rda_collections_api',
      version='0.1',
      description='RDA Collections API',
      url='https://github.com/RDACollectionsWG/rda_collections_api',
      author='RDA Collections Working Group',
      author_email='rda-collection-wg@rda-groups.org',
      license='MIT',
      packages=['rda_collections_api', 'rda_collections_api.api'],
      include_package_data=True,
      zip_safe=False)
