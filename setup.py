from setuptools import setup

setup(
    name='CompassCrawler',
    version='1.0',
    packages=['course_scraper', 'course_scraper.spiders'],
    url='',
    license='',
    author='Jorge Frías',
    author_email='jofriasg@pa.uc3m.es',
    description='This is a utility to fetch courses information from UC3M website. In order to be extracted to COMPASS project data structure.',
    python_requires='>3.6',
    install_requires=[
            "Scrapy==1.5.0",
    ],

)

