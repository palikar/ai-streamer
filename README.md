# AIStreamer

AIStreamer is my personal library/framework for streamlining the process of writing and deploying scripts for machine learning models, image processing and generally &ldquo;AI stuff&rdquo;. Hence *AIStream(lin)er*.


## Abstract

The last year I had to write quite the few project that deal with machine learning and/or computer vision. I almost all of the cases there was some substantial amount of boilerplate code that dealt now specifically with the task but rather the &ldquo;management&rdquo; of the written application/script. So at some point, I came up with the idea to write a simple framework that should abstract away the boilerplate code and allow to actually write the interesting parts of the scripts/applications without me every time worrying about how everything should come together. Furthermore, this framework allows me to structure my code better and not have it all over the place as this gets really confusing really fast (not to mention maintainability).


### Design goals

The core principles of the framework are as follows:

-   Flexibility - The framework should not limit what I can write. I should be able to write every model that I can write from scratch using [Tensorflow](https://www.tensorflow.org/%0A%0A), [Keras](https://keras.io/), [Opencv](https://opencv.org/) and what have you.
-   Extendability - adding new features should not require any substantial rewrites of the core components. The architecture should allow &ldquo;hot swappable&rdquo; components.
-   Sort of simple to use (at least when following the documentation). (This nicely ties up to the next point.)
-   Good documentation and clear architecture so that I can &ldquo;relearn&rdquo; everything with relative ease.


## Installation

The project is on [PyPi](https://pypi.org/) so you can simple install it through *pip*

```sh
pip install ai_streamer --user
```

For the latest version, you can also install it manually through *setup.py*.

```sh
git clone https://www.github.com/palikar/ai_streamer
cd ai_streamer
python setup.py install --user
```



To make sure everything (almost) works correctly, you can run the tests with [pytes](https://docs.pytest.org/en/latest/)

```sh
cd ai_streamer
pytest
```


## Documentation


## Examples
