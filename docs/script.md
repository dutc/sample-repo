Script
------

## 1. Sign-up for Github

http://mail.com/
- E-mail:   johnsmithpse@mail.com
- Password: TIP1234pse
- Security Question: What city were you born in? Tel Aviv

Go to github.com
- Username:  johnsmithpse
- E-mail:    johnsmithpse@gmail.com
- Password:  TIP1234pse

https://github.com/settings/keys

```sh
$ ssh-add -K ~/id_rsa
```

## 2. Fork repo

https://github.com/telecominfraproject/sample-repo

## 3. Clone locally

$ git clone ssh://git@github.com/johnsmithpse/sample-repo

## (4. Install Anaconda)
https://www.anaconda.com/download

Choose Python 3.6 version.

Direct links:
- Linux: https://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh
- macos: https://repo.continuum.io/archive/Anaconda3-5.0.0-MacOSX-x86_64.pkg

## 4a. Create virtual environment

```sh
$ python -m venv venv
```

## 4b. Activate virtual environment

```sh
$ source venv/bin/activate
$ which python
```

## (4c. Deactivate virtual environment)

```sh
$ which python
$ deactivate
$ which python
```

## 5. Install dependencies

```sh
$ pip install -r requirements.txt
```

## 6. Install package

```sh
$ python setup.py install
```

## 7. Run tests, notice test failure

```sh
$ python setup.py test
```

```sh
$ open result_images/test_statistics/average-*.png
```

## 8. Submit issues, discussing test failure

### (i)

```
test_statistics.py:test_plot_average test failure

The test was updated but the new expected output was not updated.

FIX: Update test image
```

### (ii)

```
test_statistics.py:test_average test failure

Comparison of floating-point numbers in test fails.

FIX: Use math.isclose
```

## 9. Make code change fixing bug

```sh
$ git checkout -b fix-tests
```

### (i)

```sh
$ mv result_images/test_statistics/average.png tests/baseline_images/test_statistics/average.png
```

### (ii)

```python
from math import isclose
assert isclose(average(f, 15.777, rel_tol=1e-3))
```

## 10. Commit change(s)

### (i)

```sh
$ git commit tests/baseline_images/test_statistics/average.png
```

```
Updated expected test image for test_statistics (#....)
```

```sh
$ git push origin fix-tests
```

### (ii)

```sh
$ git commit tests/test_statistics.py
```

```
Fixed incorrect floating-point comparison in test_statistics (#....)
```

```sh
$ git push origin fix-tests
```

## 11. Rebase into logical commit

```sh
$ git rebase -i fix-tests~2
```

```
Fix test_statistics (#...., #....)

Updated expected test image for test_statistics (#....)
Fixed incorrect floating-point comparison in test_statistics (#....)
```

## 12. Push to Github

```sh
$ git push origin fix-tests
```

## 13. Submit pull request
## 14. Code review process
## 15. Code accepted, close issue, pull updated code

```sh
$ git remote add upstream https://github.com/Telecominfraproject/sample-repo
$ git fetch upstream master
$ git reset --hard upstream/master
```

## 16. Make code change adding new feature

```sh
$ git checkout -b variance
```

### edit sample/statistics.py

```python
def variance(xs):
    sq_total, total, count = scan(add, ((x**2, x, 1) for x in xs))
    return sq_total/count - (total/count)**2
```

```
$ git commit sample/statistics.py
```

```
add variance function

Computes variance of a sequence.
```

## 17. Push to Github, submit pull request

```
$ git push origin variance
```

## 18. Code review indicates inadequate documentation
## 19. Add proper documentation

### edit sample/statistics.py
```python
def variance(xs):
    '''
    population variance of a sequence

    :param xs: the sequence
    '''
    sq_total, total, count = scan(add, ((x**2, x, 1) for x in xs))
    return sq_total/count - (total/count)**2
```

```sh
$ git commit sample/statistics.py
```

## 20. Squash commits, push to Github, comment on pull request

```sh
$ git rebase -i variance~2
```

## 21. Code review indicates inadequate testing
## 22. Add testing

### edit sample/statistics.py
```python
def variance(xs):
    '''
    population variance of a sequence

    :param xs: the sequence

    >>> variance(range(10))
    8.25
    '''
    sq_total, total, count = scan(add, ((x**2, x, 1) for x in xs))
    return sq_total/count - (total/count)**2
```

### edit tests/test_statistics.py
```python
from sample import variance

def test_variance():
    f = islice(fib(), 1 10)
    assert isclose(variance(f), 294.839, rel_tol=1e-3)
```

### edit sample/statistics.py
```python
def variance(xs):
    '''
    population variance of a sequence

    :param xs: the sequence

    >>> variance(range(10))
    8.25
    '''
    sq_total, total, count = tail(scan(add, ((x**2, x, 1) for x in xs)))[0]
    return sq_total/count - (total/count)**2
```

## 23. Squash commits push to Github, comment on pull request

```sh
$ git rebase -i variance~2
```

## 24. Code accepted, pull updated code

```sh
$ git fetch upstream master
$ git reset --hard upstream/master
```
