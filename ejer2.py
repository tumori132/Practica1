readme = '''NumPy is the fundamental package needed for scientific computing with Python.

Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security
It provides:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities
Testing:

NumPy requires pytest. Tests can then be run after installation with:

python -c 'import numpy; numpy.test()'
Call for Contributions
The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good first issue" may be a good starting point. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

review pull requests
triage issues
develop tutorials, presentations, and other educational materials
maintain and improve our website
develop graphic design for our brand assets and promotional materials
translate website content
help with outreach and onboard new contributors
write grant proposals and help with other fundraising efforts
If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invite).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved.'''

charEspeciales = ''':/,-.'"()'''
for char in readme:      # voy por palabra
    if char in charEspeciales:     # veo si hay un char especial en la palabra
        readme = readme.replace(char, " ") # reemplazo por un espacio

readme = readme.lower()
readme_mod = readme.split() # creo la lista
readmeDicc = {}  

for palabra in readme_mod:  # la recorro
    if palabra in readmeDicc:  # si existe sumo uno, sino la creo
        readmeDicc[palabra] += 1
    else:
        readmeDicc[palabra] = 1

maxPalabra = ''
maxValor = -1
for key in readmeDicc:
    if readmeDicc[key] > maxValor:
        maxValor = readmeDicc[key]
        maxPalabra = key

print(f"la palabra mas repetida es: {maxPalabra} y se repitio: {maxValor} veces")