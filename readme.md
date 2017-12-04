# A small test automation implementation
## Environment Setup
1. Install:
	* [Git](http://git-scm.com/)
	* [Python](https://www.python.org/downloads/) 
	* [pip](https://pypi.python.org/pypi/pip)

2. Use pip to install selenium , behave and request 
	* sudo pip install selenium 
	* sudo pip install behave

3. Clone the repository.
	* `cd {YOUR_GIT_HOME}`
	* `git clone https://github.com/ivanskyeng/test_task.git'

4. Set up your path
	* Add following path to your bash profile
	${YOUR_LOCAL_PATH}/features:{YOUR_LOCAL_PATH}/features/steps:{YOUR_LOCAL_PATH}/features/support:$PYTHONPATH"

5. Run following command to exceute test 
	* export location="prod" (or export location="staging" - but there no env for it yet). This will execute test on Prod or Staging.
	* behave Case_1.feature --tags=prod  (This will execute all features with tag "prod")
