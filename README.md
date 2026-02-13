# sglang-diffusion-routing

A demonstrative example of running SGLang Diffusion with a DP router, which supports `generation` (a lot of methods, including [SDE/CPS](https://github.com/sgl-project/sglang/pull/18806)) and `health_check`.

1. Copy all the codes of https://github.com/radixark/miles/pull/544 to here with sincere acknowledgment.
2. Write up a detailed README on how to use SGLang Diffusion Router to launch multiple instances and send requests.

For example, given that we can make a Python binding of the sglang-d router:

1. pip install sglang-d-router (For local development, clone the repository and run `pip install .` from the root directory.)
2. pip install "sglang[diffusion]"
3. launching command (how to use sglang-d-router to launch n sglang diffusion servers)
4. Sending demonstrative requests
